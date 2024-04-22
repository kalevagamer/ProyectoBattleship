from tkinter import *
from tkinter import messagebox

def agregarJugadores(ven,lst,N1,N2,NN1,NN2):
    if N1.strip() and N2.strip() and NN1.strip() and NN2.strip():
        lst.append((N1,NN1))
        lst.append((N2,NN2))
        ven.destroy
    else:
        messagebox.showerror("Error","Alguna de las celdas esta vacia")


def ObternerNombres(lstJugadores):
    ven=Tk()
    ven.title("Battelship")
    ven.iconbitmap("img/bt.ico")
    ven.geometry("300x200")
    ven.configure(background="lightblue")
    ven.focus()
    #labels
    lblN1=Label(ven,text="Nombre Jugador 1",background="lightblue")
    lblNickN1=Label(ven,text="NickName jugador 1",background="lightblue")
    lblN2=Label(ven,text="Nombre Jugador 2",background="lightblue")
    lblNickN2=Label(ven,text="NickName jugador 2",background="lightblue")


    lblN1.place(x=60-lblN1.winfo_reqwidth()//2,y=10)
    lblNickN1.place(x=210-lblN1.winfo_reqwidth()//2,y=10)
    lblN2.place(x=60-lblN2.winfo_reqwidth()//2,y=70)
    lblNickN2.place(x=210-lblN1.winfo_reqwidth()//2,y=70)
    
    #entrys
    ntrN1=Entry(ven,background="lightblue")
    ntrNickN1=Entry(ven,background="lightblue")
    ntrN2=Entry(ven,background="lightblue")
    ntrNickN2=Entry(ven,background="lightblue")


    ntrN1.place(x=75-ntrN1.winfo_reqwidth()//2,y=30)
    ntrNickN1.place(x=225-ntrN1.winfo_reqwidth()//2,y=30)
    ntrN2.place(x=75-ntrN2.winfo_reqwidth()//2,y=90)
    ntrNickN2.place(x=225-ntrN1.winfo_reqwidth()//2,y=90)

    
    #botones
    btnConfirmar=Button(ven,text="Confirmar",command=lambda:agregarJugadores(ven,lstJugadores,ntrN1.get(),ntrN2.get()
                                                                             ,ntrNickN1.get(),ntrNickN2.get()))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)

    ven.mainloop()