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

    
