from tkinter import *
from tkinter import messagebox
import json

def escribirDatos(ven,archivo,mtrzImg,mtrzImg2,lstJ,lstA):
    """
    Guarda los datos de la partida en archivos JSON.

    Args:
        ven (Tk): Ventana principal desde la cual se llama la función.
        archivo (str): Nombre del archivo donde se guardarán los datos de la partida.
        mtrzImg (list): Matriz de imágenes del jugador 1.
        mtrzImg2 (list): Matriz de imágenes del jugador 2.
        lstJ (list): Lista de jugadores.
        lstA (list): Lista de aciertos.

    """
    
    if archivo.strip()=="":
        
        messagebox.showerror("Error","No puedes guardar un archivo sin nombre")
    else:
        auxArchivo=f"saves/{str(archivo).strip()}.txt"
        with open(auxArchivo, 'w') as f:
            json.dump(mtrzImg, f)
        auxArchivo=f"saves/{str(archivo).strip()}-players.txt"
        with open(auxArchivo, 'w') as f:
            json.dump(lstJ, f)
        auxArchivo=f"saves/{str(archivo).strip()}-p2.txt"
        with open(auxArchivo, 'w') as f:
            json.dump(mtrzImg2, f)
        auxArchivo=f"saves/{str(archivo).strip()}-Ac.txt"
        with open(auxArchivo, 'w') as f:
            json.dump(lstA, f)
        messagebox.showinfo("Guardado","La partida se ha guardado satisfactoriamente")
        ven.destroy()
            
def guardarPartida(vMenu,lstJugadores,mtrImagenes,mtrImagenes2,lstAciertos):
    """
    Crea una ventana para que el usuario escriba el nombre de la partida y la guarde.

    Args:
        vMenu (Tk): Ventana principal desde la cual se crea la ventana secundaria.
        lstJugadores (list): Lista de jugadores.
        mtrImagenes (list): Matriz de imágenes del jugador 1.
        mtrImagenes2 (list): Matriz de imágenes del jugador 2.
        lstAciertos (list): Lista de aciertos.

    Returns:
        Toplevel: Ventana secundaria donde se puede ingresar el nombre de la partida.

    """
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
    btnConfirmar=Button(ven,text="Confirmar",command=lambda:escribirDatos(ven,ntrPartida.get(),mtrImagenes
                                                                        ,mtrImagenes2,lstJugadores,lstAciertos))
    btnConfirmar.place(x=155-btnConfirmar.winfo_reqwidth()//2,y=120)

    return ven
