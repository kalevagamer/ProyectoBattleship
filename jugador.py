from tkinter import *
from tkinter import messagebox
import crearMatriz

def agregarJugadores(ven,lst,N1,N2,NN1,NN2):
    if N1.strip() and N2.strip() and NN1.strip() and NN2.strip():
        lst.append([N1,NN1,0])
        lst.append([N2,NN2,0])
        ven.destroy()
    else:
        messagebox.showerror("Error","Alguna de las celdas esta vacia")
        ven.focus_force()

def noCerrar():
    pass

def obternerNombres(vtnMenu,lstJugadores):
    vent=Toplevel(vtnMenu)
    vent.protocol("WM_DELETE_WINDOW", noCerrar)
    vent.title("Battelship")
    vent.iconbitmap("img/bt.ico")
    vent.geometry("300x200")
    vent.configure(background="lightblue")
    
    vent.focus()
    #labels
    lblN1=Label(vent,text="Nombre Jugador 1",background="lightblue")
    lblNickN1=Label(vent,text="NickName jugador 1",background="lightblue")
    lblN2=Label(vent,text="Nombre Jugador 2",background="lightblue")
    lblNickN2=Label(vent,text="NickName jugador 2",background="lightblue")


    lblN1.place(x=60-lblN1.winfo_reqwidth()//2,y=10)
    lblNickN1.place(x=210-lblN1.winfo_reqwidth()//2,y=10)
    lblN2.place(x=60-lblN2.winfo_reqwidth()//2,y=70)
    lblNickN2.place(x=210-lblN1.winfo_reqwidth()//2,y=70)
    
    #entrys
    ntrN1=Entry(vent,background="lightblue")
    ntrNickN1=Entry(vent,background="lightblue")
    ntrN2=Entry(vent,background="lightblue")
    ntrNickN2=Entry(vent,background="lightblue")


    ntrN1.place(x=75-ntrN1.winfo_reqwidth()//2,y=30)
    ntrNickN1.place(x=225-ntrN1.winfo_reqwidth()//2,y=30)
    ntrN2.place(x=75-ntrN2.winfo_reqwidth()//2,y=90)
    ntrNickN2.place(x=225-ntrN1.winfo_reqwidth()//2,y=90)

    
    #botones
    btnConfirmar=Button(vent,text="Confirmar",command=lambda:agregarJugadores(vent,lstJugadores,ntrN1.get(),ntrN2.get()
                                                                             ,ntrNickN1.get(),ntrNickN2.get()))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)

    return vent


