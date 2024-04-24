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
lstAciertos=[]

def bloquearVetana(vtn):
    vtn.attributes("-disabled", True)

def desBloquearVentana(vtn):
    vtn.attributes("-disabled", False)

def cargarDatos(vtnMenu):
    bloquearVetana(vtnMenu)
    vtnReanudar=reanudar.reanudarPartida(vtnMenu,matrizGuardar,matrizGuardar2,lstJugadores,lstAciertos)
    vtnMenu.wait_window(vtnReanudar)
    desBloquearVentana(vtnMenu)
    vtnMenu.focus_force()
    juego.empezarJuego(vtnMenu,lstJugadores,matrizBotones,matrizImagenes,matrizBotones2,matrizImagenes2,matrizGuardar,matrizGuardar2,lstAciertos)

def iniciarPartida(vtnMenu):
    bloquearVetana(vtnMenu)
    vntjugador=jugador.obternerNombres(vtnMenu,lstJugadores)
    vtnMenu.wait_window(vntjugador)
    vtnMatriz=crearMatriz.obtenerTamano(vtnMenu,matriz)
    vtnMenu.wait_window(vtnMatriz)
    desBloquearVentana(vtnMenu)
    vtnMenu.focus_force()
    juego.crearObjetos(vtnMenu,matriz,lstJugadores,matrizBotones,matrizBotones2,matrizImagenes,matrizImagenes2,matrizGuardar,matrizGuardar2)


def main():
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