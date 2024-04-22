from tkinter import *

def escribirDatos():
    pass

def guardarPartida(matriz,Ljugadores):
    ven=Tk()
    ven.title("Battelship")
    ven.iconbitmap("img/bt.ico")
    ven.geometry("300x200")
    ven.configure(background="lightblue")
    ven.focus()
    #labels
    lblAncho=Label(ven,text="Numero de Filas (min 10)",background="lightblue")
    lblLargo=Label(ven,text="Numero de columnas (min 10)",background="lightblue")
    
    lblAncho.place(x=150-lblAncho.winfo_reqwidth()//2,y=10)
    lblLargo.place(x=150-lblLargo.winfo_reqwidth()//2,y=70)
    
    #entrys
    ntrAncho=Entry(ven,background="lightblue")
    ntrAncho.insert(0,10)
    ntrLargo=Entry(ven,background="lightblue")
    ntrLargo.insert(0,10)


    ntrAncho.place(x=155-ntrAncho.winfo_reqwidth()//2,y=30)
    ntrLargo.place(x=155-ntrLargo.winfo_reqwidth()//2,y=90)

    
    #botones
    btnConfirmar=Button(ven,text="Confirmar",command=lambda:agregarJugadores(lstJugadores,ntrN1.get(),ntrN2.get()
                                                                             ,ntrNickN1.get(),ntrNickN2.get()))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)

    ven.mainloop()