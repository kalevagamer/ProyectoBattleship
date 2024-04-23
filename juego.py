from tkinter import *
from tkinter import messagebox
import guardar
from PIL import Image,ImageTk

def apagarBotones(mtrBotones):
    for e in mtrBotones:
        for i in e:
            i.config(state="disabled",image='')

def encenderBotones(mtrBotones,mtrImagenes):
    x=0
    for e in mtrBotones:
        y=0
        for i in e:
            img=mtrImagenes[x][y]
            i.config(state="normal",image=img)
            y+=1
        x+=1

def limpiarVentana(ven):
    for e in ven.winfo_children():
        e.destroy()

def guardarP():
    pass

def empate():
    pass

def disparo(e, i, mtrBotones,mtrImagenes,filas,columnas,mtrOtrosBotones,mtrOtrasImagenes):
    print("hola")

def empezarJuego(vMenu,lstJugadores,mtrBotones,mtrImagenes,mtrBotones2,mtrImagenes2):
    global fase
    fase=2
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
    #Botones
    btnGuardar=Button(vMenu,text="Guardar Partida",font=("Arial", 12),command=lambda:guardarP())
    btnGuardar.place(x=320, y=600)

    btnEmpate=Button(vMenu,text="Declarar Empate",font=("Arial", 12),command=lambda:empate())
    btnEmpate.place(x=500, y=600)

    f=len(mtrImagenes)
    c=len(mtrImagenes[0])
    mtrBotones=matrizGrafica(mtrBotones,mtrImagenes,frameJugador1,f,c,mtrBotones2,mtrImagenes2,vMenu,lstJugadores)
    mtrBotones2=matrizGrafica(mtrBotones2,mtrImagenes2,frameJugador2,f,c,mtrBotones,mtrImagenes,vMenu,lstJugadores)
    mtrBotones=matrizGrafica(mtrBotones,mtrImagenes,frameJugador1,f,c,mtrBotones2,mtrImagenes2,vMenu,lstJugadores)
   

def barcoSeleccionado(n):
    global barco
    barco=n


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

def actualizarImagen(imagen,x,y,mtrImg):
    mtrImg[x][y]=imagen

def rotarImagen(imagen):
    global barco,orientacion
    imagenRotada=imagen.rotate(orientacion*90)
    imagen=ImageTk.PhotoImage(imagenRotada)
    return imagen


def colocarBarcos(x, y, mtrBtn,mtrImg,filas,columnas,mtrOtrosBtn,mtrOtrasImg,vtnMenu,lstJugadores):
    global barco,orientacion,imgAcorazado3,imgAcorazado2,imgAcorazado
    global imgCrusero,imgCrusero2,imgDestructor,barco1,barco2,barco3
    if orientacion==0:
        if barco==1 and barco1<6:
            if mtrBtn[x][y].cget('image')=='':
                img=rotarImagen(imgDestructor)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y].image=img
                barco1+=1
                actualizarImagen(img,x,y,mtrImg)
        elif barco == 2 and y < columnas-1 and barco2<4:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x][y+1].cget('image')=='':
                img=rotarImagen(imgCrusero2)
                img2=rotarImagen(imgCrusero)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y+1].config(image=img2)
                mtrBtn[x][y].image=img
                mtrBtn[x][y+1].image=img2
                barco2+=1
                actualizarImagen(img,x,y,mtrImg)
                actualizarImagen(img2,x,y+1,mtrImg)
        elif barco == 3 and y < columnas-2 and barco3<2:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x][y+1].cget('image')==''and mtrBtn[x][y+2].cget('image')=='':
                img=rotarImagen(imgAcorazado3)
                img2=rotarImagen(imgAcorazado2)
                img3=rotarImagen(imgAcorazado)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y+1].config(image=img2)
                mtrBtn[x][y+2].config(image=img3)
                mtrBtn[x][y].image=img
                mtrBtn[x][y+1].image=img2
                mtrBtn[x][y+2].image=img3
                barco3+=1
                actualizarImagen(img,x,y,mtrImg)
                actualizarImagen(img2,x,y+1,mtrImg)
                actualizarImagen(img3,x,y+2,mtrImg)
    elif orientacion==1:
        if barco==1 and barco1<6:
            if mtrBtn[x][y].cget('image')=='':
                img=rotarImagen(imgDestructor)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y].image=img
                barco1+=1
                actualizarImagen(img,x,y,mtrImg)
        elif barco == 2 and x>0 and barco2<4:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x-1][y].cget('image')=='':
                img=rotarImagen(imgCrusero)
                img2=rotarImagen(imgCrusero2)
                mtrBtn[x-1][y].config(image=img)
                mtrBtn[x][y].config(image=img2)
                mtrBtn[x-1][y].image=img
                mtrBtn[x][y].image=img2
                barco2+=1
                actualizarImagen(img,x-1,y,mtrImg)
                actualizarImagen(img2,x,y,mtrImg)
            
        elif barco == 3 and x>1 and barco3<2:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x-1][y].cget('image')==''and mtrBtn[x-2][y].cget('image')=='':
                img=rotarImagen(imgAcorazado3)
                img2=rotarImagen(imgAcorazado2)
                img3=rotarImagen(imgAcorazado)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x-1][y].config(image=img2)
                mtrBtn[x-2][y].config(image=img3)
                mtrBtn[x][y].image=img
                mtrBtn[x-1][y].image=img2
                mtrBtn[x-2][y].image=img3
                barco3+=1
                actualizarImagen(img,x,y,mtrImg)
                actualizarImagen(img2,x-1,y,mtrImg)
                actualizarImagen(img3,x-2,y,mtrImg)

    elif orientacion==2:
        if barco==1 and barco1<6:
            if mtrBtn[x][y].cget('image')=='':
                img=rotarImagen(imgDestructor)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y].image=img
                barco1+=1
                actualizarImagen(img,x,y,mtrImg)
        elif barco == 2 and y > 0 and barco2<4:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x][y-1].cget('image')=='':
                img=rotarImagen(imgCrusero2)
                img2=rotarImagen(imgCrusero)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y-1].config(image=img2)
                mtrBtn[x][y].image=img
                mtrBtn[x][y-1].image=img2
                barco2+=1
                actualizarImagen(img,x,y,mtrImg)
                actualizarImagen(img2,x,y-1,mtrImg)
        elif barco == 3 and y > 1 and barco3<2:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x][y-1].cget('image')==''and mtrBtn[x][y-2].cget('image')=='':
                img=rotarImagen(imgAcorazado3)
                img2=rotarImagen(imgAcorazado2)
                img3=rotarImagen(imgAcorazado)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y-1].config(image=img2)
                mtrBtn[x][y-2].config(image=img3)
                mtrBtn[x][y].image=img
                mtrBtn[x][y-1].image=img2
                mtrBtn[x][y-2].image=img3
                barco3+=1
                actualizarImagen(img,x,y,mtrImg)
                actualizarImagen(img2,x,y-1,mtrImg)
                actualizarImagen(img3,x,y-2,mtrImg)


    elif orientacion==3:
        if barco==1 and barco1<6:
            if mtrBtn[x][y].cget('image')=='':
                img=rotarImagen(imgDestructor)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y].image=img
                barco1+=1
                actualizarImagen(img,x,y,mtrImg)
        elif barco == 2 and x < filas-1 and barco2<4:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x+1][y].cget('image')=='':
                img=rotarImagen(imgCrusero2)
                img2=rotarImagen(imgCrusero)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x+1][y].config(image=img2)
                mtrBtn[x][y].image=img
                mtrBtn[x+1][y].image=img2
                barco2+=1
                actualizarImagen(img,x,y,mtrImg)
                actualizarImagen(img2,x+1,y,mtrImg)
        elif barco == 3 and x < filas-2 and barco3<2:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x+1][y].cget('image')==''and mtrBtn[x+2][y].cget('image')=='':
                img=rotarImagen(imgAcorazado3)
                img2=rotarImagen(imgAcorazado2)
                img3=rotarImagen(imgAcorazado)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x+1][y].config(image=img2)
                mtrBtn[x+2][y].config(image=img3)
                mtrBtn[x][y].image=img
                mtrBtn[x+1][y].image=img2
                mtrBtn[x+2][y].image=img3
                barco3+=1
                actualizarImagen(img,x,y,mtrImg)
                actualizarImagen(img2,x+1,y,mtrImg)
                actualizarImagen(img3,x+2,y,mtrImg)

    if barco1+barco2+barco3==12:
        global fase
        if fase==0:
            
            barco=1
            apagarBotones(mtrBtn)
            messagebox.showinfo("Jugador 1","Ya no te quedan más barcos")
            barco1=0
            barco2=0
            barco3=0
            messagebox.showinfo("Jugador 2","Tu turno de colocar, recuerda que tienes 6 Destructores, 4 Cruceros y 2 Acorazados")
            
            encenderBotones(mtrOtrosBtn,mtrOtrasImg)
        elif fase==1:
            apagarBotones(mtrBtn)
            encenderBotones(mtrOtrosBtn,mtrOtrasImg)
            empezarJuego(vtnMenu,lstJugadores,mtrOtrosBtn,mtrOtrasImg,mtrBtn,mtrImg)
        fase+=1
    


def matrizGrafica(mtrBtn,mtrImagenes,frame,filas,columnas,mtrOtrosBotones,mtrOtrasImagenes,vtnMenu,lstJugadores):
    mtrBtn=[[None for _ in range(columnas)] for _ in range(filas)]
    for e in range(filas):
        for i in range(columnas):
            button = Button(frame, text="", width=4, height=2)
            button.grid(row=e, column=i,sticky="nsew")
            mtrBtn[e][i]=button
            if fase==0:
                button.config(command=lambda e=e, i=i: colocarBarcos(e, i, mtrBtn,mtrImagenes,filas,
                                                                 columnas,mtrOtrosBotones,mtrOtrasImagenes,vtnMenu,lstJugadores))
            elif fase==2:
                button.config(image=mtrImagenes[e][i],command=lambda e=e, i=i:disparo(e, i, mtrBtn,mtrImagenes,filas,
                                                                 columnas,mtrOtrosBotones,mtrOtrasImagenes))
    return mtrBtn
    

def crearObjetos(vMenu,matriz,lstJugadores,mtrBotones,mtrBotones2,mtrImagenes,mtrImagenes2):
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
    mtrImagenes=[[None for _ in range(c)] for _ in range(f)]
    mtrImagenes2=[[None for _ in range(c)] for _ in range(f)]
    mtrBotones=matrizGrafica(mtrBotones,mtrImagenes,frameJugador1,f,c,mtrBotones2,mtrImagenes2,vMenu,lstJugadores)
    mtrBotones2=matrizGrafica(mtrBotones2,mtrImagenes2,frameJugador2,f,c,mtrBotones,mtrImagenes,vMenu,lstJugadores)
    mtrBotones=matrizGrafica(mtrBotones,mtrImagenes,frameJugador1,f,c,mtrBotones2,mtrImagenes2,vMenu,lstJugadores)
    messagebox.showinfo("Jugador 1","Coloca tus barcos, recuerda que tienes 6 Destructores, 4 Cruceros y 2 Acorazados")
    apagarBotones(mtrBotones2)
    



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