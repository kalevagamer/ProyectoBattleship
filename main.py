from tkinter import *
from PIL import Image,ImageTk
import crearMatriz

matriz=[]
matrizBotones=[]

def iniciarPartida():
    crearMatriz.tamano(matriz)

def main():
    vMenu=Tk()
    vMenu.title("Battleship")
    vMenu.iconbitmap("img/bt.ico")
    vMenu.geometry("1300x700")

    #lables
    img=Image.open("img/battle.jpg")
    img= img.resize((1300,700))
    fondo=ImageTk.PhotoImage(img)
    lbl=Label(vMenu, image=fondo)
    lbl.place(x=-1,y=0)

    #botones
    btnNuevaPartida=Button(vMenu,text="Nueva Partida", command=lambda:iniciarPartida())
    btnNuevaPartida.place(x=650-btnNuevaPartida.winfo_reqwidth()//2,y=350-btnNuevaPartida.winfo_reqheight()//2)

    btnReanudarPartida=Button(vMenu,text="Reanudar Partida")
    btnReanudarPartida.place(x=650-btnReanudarPartida.winfo_reqwidth()//2,y=390-btnReanudarPartida.winfo_reqheight()//2)

    btnSalir=Button(vMenu,text="Salir",command=lambda:vMenu.destroy())
    btnSalir.place(x=650-btnSalir.winfo_reqwidth()//2,y=430-btnSalir.winfo_reqheight()//2)

    vMenu.mainloop()



main()
for e in matriz:
    print(e)    