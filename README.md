# Juego Sokoban

Este repositorio contiene el desarrollo del Trabajo Práctico 3 de la materia **Algoritmos y Programación I** (Universidad de Buenos Aires - Facultad de Ingeniería). Se trata de una implementación del clásico juego **Sokoban**, incluyendo lógica de juego, niveles personalizados, estructuras de datos y una interfaz gráfica desarrollada con `gamelib`.

---

## 📦 Contenido

El proyecto incluye los siguientes archivos y módulos:

- `main.py`: punto de entrada principal para iniciar el juego.
- `soko.py`: lógica del juego (movimiento del jugador, verificación de victoria, carga de niveles, etc.).
- `mostrar_juego.py`: módulo encargado de renderizar el juego en pantalla mediante `gamelib`.
- `niveles.txt`: archivo de texto con los distintos niveles que el jugador puede resolver.
- `cola.py` y `pila.py`: estructuras de datos implementadas manualmente para prácticas del curso.
- `img/`: carpeta que contiene los sprites del juego (jugador, caja, pared, objetivo, etc.).
- `teclas.txt`: configuración de teclas que utiliza el juego.

---

## 🚀 Cómo ejecutar el juego

### 1. Requisitos

- Python 3.x
- Librería `gamelib` (incluida en el repositorio como parte del entorno de la materia)

### 2. Instrucciones

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Soko-Ban-SokoBan.git
   cd Soko-Ban-Soko-Ban/Soko-Ban

2. Ejecutar el codigo:
``bash
  python3 main.py`

3. Cómo jugar
Usá las teclas de flecha para mover al personaje.

El objetivo es empujar todas las cajas hasta sus respectivos lugares objetivo (marcados con un punto).

Solo se pueden empujar cajas (no tirar).

El juego avanza automáticamente al siguiente nivel una vez resuelto el actual.

📚 Créditos
Autor: Estefano Polizzi

Carrera: Ingeniería Informática

Universidad: Universidad de Buenos Aires – Facultad de Ingeniería

Materia: Algoritmos y Programación I

Cuatrimestre: Segundo Cuatrimestre 2022


