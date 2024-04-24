from tkinter import *
from tkinter import messagebox
import json
def leerDatos(archivo,mtrzImagenes,mtrzImagenes2,lstJugadores,lstAciertos):
    """
         Lee los datos de una partida guardada desde varios archivos de texto y los carga en las listas correspondientes.

    Args:
    archivo : str
        Nombre base del archivo sin extensión, que se usará para generar los nombres de los archivos de datos.
    mtrzImagenes : list
        Lista para almacenar los datos de la primera matriz de imágenes.
    mtrzImagenes2 : list
        Lista para almacenar los datos de la segunda matriz de imágenes.
    lstJugadores : list
        Lista para almacenar los datos de los jugadores.
    lstAciertos : list
        Lista para almacenar los datos de los aciertos.

    Esta función intenta abrir y leer cuatro archivos distintos que contienen los datos necesarios
    para reanudar una partida. Si hay un problema al abrir los archivos, se muestra un mensaje de error.
    """
    
    try:
        auxArchivo=f"saves/{str(archivo).strip()}.txt"
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
    """
    Crea una ventana para que el usuario ingrese el nombre de la partida que desea reanudar.

    Args:
    matriz : list
        Matriz de juego que se actualizará con los datos leídos.
    lstJugadores : list
        Lista de jugadores que se actualizará con los datos leídos.

    La función configura una interfaz gráfica que incluye un campo de entrada y un botón de confirmación.
    Al presionar el botón de confirmación, se intentará cargar los datos de la partida especificada.
    """
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