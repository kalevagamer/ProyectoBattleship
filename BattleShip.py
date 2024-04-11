import random
from juegobatallanaval import JuegoBatallaNaval
from jugador import Jugador
import os

def colocar_barcos(self, tablero):
        barcos_colocados = {}
        for barco, tamaño in self.barcos.items():
            orientación = random.choice(['horizontal', 'vertical'])
            if orientación == 'horizontal':
                fila = random.randint(0, self.filas - 1)
                columna = random.randint(0, self.columnas - tamaño)
                for c in range(columna, columna + tamaño):
                    tablero[fila][c] = barco[0]
            else:  # orientación == 'vertical'
                fila = random.randint(0, self.filas - tamaño)
                columna = random.randint(0, self.columnas - 1)
                for f in range(fila, fila + tamaño):
                    tablero[f][columna] = barco[0]
            barcos_colocados[barco] = (fila, columna, orientación)
        return barcos_colocados

def mostrar_lista_jugadores(juego):
    if not juego.jugadores:
        print("No hay jugadores registrados.")
    else:
        print("Lista de jugadores:")
        for i, jugador in enumerate(juego.jugadores, 1):
            print(f"{i}. Nombre: {jugador.nombre}, Nickname: {jugador.nickname}")

def empezar_juego(juego):
    if len(juego.jugadores) < 2:
        print("Debes tener al menos dos jugadores para empezar el juego.")
    else:
        print("El juego ha comenzado.")

def agregar_jugador(juego):
    nombre = input("Ingrese el nombre del jugador: ")
    nickname = input("Ingrese el nickname del jugador: ")
    juego.jugadores.append(Jugador(nombre, nickname))
    print(f"El jugador {nombre} ha sido agregado correctamente.")

def editar_jugador(juego):
    if not juego.jugadores:
        print("No hay jugadores para editar.")
        return
    nombre = input("Ingrese el nombre del jugador que desea editar: ")
    for jugador in juego.jugadores:
        if jugador.nombre == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre del jugador: ")
            nuevo_nickname = input("Ingrese el nuevo nickname del jugador: ")
            jugador.nombre = nuevo_nombre
            jugador.nickname = nuevo_nickname
            print(f"El jugador {nombre} ha sido editado correctamente.")
            return
    print(f"No se encontró un jugador con el nombre {nombre}.")

def salir_del_juego(juego):
    juego.juego_terminado = True

def mostrar_menu():
    print("\n--- BattleShip ---")
    print("1. Empezar juego")
    print("2. Agregar jugador")
    print("3. Editar jugador")
    print("4. Mostrar lista de jugadores")
    print("5. Salir del juego")

def ejecutar_opcion(juego, opcion):
    if opcion == 1:
        empezar_juego(juego)
    elif opcion == 2:
        agregar_jugador(juego)
    elif opcion == 3:
        editar_jugador(juego)
    elif opcion == 4:
        mostrar_lista_jugadores(juego)
    elif opcion == 5:
        print("Saliendo del Juego...")
        salir_del_juego(juego)
    else:
        print("Opción no válida. Presione enter para continuar")

def jugar():
    juego = JuegoBatallaNaval()
    while not juego.juego_terminado:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            ejecutar_opcion(juego, opcion)
        except ValueError:
            print("Error: Ingrese un número válido.")

# Ejecutar el juego
if __name__ == "__main__":
    jugar()

