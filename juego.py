from tkinter import *
import guardar
from PIL import Image,ImageTk

def comprobarIzquierda():
    pass

def comprobarDerecha():
    pass

def comprobarArriba():
    pass

def comprobarAbajo():
    pass

def limpiarVentana(ven):
    for e in ven.winfo_children():
        e.destroy()


def empezarJuego(vMenu):
    #Botones
    btnGuardar=Button(vMenu,text="Guardar Partida",font=("Arial", 12))
    btnGuardar.place(x=220, y=600)

    btnEmpate=Button(vMenu,text="Declarar Empate",font=("Arial", 12))
    btnEmpate.place(x=470, y=600)

    btnRevelar=Button(vMenu,text="Revelar Barcos",font=("Arial", 12))
    btnRevelar.place(x=720, y=600)

def barcoSeleccionado(n):
    global barco
    barco=n

def horientacionSeleccionada(btnHorientacion):
    global horientacion
    if horientacion==0:
        horientacion+=1
        btnHorientacion.configure(text="v")
    elif horientacion==1:
        horientacion+=1
        btnHorientacion.configure(text="<")
    elif horientacion==2:
        horientacion+=1
        btnHorientacion.configure(text="^")
    elif horientacion==3:
        horientacion=0
        btnHorientacion.configure(text=">")

def rotarImagen(imagen):
    global barco,horientacion
    imagen=imagen.rotate(horientacion*90)

    

def colocarBarcos(x, y, mtrBotones,filas,columnas):
    global barco,horientacion,imgAcorazado3,imgAcorazado2,imgAcorazado
    global imgCrusero,imgCrusero2,imgDestructor,barco1,barco2,barco3
    if horientacion==0:
        if barco==1 and barco1<6:
            mtrBotones[x][y].config(image=rotarImagen(imgDestructor))
            barco1+=1
        elif barco == 2 and y < columnas-1 and barco2<4:
            mtrBotones[x][y].config(image=rotarImagen(imgCrusero))
            mtrBotones[x][y+1].config(image=rotarImagen(imgCrusero2))
            barco2+=1
        elif barco == 3 and y < columnas-2 and barco3<2:
            mtrBotones[x][y].config(image=rotarImagen(imgAcorazado))
            mtrBotones[x][y+1].config(image=rotarImagen(imgAcorazado2))
            mtrBotones[x][y+2].config(image=rotarImagen(imgAcorazado3))
            barco3+=1


    elif horientacion==1:
        if barco==1 and barco1<6:
            mtrBotones[x][y].config(image=rotarImagen(imgDestructor))
            barco1+=1
        elif barco == 2 and y < 9 and barco2<4:
            mtrBotones[x][y].config(image=rotarImagen(imgCrusero))
            mtrBotones[x+1][y].config(image=rotarImagen(imgCrusero2))
            barco2+=1
        elif barco == 3 and y < 8 and barco3<2:
            mtrBotones[x][y].config(image=rotarImagen(imgAcorazado))
            mtrBotones[x][y+1].config(image=rotarImagen(imgAcorazado2))
            mtrBotones[x][y+2].config(image=rotarImagen(imgAcorazado3))
            barco3+=1


    elif horientacion==2:
        if barco==1 and barco1<6:
            mtrBotones[x][y].config(image=rotarImagen(imgDestructor))
            barco1+=1
        elif barco == 2 and y < 9 and barco2<4:
            mtrBotones[x][y].config(image=rotarImagen(imgCrusero))
            mtrBotones[x][y+1].config(image=rotarImagen(imgCrusero2))
            barco2+=1
        elif barco == 3 and y < 8 and barco3<2:
            mtrBotones[x][y].config(image=rotarImagen(imgAcorazado))
            mtrBotones[x][y+1].config(image=rotarImagen(imgAcorazado2))
            mtrBotones[x][y+2].config(image=rotarImagen(imgAcorazado3))
            barco3+=1


    elif horientacion==3:
        if barco==1 and barco1<6:
            mtrBotones[x][y].config(image=rotarImagen(imgDestructor))
            barco1+=1
        elif barco == 2 and y < 9 and barco2<4:
            mtrBotones[x][y].config(image=rotarImagen(imgCrusero))
            mtrBotones[x][y+1].config(image=rotarImagen(imgCrusero2))
            barco2+=1
        elif barco == 3 and y < 8 and barco3<2:
            mtrBotones[x][y].config(image=rotarImagen(imgAcorazado))
            mtrBotones[x][y+1].config(image=rotarImagen(imgAcorazado2))
            mtrBotones[x][y+2].config(image=rotarImagen(imgAcorazado3))
            barco3+=1



def matrizGrafica(mtrBotones,frame,filas,columnas):
    mtrBotones=[[None for _ in range(filas)] for _ in range(columnas)]
    for e in range(filas):
            for i in range(columnas):
                button = Button(frame, text="", width=4, height=2)
                button.grid(row=e, column=i, sticky="nsew")
                button.config(command=lambda e=e, i=i: colocarBarcos(e, i, mtrBotones,filas,columnas))
                mtrBotones[e][i]=button

def crearObjetos(vMenu,matriz,lstJugadores,mtrBotones):
    limpiarVentana(vMenu)
    #labels
    lblJugador1=Label(vMenu,text=f"Jugador 1: {lstJugadores[0][0]}",font=("Arial", 16))
    lblJugador1.place(x=60,y=20)

    lblPuntaje1=Label(vMenu,text=f"Puntuación: {lstJugadores[0][2]}",font=("Arial", 16))
    lblPuntaje1.place(x=60,y=60)

    lblJugador2=Label(vMenu,text=f"Jugador 2: {lstJugadores[1][0]}",font=("Arial", 16))
    lblJugador2.place(x=670,y=20)

    lblPuntaje2=Label(vMenu,text=f"Puntuación: {lstJugadores[1][2]}",font=("Arial", 16))
    lblPuntaje2.place(x=670,y=60)

    #frames
    frameJugador1=Frame(vMenu,borderwidth=2,relief="solid",width=600,height=400)
    frameJugador1.place(x=50, y=140)

    frameJugador2=Frame(vMenu,borderwidth=2,relief="solid",width=600,height=400)
    frameJugador2.place(x=650, y=140)

    #botones
    btnDestructor=Button(vMenu,text="destructor",font=("Arial", 12),command=lambda:barcoSeleccionado(1))
    btnDestructor.place(x=220, y=600)

    btnCrucero=Button(vMenu,text="Crucero",font=("Arial", 12),command=lambda:barcoSeleccionado(2))
    btnCrucero.place(x=470, y=600)

    btnAcorazado=Button(vMenu,text="Acorazado",font=("Arial", 12),command=lambda:barcoSeleccionado(3))
    btnAcorazado.place(x=720, y=600)

    btnHorientacion=Button(vMenu,text=">",font=("Arial", 12),command=lambda:horientacionSeleccionada(btnHorientacion))
    btnHorientacion.place(x=920, y=600)


    f=len(matriz)
    c=len(matriz[0])//2
    matrizGrafica(mtrBotones,frameJugador1,f,c)
    matrizGrafica(mtrBotones,frameJugador2,f,c)


imgDestructor=Image.open("img/b1.png")
imgDestructor=imgDestructor.resize((4, 2))

imgCrusero=Image.open("img/b21.png")
imgCrusero=imgCrusero.resize((4, 2))
imgCrusero2=Image.open("img/b22.png")
imgCrusero2=imgCrusero2.resize((4, 2))

imgAcorazado=Image.open("img/b31.png")
imgAcorazado=imgAcorazado.resize((4, 2))
imgAcorazado2=Image.open("img/b32.png")
imgAcorazado2=imgAcorazado2.resize((4, 2))
imgAcorazado3=Image.open("img/b33.png")
imgAcorazado3=imgAcorazado3.resize((4, 2))
                                   
fase=0
barco=1
barco1=0
barco2=0
barco3=0
horientacion=1