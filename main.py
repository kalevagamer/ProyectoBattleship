from tkinter import *
from PIL import Image,ImageTk
import crearMatriz
import jugador
import juego
import reanudar

matriz=[]
lstJugadores=[]

def bloquearVetana(vtn):
    vtn.attributes("-disabled", True)

def desBloquearVentana(vtn):
    vtn.attributes("-disabled", False)

def cargarDatos(vtnMenu):
    reanudar.reanudarPartida(vtnMenu,matriz,lstJugadores)

def iniciarPartida(vtnMenu):
    bloquearVetana(vtnMenu)
    vntjugador=jugador.obternerNombres(vtnMenu,lstJugadores)
    vtnMenu.wait_window(vntjugador)
    vtnMatriz=crearMatriz.obtenerTamano(vtnMenu,matriz)
    vtnMenu.wait_window(vtnMatriz)
    desBloquearVentana(vtnMenu)
    vtnMenu.focus_force()
    juego.matrizGrafica(vtnMenu,matriz,lstJugadores)


def main():
    vtnMenu=Tk()
    vtnMenu.title("Battleship")
    vtnMenu.iconbitmap("img/bt.ico")
    vtnMenu.geometry("1300x800")
    vtnMenu.resizable(False,False)

    #lables
    img=Image.open("img/battle.jpeg")
    img= img.resize((1302,800))
    fondo=ImageTk.PhotoImage(img)
    lbl=Label(vtnMenu, image=fondo)
    lbl.place(x=-10,y=0)

    #botones
    btnNuevaPartida=Button(vtnMenu,text="Nueva Partida", command=lambda:iniciarPartida(vtnMenu))
    btnNuevaPartida.place(x=650-btnNuevaPartida.winfo_reqwidth()//2,y=350-btnNuevaPartida.winfo_reqheight()//2)

    btnReanudarPartida=Button(vtnMenu,text="Reanudar Partida",command=lambda:cargarDatos(vtnMenu))
    btnReanudarPartida.place(x=650-btnReanudarPartida.winfo_reqwidth()//2,y=390-btnReanudarPartida.winfo_reqheight()//2)

    btnSalir=Button(vtnMenu,text="Salir",command=lambda:vtnMenu.destroy())
    btnSalir.place(x=650-btnSalir.winfo_reqwidth()//2,y=430-btnSalir.winfo_reqheight()//2)

    vtnMenu.mainloop()



main()
for e in matriz:
    print(e)
for e in lstJugadores:
    print(e)    