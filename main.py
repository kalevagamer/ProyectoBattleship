from tkinter import *
from PIL import Image,ImageTk
import crearMatriz
import jugador
import juego
import reanudar

matriz=[]
lstJugadores=[]

def cargarDatos():
    reanudar.reanudarPartida(matriz,lstJugadores)
    
def iniciarPartida(vMenu):
    jugador.ObternerNombres(lstJugadores)
    crearMatriz.obtenerTamano(matriz)
    juego.matrizGrafica(matriz,lstJugadores)
    main()


def main():
    vMenu=Tk()
    vMenu.title("Battleship")
    vMenu.iconbitmap("img/bt.ico")
    vMenu.geometry("1300x700")
    vMenu.resizable(False,False)

    #lables
    img=Image.open("img/battle.jpeg")
    img= img.resize((1300,700))
    fondo=ImageTk.PhotoImage(img)
    lbl=Label(vMenu, image=fondo)
    lbl.place(x=-10,y=0)

    #botones
    btnNuevaPartida=Button(vMenu,text="Nueva Partida", command=lambda:iniciarPartida(vMenu))
    btnNuevaPartida.place(x=650-btnNuevaPartida.winfo_reqwidth()//2,y=350-btnNuevaPartida.winfo_reqheight()//2)

    btnReanudarPartida=Button(vMenu,text="Reanudar Partida",command=lambda:cargarDatos())
    btnReanudarPartida.place(x=650-btnReanudarPartida.winfo_reqwidth()//2,y=390-btnReanudarPartida.winfo_reqheight()//2)

    btnSalir=Button(vMenu,text="Salir",command=lambda:vMenu.destroy())
    btnSalir.place(x=650-btnSalir.winfo_reqwidth()//2,y=430-btnSalir.winfo_reqheight()//2)

    vMenu.mainloop()



main()
for e in matriz:
    print(e)
for e in lstJugadores:
    print(e)    