from tkinter import *
from PIL import Image,ImageTk
import crearMatriz
import jugador
import juego
import reanudar

matriz=[]
matrizBotones=[]
matrizBotones2=[0]
matrizImagenes=[]
matrizImagenes2=[]
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
    juego.crearObjetos(vtnMenu,matriz,lstJugadores,matrizBotones,matrizBotones2,matrizImagenes,matrizImagenes2)


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
for e in matrizImagenes:
    print(e)
print() 
for e in matrizImagenes2:
    print(e)  