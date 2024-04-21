from tkinter import *

def validarNumeros(n):
    return (n%2==0,isinstance(n, int))



def crearMatriz(largo=10,ancho=10):
    mtz=[]
    anchoMatriz=[]
    for i in range(0,ancho*2):
        anchoMatriz.append(0)
    for e in range(0,largo):
        mtz.append(anchoMatriz)
    return mtz


def tamaño():
    ven=Tk()
    ven.title("Battelship")
    ven.iconbitmap("img/bt.ico")
    ven.geometry("300x200")
    ven.configure(background="lightblue")

    #labels
    lblAncho=Label(ven,text="Numero de Filas (min 10)",background="lightblue")
    lblLargo=Label(ven,text="Numero de columnas (min 10)",background="lightblue")
    
    lblAncho.place(x=150-lblAncho.winfo_reqwidth()//2,y=10)
    lblLargo.place(x=150-lblAncho.winfo_reqwidth()//2,y=70)
    
    #botones
    btnConfirmar=Button(ven,text="Confirmar")

    #entrys
    ntrAncho=Entry(ven,background="lightblue")
    ntrLargo=Entry(ven,background="lightblue")

    ntrAncho.place(x=155-lblAncho.winfo_reqwidth()//2,y=30)
    ntrLargo.place(x=155-lblAncho.winfo_reqwidth()//2,y=90)


    ven.mainloop()

tamaño()
