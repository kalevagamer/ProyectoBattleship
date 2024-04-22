from tkinter import *
from tkinter import messagebox

def escribirDatos(archivo,mtrz,lstJ):
    if archivo.strip()=="":
        messagebox.showerror("Error","No puedes guardar un archivo sin nombre")
    else:
        with open(archivo.strip(), "w") as file:
            file.write("%s\n" % lstJ)
            for e in mtrz:
                file.write("%s\n" % e)

def guardarPartida(matriz,lstJugadores):
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
    btnConfirmar=Button(ven,text="Confirmar",command=lambda:escribirDatos(ntrPartida.get(),matriz,lstJugadores))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)

    ven.mainloop()