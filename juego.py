from tkinter import *
import guardar
from PIL import Image,ImageTk

def apagarBotones(mtrBotones):
    for e in mtrBotones:
        for i in e:
            i

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

def configurarBoton(matriz,bnt,x,y):
    # if matriz[x][y]==1:
    # elif matriz[x][y]==1:
    pass

def orientacionSeleccionada(btnOrientacion):
    global orientacion
    if orientacion==0:
        orientacion+=1
        btnOrientacion.configure(text="^")
    elif orientacion==1:
        orientacion+=1
        btnOrientacion.configure(text="<")
    elif orientacion==2:
        orientacion+=1
        btnOrientacion.configure(text="v")
    elif orientacion==3:
        orientacion=0
        btnOrientacion.configure(text=">")

def rotarImagen(imagen):
    global barco,orientacion
    imagenRotada=imagen.rotate(orientacion*90)
    imagen=ImageTk.PhotoImage(imagenRotada)
    return imagen


def colocarBarcos(x, y, mtrBotones,filas,columnas,matriz):
    global barco,orientacion,imgAcorazado3,imgAcorazado2,imgAcorazado
    global imgCrusero,imgCrusero2,imgDestructor,barco1,barco2,barco3
    if orientacion==0:
        if barco==1 and barco1<6:
            img=rotarImagen(imgDestructor)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x][y].image=img
            barco1+=1
        elif barco == 2 and y < columnas-1 and barco2<4:
            img=rotarImagen(imgCrusero2)
            img2=rotarImagen(imgCrusero)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x][y+1].config(image=img2)
            mtrBotones[x][y].image=img
            mtrBotones[x][y+1].image=img2
            barco2+=1
        elif barco == 3 and y < columnas-2 and barco3<2:
            img=rotarImagen(imgAcorazado3)
            img2=rotarImagen(imgAcorazado2)
            img3=rotarImagen(imgAcorazado)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x][y+1].config(image=img2)
            mtrBotones[x][y+2].config(image=img3)
            mtrBotones[x][y].image=img
            mtrBotones[x][y+1].image=img2
            mtrBotones[x][y+2].image=img3
            barco3+=1

    elif orientacion==1:
        if barco==1 and barco1<6:
            img=rotarImagen(imgDestructor)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x][y].image=img
            barco1+=1
        elif barco == 2 and x>0 and barco2<4:
            img=rotarImagen(imgCrusero)
            img2=rotarImagen(imgCrusero2)
            mtrBotones[x-1][y].config(image=img)
            mtrBotones[x][y].config(image=img2)
            mtrBotones[x-1][y].image=img
            mtrBotones[x][y].image=img2
            barco2+=1
            
        elif barco == 3 and x>1 and barco3<2:
            img=rotarImagen(imgAcorazado3)
            img2=rotarImagen(imgAcorazado2)
            img3=rotarImagen(imgAcorazado)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x-1][y].config(image=img2)
            mtrBotones[x-2][y].config(image=img3)
            mtrBotones[x][y].image=img
            mtrBotones[x-1][y].image=img2
            mtrBotones[x-2][y].image=img3
            barco3+=1

    elif orientacion==2:
        if barco==1 and barco1<6:
            img=rotarImagen(imgDestructor)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x][y].image=img
            barco1+=1
        elif barco == 2 and y > 0 and barco2<4:
            img=rotarImagen(imgCrusero2)
            img2=rotarImagen(imgCrusero)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x][y-1].config(image=img2)
            mtrBotones[x][y].image=img
            mtrBotones[x][y-1].image=img2
            barco2+=1
        elif barco == 3 and y > 1 and barco3<2:
            img=rotarImagen(imgAcorazado3)
            img2=rotarImagen(imgAcorazado2)
            img3=rotarImagen(imgAcorazado)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x][y-1].config(image=img2)
            mtrBotones[x][y-2].config(image=img3)
            mtrBotones[x][y].image=img
            mtrBotones[x][y-1].image=img2
            mtrBotones[x][y-2].image=img3
            barco3+=1


    elif orientacion==3:
        if barco==1 and barco1<6:
            img=rotarImagen(imgDestructor)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x][y].image=img
            barco1+=1
        elif barco == 2 and x < filas-1 and barco2<4:
            img=rotarImagen(imgCrusero2)
            img2=rotarImagen(imgCrusero)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x+1][y].config(image=img2)
            mtrBotones[x][y].image=img
            mtrBotones[x+1][y].image=img2
            barco2+=1
        elif barco == 3 and x < filas-2 and barco3<2:
            img=rotarImagen(imgAcorazado3)
            img2=rotarImagen(imgAcorazado2)
            img3=rotarImagen(imgAcorazado)
            mtrBotones[x][y].config(image=img)
            mtrBotones[x+1][y].config(image=img2)
            mtrBotones[x+2][y].config(image=img3)
            mtrBotones[x][y].image=img
            mtrBotones[x+1][y].image=img2
            mtrBotones[x+2][y].image=img3
            barco3+=1



def matrizGrafica(matriz,mtrBotones,frame,filas,columnas):
    for e in range(filas):
        for i in range(columnas):
            button = Button(frame, text="", width=4, height=2)
            button.grid(row=e, column=i,sticky="nsew")
            mtrBotones[e][i]=button
            button.config(command=lambda e=e, i=i: colocarBarcos(e, i, mtrBotones,filas,columnas,matriz))

    

def crearObjetos(vMenu,matriz,lstJugadores,mtrBotones,mtrBotones2):
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

    btnOrientacion=Button(vMenu,text=">",font=("Arial", 12),command=lambda:orientacionSeleccionada(btnOrientacion))
    btnOrientacion.place(x=920, y=600)


    f=len(matriz)
    c=len(matriz[0])//2
    mtrBotones=[[None for _ in range(c)] for _ in range(f)]
    mtrBotones2=[[None for _ in range(c)] for _ in range(f)]
    matrizGrafica(matriz,mtrBotones,frameJugador1,f,c)
    matrizGrafica(matriz,mtrBotones2,frameJugador2,f,c)
    for e in mtrBotones:
        print(e)


imgDestructor=Image.open("img/b1.png")
imgDestructor=imgDestructor.resize((40, 40))

imgCrusero=Image.open("img/b21.png")
imgCrusero=imgCrusero.resize((40, 40))
imgCrusero2=Image.open("img/b22.png")
imgCrusero2=imgCrusero2.resize((40, 40))

imgAcorazado=Image.open("img/b31.png")
imgAcorazado=imgAcorazado.resize((40, 40))
imgAcorazado2=Image.open("img/b32.png")
imgAcorazado2=imgAcorazado2.resize((40, 40))
imgAcorazado3=Image.open("img/b33.png")
imgAcorazado3=imgAcorazado3.resize((40, 40))
                                   
fase=0
barco=1
barco1=0
barco2=0
barco3=0
orientacion=0