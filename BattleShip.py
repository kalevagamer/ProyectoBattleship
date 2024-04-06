import os
from jugador import Jugador

class JuegoBatallaNaval:
    def __init__(self):
        self.filas = 20
        self.columnas = 20
        self.tablero_jugador1 = [['-' for _ in range(self.columnas)] for _ in range(self.filas)]
        self.tablero_jugador2 = [['-' for _ in range(self.columnas)] for _ in range(self.filas)]
        self.tablero_jugador1_objetivo = [['-' for _ in range(self.columnas)] for _ in range(self.filas)]
        self.tablero_jugador2_objetivo = [['-' for _ in range(self.columnas)] for _ in range(self.filas)]
        self.barcos = {'Destructor': 6, 'Crucero': 4, 'Acorazado': 2}
        self.barcos_jugador1 = self.colocar_barcos(self.tablero_jugador1)
        self.barcos_jugador2 = self.colocar_barcos(self.tablero_jugador2)
        self.turno = 1
        self.juego_terminado = False
        self.jugadores = []

    def colocar_barcos(self, tablero):
        # Lógica para colocar aleatoriamente los barcos en el tablero
        pass

    def guardar_juego(self, nombre_archivo):
        # Lógica para guardar el estado actual del juego en un archivo
        pass

    def cargar_juego(self, nombre_archivo):
        # Lógica para cargar un juego guardado previamente desde un archivo
        pass

    def atacar(self, jugador, fila, columna):
        # Lógica para manejar los ataques de los jugadores y actualizar los tableros en consecuencia
        pass

    def verificar_ganador(self):
        # Lógica para verificar si algún jugador ha ganado el juego
        pass

    def imprimir_tablero(self, tablero):
        print("   ", end="")
        for i in range(self.columnas):
            print(f"{i:2}", end=" ")
        print()
        for i in range(self.filas):
            print(f"{i:2}", end=" ")
            for j in range(self.columnas):
                print(tablero[i][j], end=" ")
            print()

    def mostrar_lista_jugadores(self):
        if not self.jugadores:
            print("No hay jugadores registrados.")
        else:
            print("Lista de jugadores:")
            for i, jugador in enumerate(self.jugadores, 1):
                print(f"{i}. Nombre: {jugador.nombre}, Nickname: {jugador.nickname}")

    def empezar_juego(self):
        if len(self.jugadores) < 2:
            print("Debes tener al menos dos jugadores para empezar el juego.")
            return
        print("El juego ha comenzado.")

    def agregar_jugador(self):
        nombre = input("Ingrese el nombre del jugador: ")
        nickname = input("Ingrese el nickname del jugador: ")
        self.jugadores.append(Jugador(nombre, nickname))
        print(f"El jugador {nombre} ha sido agregado correctamente.")

    def editar_jugador(self):
        if not self.jugadores:
            print("No hay jugadores para editar.")
            return
        nombre = input("Ingrese el nombre del jugador que desea editar: ")
        for jugador in self.jugadores:
            if jugador.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del jugador: ")
                nuevo_nickname = input("Ingrese el nuevo nickname del jugador: ")
                jugador.nombre = nuevo_nombre
                jugador.nickname = nuevo_nickname
                print(f"El jugador {nombre} ha sido editado correctamente.")
                return
        print(f"No se encontró un jugador con el nombre {nombre}.")

    def eliminar_jugador(self):
        if not self.jugadores:
            print("No hay jugadores para eliminar.")
            return
        nombre = input("Ingrese el nombre del jugador que desea eliminar: ")
        for jugador in self.jugadores:
            if jugador.nombre == nombre:
                self.jugadores.remove(jugador)
                print(f"El jugador {nombre} ha sido eliminado correctamente.")
                return
        print(f"No se encontró un jugador con el nombre {nombre}.")

    def salir_del_juego(self):
        self.juego_terminado = True

    def mostrar_menu(self):
        print("\n--- BattleShip ---")
        print(" ")
        print("1. Empezar juego")
        print("2. Agregar jugador")
        print("3. Editar jugador")
        print("4. Eliminar jugador")
        print("5. Mostrar lista de jugadores")
        print("6. Salir del juego")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            print('\033[2J') # Código ANSI para limpiar la pantalla en sistemas Windows
            self.empezar_juego()
        elif opcion == 2:
            print('\033[2J') # Código ANSI para limpiar la pantalla en sistemas Windows
            self.agregar_jugador()
        elif opcion == 3:
            print('\033[2J') # Código ANSI para limpiar la pantalla en sistemas Windows
            self.editar_jugador()
        elif opcion == 4:
            print('\033[2J') # Código ANSI para limpiar la pantalla en sistemas Windows
            self.eliminar_jugador()
        elif opcion == 5:
            print('\033[2J') # Código ANSI para limpiar la pantalla en sistemas Windows
            self.mostrar_lista_jugadores()
        elif opcion == 6:
            print('\033[2J') # Código ANSI para limpiar la pantalla en sistemas Windows
            print("Saliendo del Juego......")
            self.salir_del_juego()
        else:
            print("Opción no válida.....presione enter para continuar")

    def jugar(self):
        while not self.juego_terminado:
            self.mostrar_menu()
            opcion = int(input("Seleccione una opcion: "))
            self.ejecutar_opcion(opcion)

# Instanciamos y ejecutamos el juego
juego = JuegoBatallaNaval()
juego.jugar()
