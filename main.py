from tkinter import *
from PIL import Image,ImageTk
import crearMatriz
import jugador
import juego
import reanudar

matriz=[]
matrizBotones=[]
matrizBotones2=[]
matrizImagenes=[]
matrizImagenes2=[]
matrizGuardar=[]
matrizGuardar2=[]
lstJugadores=[]
lstAciertos=[[],[]]

def bloquearVetana(vtn):
    """
    Deshabilita temporalmente la interacción con una ventana de Tkinter.

    Args:
    vtn : Tkinter window object
        La ventana que será deshabilitada.
    """
    vtn.attributes("-disabled", True)

def desBloquearVentana(vtn):
    """
    Habilita la interacción con una ventana de Tkinter que fue previamente deshabilitada.

    Args:
    vtn : Tkinter window object
        La ventana que será habilitada.
    """
    vtn.attributes("-disabled", False)

def cargarDatos(vtnMenu):
    """
    Gestiona la carga y continuación de una partida guardada, bloqueando la ventana principal
    mientras la partida se reanuda y se inicia el juego nuevamente.

    Args:
    vtnMenu : Tkinter window object
        La ventana principal del menú desde la cual se lanza la partida.
    """
    bloquearVetana(vtnMenu)
    vtnReanudar=reanudar.reanudarPartida(vtnMenu,matrizImagenes,matrizImagenes2,lstJugadores,lstAciertos)
    vtnMenu.wait_window(vtnReanudar)
    desBloquearVentana(vtnMenu)
    vtnMenu.focus_force()
    juego.empezarJuego(vtnMenu,lstJugadores,matrizBotones,matrizImagenes,matrizBotones2,matrizImagenes2,matrizGuardar,matrizGuardar2,lstAciertos)

def iniciarPartida(vtnMenu):
    """
    Inicia una nueva partida, obteniendo primero los nombres de los jugadores y luego configurando la matriz del juego.
    La ventana principal se bloquea durante el proceso.

    Args:
    vtnMenu : Tkinter window object
        La ventana principal desde donde se inicia la nueva partida.
    """
    bloquearVetana(vtnMenu)
    vntjugador=jugador.obternerNombres(vtnMenu,lstJugadores)
    vtnMenu.wait_window(vntjugador)
    vtnMatriz=crearMatriz.obtenerTamano(vtnMenu,matriz)
    vtnMenu.wait_window(vtnMatriz)
    desBloquearVentana(vtnMenu)
    vtnMenu.focus_force()
    juego.crearObjetos(vtnMenu,matriz,lstJugadores,matrizBotones,matrizBotones2,matrizImagenes,matrizImagenes2,matrizGuardar,matrizGuardar2)


def main():
    """
    Configura y muestra la ventana principal del juego de Battleship, incluyendo configuración de imagen de fondo
    y botones para manejar el inicio de una nueva partida, reanudar una existente y salir del juego.
    """
    
    vtnMenu=Tk()
    vtnMenu.title("Battleship")
    vtnMenu.iconbitmap("img/bt.ico")
    vtnMenu.geometry("1100x650")
    vtnMenu.resizable(False,False)

    #lables
    img=Image.open("img/battle.jpeg")
    img= img.resize((1102,650))
    fondo=ImageTk.PhotoImage(img)
    lbl=Label(vtnMenu, image=fondo)
    lbl.place(x=-5,y=0)

    #botones
    btnNuevaPartida=Button(vtnMenu,text="Nueva Partida",font=("Arial", 12), command=lambda:iniciarPartida(vtnMenu))
    btnNuevaPartida.place(x=550-btnNuevaPartida.winfo_reqwidth()//2,y=350-btnNuevaPartida.winfo_reqheight()//2)

    btnReanudarPartida=Button(vtnMenu,text="Reanudar Partida",font=("Arial", 12),command=lambda:cargarDatos(vtnMenu))
    btnReanudarPartida.place(x=550-btnReanudarPartida.winfo_reqwidth()//2,y=390-btnReanudarPartida.winfo_reqheight()//2)

    btnSalir=Button(vtnMenu,text="Salir",font=("Arial", 12),command=lambda:vtnMenu.destroy())
    btnSalir.place(x=550-btnSalir.winfo_reqwidth()//2,y=430-btnSalir.winfo_reqheight()//2)

    vtnMenu.mainloop()



main()