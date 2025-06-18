'''Constantes globales.'''
PARED = '#'
CAJA = '$'
JUGADOR = '@'
OBJETIVO = '.'
OBJETIVO_CAJA = '*'
OBJETIVO_JUGADOR = '+'
VACIO = ' '
OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.'''
    grilla = []
    for i in range(len(desc)):
         grilla.append(list(desc[i]))
    return grilla
        
def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    f = len(grilla) 
    c = len(grilla[0])     
    return c, f

def hay_vacio(grilla, c, f):
    '''Devuelve True si hay un vacio en la columna y fila (c, f).'''
    return grilla[f][c] == VACIO
    
def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return grilla[f][c] == PARED
 
def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] == OBJETIVO or grilla[f][c] == OBJETIVO_CAJA or grilla[f][c] == OBJETIVO_JUGADOR

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return grilla[f][c] == CAJA or grilla[f][c] == OBJETIVO_CAJA
        
def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] == JUGADOR or grilla[f][c] == OBJETIVO_JUGADOR

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for f in range(len(grilla)):
        for c in range(len(grilla[0])):
            if hay_objetivo(grilla, c, f) and not hay_caja(grilla, c, f):
                return False
    return True

def posicion_jugador(grilla):
    '''Devuelve una tupla con la posicion del jugador.'''
    for f in range(len(grilla)):
        for c in range(len(grilla[0])):
            if grilla[f][c] == JUGADOR or grilla[f][c] == OBJETIVO_JUGADOR:
                return c, f
        
def es_movimiento_valido(grilla, direccion):
    '''Devuelve true si el movimiento es valido'''
    dx, dy = direccion
    c, f = posicion_jugador(grilla)
    if hay_pared(grilla, c + dx, f + dy):
        return False
    elif hay_caja(grilla, c + dx, f + dy) and hay_pared(grilla, c + (dx * 2), f + (dy * 2)):
        return False
    elif hay_caja(grilla, c + dx, f + dy) and hay_caja(grilla, c + (dx * 2), f + (dy * 2)):
        return False
    return True

def mover_caja(grilla, nueva_grilla, direccion):
    '''Modifica la nueva grilla en la posicion de la caja segun las condiciones.'''
    dx, dy = direccion
    c, f = posicion_jugador(grilla)
    if hay_caja(grilla, c + dx, f + dy):
        if hay_objetivo(grilla, c + (dx * 2), f + (dy * 2)):
            nueva_grilla[f + (dy * 2)][c + (dx * 2)] = OBJETIVO_CAJA
        elif not hay_pared(grilla, c + (dx * 2), f + (dy * 2)):
            nueva_grilla[f + (dy * 2)][c + (dx * 2)] = CAJA
    return nueva_grilla
    
def mover_jugador(grilla, nueva_grilla, direccion):
    '''Modifica la nueva grilla en la posicion del jugador segun las condiciones.'''
    dx, dy = direccion
    c, f = posicion_jugador(grilla)
    if hay_objetivo(grilla, c + dx, f + dy):
        nueva_grilla[f + dy][c + dx] = OBJETIVO_JUGADOR
    elif hay_caja(grilla, c + dx, f + dy) or not hay_pared(grilla, c + dx, f + dy):
        nueva_grilla[f + dy][c + dx] = JUGADOR
    return nueva_grilla
            
def posicion_jugador_anterior(grilla, nueva_grilla):
    '''Modifica la nueva grilla en la posicion anterior del jugador si hay un objetivo o no.'''
    c, f = posicion_jugador(grilla)
    if grilla[f][c] == JUGADOR:
        nueva_grilla[f][c] = VACIO
    else:
        nueva_grilla[f][c] = OBJETIVO
    return nueva_grilla
        
def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.'''
    nueva_grilla = crear_grilla(grilla)
    if es_movimiento_valido(grilla, direccion):
        mover_caja(grilla, nueva_grilla, direccion)
        mover_jugador(grilla, nueva_grilla, direccion)
        posicion_jugador_anterior(grilla, nueva_grilla)
    return nueva_grilla
