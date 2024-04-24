from tkinter import *
from tkinter import messagebox

def validarNumeros(n,ven):
    """
    Valida si el número ingresado 'n' es un entero mayor o igual a 10.

    Args:
        n (str): Cadena que representa el número a validar.
        ven (Tk): Ventana donde se mostrarán los mensajes de error en caso de falla.

    Returns:
        bool: True si 'n' es un entero mayor o igual a 10, False de lo contrario.
    """
    try:
        n=int(n)
        if n>=10:
            if n%1==0:
                return True
            else:
                messagebox.showerror("Error",f"{n} no es entero")
                ven.focus()
                return False
        messagebox.showwarning("Alerta",f"{n} a sido cambiado por el minimo (10)")
    except: 
        messagebox.showerror("Error",f"{n} No es un numero")
        ven.focus()
        return False 


def crearMatriz(largo,ancho,mtrz):
    """
    Crea una matriz de dimensiones 'largo' x 'ancho' inicializada con ceros.

    Args:
        largo (str): Cadena que representa el número de filas de la matriz.
        ancho (str): Cadena que representa el número de columnas de la matriz.
        mtrz (list): Lista donde se almacenará la matriz creada.

    """
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
    """
    Procesa las dimensiones ingresadas y crea la matriz si son válidas.

    Args:
        largo (str): Cadena que representa el número de filas deseado.
        ancho (str): Cadena que representa el número de columnas deseado.
        mtrz (list): Lista donde se almacenará la matriz creada.
        ven (Tk): Ventana donde se mostrarán los mensajes de error en caso de falla.

    """
    if validarNumeros(largo,ven):
        if validarNumeros(ancho,ven):
            crearMatriz(largo,ancho,mtrz)
            ven.destroy()

def noCerrar():
    pass

def obtenerTamano(vtnMenu,mtrz):
    """
    Crea una ventana secundaria para obtener las dimensiones deseadas de la matriz.

    Args:
        vtnMenu (Tk): Ventana principal desde la cual se crea la ventana secundaria.
        mtrz (list): Lista donde se almacenará la matriz creada.

    Returns:
        Toplevel: Ventana secundaria donde se pueden ingresar las dimensiones.
    """
    ven=Toplevel(vtnMenu)
    ven.protocol("WM_DELETE_WINDOW", noCerrar)
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

    return ven





