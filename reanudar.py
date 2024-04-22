from tkinter import *
from tkinter import messagebox
def leerDatos(archivo,matriz,lstJugadores):
    archivo=f"{str(archivo).strip()}.txt"
    try:
        cont=0
        with open(archivo, "r") as file:
            for line in file:
                lstJugadores.append(eval(line.strip()))
                cont+=1
                if cont==2:
                    break
            cont=0
            for line in file:
                if cont==2:
                    matriz.append(eval(line.strip()))
                cont+=1
    except:
        messagebox.showerror("Error", "El archivo no existe o no se puede abrir.")

def reanudarPartida(matriz,lstJugadores):
    ven=Tk()
    ven.title("Battelship")
    ven.iconbitmap("img/bt.ico")
    ven.geometry("300x200")
    ven.configure(background="lightblue")
    ven.focus()
    
    #labels
    lblpartida=Label(ven,text="Escriba el nombre de la partida",background="lightblue")
    
    lblpartida.place(x=150-lblpartida.winfo_reqwidth()//2,y=10)
    
    #entrys
    ntrPartida=Entry(ven,background="lightblue")
    ntrPartida.insert(0,10)
   
    ntrPartida.place(x=155-ntrPartida.winfo_reqwidth()//2,y=30)
    
    #botones
    btnConfirmar=Button(ven,text="Confirmar",command=lambda:leerDatos(ntrPartida.get(),matriz,lstJugadores))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)
