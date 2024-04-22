from tkinter import *
from tkinter import messagebox

def escribirDatos(archivo,mtrz,lstJ):
    archivo=f"{str(archivo).strip()}.txt"
    lstJStr=[]
    mtrzStr=[]
    if archivo=="":
        messagebox.showerror("Error","No puedes guardar un archivo sin nombre")
    else:
        for e in lstJ:
            lstJStr.append(str(e)+"\n")
        for e in mtrz:
            mtrzStr.append(str(e)+"\n")
        with open(archivo, "w") as file:
            file.writelines(lstJStr)
            file.writelines(mtrzStr)
        messagebox.showinfo("Guardado","La partida se ha guardado satisfactoriamente")
            
def guardarPartida(vMenu,matriz,lstJugadores):
    ven=Toplevel(vMenu)
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
    ntrPartida.insert(0,"archivo")
   
    ntrPartida.place(x=155-ntrPartida.winfo_reqwidth()//2,y=30)

    
    #botones
    btnConfirmar=Button(ven,text="Confirmar",command=lambda:escribirDatos(ntrPartida.get(),matriz,lstJugadores))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)
