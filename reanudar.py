from tkinter import *
from tkinter import messagebox
import json
def leerDatos(archivo,mtrzImagenes,mtrzImagenes2,lstJugadores,lstAciertos):
    
    try:
        auxArchivo=f"{str(archivo).strip()}.txt"
        with open(auxArchivo, 'r') as f:
            mtrzImagenes=json.load(f)
        auxArchivo=f"saves/{str(archivo).strip()}-m2.txt" 
        with open(auxArchivo, 'r') as f:
            mtrzImagenes2=json.load(f)
        auxArchivo=f"saves/{str(archivo).strip()}-players.txt" 
        with open(auxArchivo, 'r') as f:
            lstJugadores=json.load(f)
        auxArchivo=f"saves/{str(archivo).strip()}-Ac.txt"
        with open(auxArchivo, 'r') as f:
            lstAciertos=json.load(f)
    except:
        messagebox.showerror("Error", "El archivo no existe o no se puede abrir.")

def reanudarPartida(matriz,lstJugadores):
    ven=Tk()
    ven.title("Battelship")
    ven.protocol("WM_DELETE_WINDOW", noCerrar)
    ven.iconbitmap("img/bt.ico")
    ven.geometry("300x200")
    ven.configure(background="lightblue")
    ven.focus()
    
    #labels
    lblpartida=Label(ven,text="Escriba el nombre de la partida",background="lightblue")
    
    lblpartida.place(x=150-lblpartida.winfo_reqwidth()//2,y=10)
    
    #entrys
    ntrPartida=Entry(ven,background="lightblue")
    ntrPartida.insert(0,"juego")
   
    ntrPartida.place(x=155-ntrPartida.winfo_reqwidth()//2,y=30)
    
    #botones
    btnConfirmar=Button(ven,text="Confirmar",command=lambda:leerDatos(ntrPartida.get(),matriz,lstJugadores))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)

def noCerrar():
    pass