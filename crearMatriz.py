from tkinter import *
from tkinter import messagebox

def validarNumeros(n):
    try:
        n=int(n)
        if n>=10:
            if n%1==0:
                return True
            else:
                messagebox.showerror("Error",f"{n} no es entero")
                return False
        messagebox.showwarning("Alerta",f"{n} a sido cambiado por el minimo (10)")
    except: 
        messagebox.showerror("Error",f"{n} No es un numero")
        return False 


def crearMatriz(largo,ancho,mtrz):
    if largo in range(0,10):
        largo=10
    if ancho in range(0,10):
        ancho=10
    anchoMatriz=[]
    largo=int(largo)
    ancho=int(ancho)
    for e in range(0,ancho*2):
        anchoMatriz.append(0)
    for e in range(0,largo):
        mtrz.append(anchoMatriz)

def proceso(largo,ancho,mtrz,ven):
    if validarNumeros(largo):
        if validarNumeros(ancho):
            crearMatriz(largo,ancho,mtrz)
            ven.destroy()
    

def obtenerTamano(mtrz):
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
    btnConfirmar=Button(ven,text="Confirmar",command=lambda:proceso(ntrAncho.get(),ntrLargo.get(),mtrz,ven))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)


    ven.mainloop()

