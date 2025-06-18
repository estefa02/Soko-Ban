import soko
import gamelib
from pila import Pila
from cola import Cola
from mostrar_juego import primer_pos

def fila_mas_larga(desc):
    '''Devuelve la fila mas larga de la descripcion'''
    fil_mas_larga = 0
    for i in range(len(desc)):
            if len(desc[i]) > fil_mas_larga:
                fil_mas_larga = len(desc[i])
    return fil_mas_larga

def corregir_desc(desc):
    '''Corrige la descripcion para que sea cuadrada'''
    fila_larga = fila_mas_larga(desc)
    desc_cuadrado = []
    for fila in desc:
        veces = fila_larga - len(fila)
        for j in range(veces):
            fila += ' '
        desc_cuadrado.append(fila)
    return desc_cuadrado

def leer_nivel(niveles):
    '''Lee el archivo de niveles, y devuelve un diccionario con los niveles en la clave y la descripcion como valor'''
    lista_de_niveles = []
    desc = []
    with open(niveles) as archivo:
        for lineas in archivo:
            linea = lineas.rstrip('\n')
            if linea.startswith('#') or linea.startswith(' '):
                desc.append(linea)
            if linea == '':
                nivel = corregir_desc(desc)
                grilla = soko.crear_grilla(nivel)
                lista_de_niveles.append(grilla)
                desc = []
        return lista_de_niveles
    
def leer_teclas(teclas):
    '''Lee el archivo de las teclas y devuelve un diccionario con la tecla como clave y la funcion como valor'''
    dicc = {}
    with open(teclas) as archivo:
        for lineas in archivo:
            linea = lineas.rstrip('\n').split(' = ')
            if linea[0] == '':
                continue
            else:
                dicc[linea[0]] = linea[1]
        return dicc
    
def actualizar_juego(nivel, pistas, tecla, teclas, hay_pistas):
    '''Devuelve el nivel actualizado según la tecla presionada'''
    if tecla in teclas:
        if teclas[tecla] == 'PISTAS':
            # El usuario presionó la tecla correspondiente, buscar/realizar pistas.
            if not hay_pistas:
                hay_solucion, pistas = buscar_solucion(nivel)
                if hay_solucion:
                    hay_pistas = True
                    return nivel, hay_pistas, pistas
            elif hay_pistas:
                nivel_actualizado = soko.mover(nivel, pistas.desapilar())
                return nivel_actualizado, hay_pistas, pistas
        else:
            # El usuario presionó la tecla correspondiente, realizar movimiento.
            direccion = saber_direccion(teclas[tecla])
            nivel_actualizado = soko.mover(nivel, direccion)
            return nivel_actualizado, hay_pistas, pistas
    return nivel, hay_pistas, pistas
    
def saber_direccion(movimiento):
    '''Identifica el movimiento y devolver la direccion'''
    direcciones = {'NORTE':(0, -1), 'SUR':(0, 1), 'ESTE':(1, 0) , 'OESTE':(-1, 0)}
    if movimiento in direcciones:
        return direcciones[movimiento]
    
def posicion_a_pixeles(c, f):
    '''Devuelve las coordenadas de la grilla en pixeles'''
    TAMANIO_CELDA = 64
    y = f * TAMANIO_CELDA
    x = c * TAMANIO_CELDA
    return x, y
    
def mostrar_juego(nivel, hay_pistas):
    '''Dibuja el juego en pantalla'''
    columnas, filas = soko.dimensiones(nivel)
    for f in range(filas):
        for c in range(columnas):
            x, y = posicion_a_pixeles(c, f)
            gamelib.draw_image('img/ground.gif', x, y)
            if soko.hay_objetivo(nivel, c, f):
                gamelib.draw_image('img/goal.gif', x, y + 10)
            if soko.hay_jugador(nivel, c, f):
                gamelib.draw_image('img/player.gif', x, y)
            if soko.hay_pared(nivel, c, f) and not primer_pos(c,f):
                gamelib.draw_image('img/wall.gif', x + 8, y + 8)
            if soko.hay_caja(nivel, c, f):
                gamelib.draw_image('img/box.gif', x, y + 15)
    if hay_pistas:
        gamelib.draw_image('img/hay_pistas.gif', 5, 0)
    elif not hay_pistas:
        gamelib.draw_image('img/no_hay_pistas.gif', 5, 0)
             
def deshacer(nivel, pila_deshacer, pila_rehacer):
    '''Deshace un movimiento hecho y lo guarda en una pila'''
    if pila_deshacer.esta_vacia():
        return nivel, pila_rehacer
    nivel = pila_deshacer.desapilar()
    pila_rehacer.apilar(nivel)
    return nivel, pila_rehacer

def rehacer(nivel, pila_deshacer, pila_rehacer):
    '''Rehace un movimiento deshecho'''
    if pila_rehacer.esta_vacia():
        return nivel, pila_deshacer
    nivel = pila_rehacer.desapilar()
    pila_deshacer.apilar(nivel)
    return nivel, pila_deshacer

def buscar_solucion(estado_inicial):
    '''Busca solucion al nivel'''
    visitados = {}
    return backtrack(estado_inicial, visitados)

def backtrack(estado, visitados):
    '''Busca solucion al nivel con el algoritmo backtracking'''
    direcciones = [soko.SUR, soko.OESTE, soko.NORTE, soko.ESTE]
    for movimiento in direcciones:
        visitados[str(estado)] = movimiento
        if soko.juego_ganado(estado):
            return True, Pila()
        if estado != soko.mover(estado, movimiento):
            nuevo_estado = soko.mover(estado, movimiento)
            if str(nuevo_estado) in visitados:
                continue
            solucion_encontrada, acciones = backtrack(nuevo_estado, visitados)
            if solucion_encontrada:
                acciones.apilar(movimiento)
                return True, acciones
    return False, None

def inicializar_nivel(niveles, clave):
    '''Inicializa los valores por defecto'''
    nivel = niveles[clave]
    pila_deshacer = Pila()      #Inicializo pila para deshacer movimiento
    pila_deshacer.apilar(nivel) #Apilo el nivel inical
    pila_rehacer = Pila()       #Inicializo pila para rehacer movimiento
    pistas = Pila()              
    hay_pistas = False          #No hay pistas disponibles
    return pila_deshacer, pila_rehacer, pistas, hay_pistas, nivel, clave
    

def main():
    try:
        niveles = leer_nivel('niveles.txt')
    except FileNotFoundError:
        print('Archivo de niveles no encontrado')
    try:
        teclas = leer_teclas('teclas.txt')
    except FileNotFoundError: 
        print('Archivo de niveles no encontrado')
    clave = 0
    pila_deshacer, pila_rehacer, pistas, hay_pistas, nivel, clave = inicializar_nivel(niveles, clave)
    # Inicializar el estado del juego
    c, f = soko.dimensiones(nivel)
    ancho_ventana, alto_ventana = posicion_a_pixeles(c, f)
    gamelib.resize(ancho_ventana, alto_ventana)

    while gamelib.is_alive():
        gamelib.draw_begin()
        mostrar_juego(nivel, hay_pistas)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        
        if ev.type == gamelib.EventType.KeyPress and teclas.get(ev.key) == 'SALIR':
            # El usuario presionó la tecla correspondiente, cerrar la aplicación.
            break
        
        if ev.type == gamelib.EventType.KeyPress and teclas.get(ev.key) == 'REINICIAR':
            # El usuario presionó la tecla correspondiente, reiniciar nivel.
            pila_deshacer, pila_rehacer, pistas, hay_pistas, nivel, clave = inicializar_nivel(niveles, clave)
            continue
        
        if ev.type == gamelib.EventType.KeyPress and teclas.get(ev.key) == 'DESHACER':
            # El usuario presionó la tecla correspondiente, deshacer movimiento.
            nivel, pila_rehacer = deshacer(nivel, pila_deshacer, pila_rehacer)
            continue
        
        if ev.type == gamelib.EventType.KeyPress and teclas.get(ev.key) == 'REHACER':
            # El usuario presionó la tecla correspondiente, rehacer movimiento.
            nivel, pila_deshacer = rehacer(nivel, pila_deshacer, pila_rehacer)
            continue
        
        else:
            tecla = ev.key
            nivel, hay_pistas, pistas = actualizar_juego(nivel, pistas, tecla, teclas, hay_pistas) 
            pila_deshacer.apilar(nivel)
            pila_rehacer = Pila() #Si el usuario realiza un movimiento, se reinicia la pila para rehacer movmiento.
            # Actualizar el estado del juego, según la `tecla` presionada.
            if soko.juego_ganado(nivel):
                clave += 1
                pila_deshacer, pila_rehacer, pistas, hay_pistas, nivel, clave = inicializar_nivel(niveles, clave)
                # Avanzar de nivel, si ganó
                c, f = soko.dimensiones(nivel)                        #Redimensiono la grilla  
                ancho_ventana, alto_ventana = posicion_a_pixeles(c, f)#para hacer
                gamelib.resize(ancho_ventana, alto_ventana)           #resize de la ventana.

gamelib.init(main)