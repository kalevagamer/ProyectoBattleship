from tkinter import *
from tkinter import messagebox
import guardar
from PIL import Image,ImageTk

def apagarBotones(mtrBotones):
    """
    Deshabilita todos los botones en la matriz de botones.

    Args:
        mtrBotones (list): Una matriz de botones (matriz 2D).

    Returns:
        None
    """
    for e in mtrBotones:
        for i in e:
            i.config(state="disabled",image='')

def encenderBotones(mtrBotones):
    """
    Habilita todos los botones en la matriz de botones.

    Args:
        mtrBotones (list): Una matriz de botones (matriz 2D).

    Returns:
        None
    """
    x=0
    for e in mtrBotones:
        y=0
        for i in e:
            i.config(state="normal")
            y+=1
        x+=1

def limpiarVentana(ven):
    """
    Limpia todos los widgets dentro de una ventana.

    Args:
        ven (Tk): La ventana de Tkinter a limpiar.

    Returns:
        None
    """
    for e in ven.winfo_children():
        e.destroy()

    

def guardarP(vMenu,lstJugadores,mtrImagenes,mtrImagenes2,lstAciertos):
    """
    Maneja el proceso de guardado de partida.

    Args:
        vMenu (Tk): La ventana principal de la aplicación.
        lstJugadores (list): Lista de jugadores.
        mtrImagenes (list): Matriz de imágenes del jugador 1.
        mtrImagenes2 (list): Matriz de imágenes del jugador 2.
        lstAciertos (list): Lista de aciertos.
        lstTodasImagenes (list): Lista de rutas de imágenes.

    Returns:
        None
    """
    # mtrOrientacion=orientar(mtrImagenes,lstTodasImagenes)
    # mtrOrientacion2=orientar(mtrImagenes2,lstTodasImagenes)
    vMenu.attributes("-disabled", True)
    vntGuardar=guardar.guardarPartida(vMenu,lstJugadores,mtrImagenes,mtrImagenes2,lstAciertos)
    vMenu.wait_window(vntGuardar)
    vMenu.attributes("-disabled", False)


def moverBarcos(matrizGuardar,filas,columnas):
    """
    Mueve los barcos en la matriz en la dirección a donde apuntan, mientras no choque con nada
     y si un barco no se puede mover, se dara la vuelta.

    Args:
        matrizGuardar (list): Matriz del juego donde cada elemento puede ser None o una referencia a una imagen.
        filas (int): Número total de filas en la matriz.
        columnas (int): Número total de columnas en la matriz.
        direccion (str): Dirección del movimiento ('derecha', 'izquierda', 'arriba', 'abajo').

    Returns:
        None
    """
    derecha=[lstTodasImagenes[0],lstTodasImagenes[4],lstTodasImagenes[12]]
    arriba=[lstTodasImagenes[1],lstTodasImagenes[5],lstTodasImagenes[13]]
    izquierda=[lstTodasImagenes[2],lstTodasImagenes[6],lstTodasImagenes[14]]
    abajo=[lstTodasImagenes[3],lstTodasImagenes[7],lstTodasImagenes[15]]
    imgInicial=[lstTodasImagenes[0],lstTodasImagenes[4],lstTodasImagenes[12],
                lstTodasImagenes[1],lstTodasImagenes[5],lstTodasImagenes[13],
                lstTodasImagenes[2],lstTodasImagenes[6],lstTodasImagenes[14],
                lstTodasImagenes[3],lstTodasImagenes[7],lstTodasImagenes[15]]
    destructor=['img/b1.png','img/b1_rotated_90.png','img/b1_rotated_180.png','img/b1_rotated_270.png']
    crusero=[['img/b21.png','img/b21_rotated_90.png','img/b21_rotated_180.png','img/b21_rotated_270.png'],
            ['img/b22.png','img/b22_rotated_90.png','img/b22_rotated_180.png','img/b22_rotated_270.png']]
    acorazado=[['img/b31.png','img/b31_rotated_90.png','img/b31_rotated_180.png','img/b31_rotated_270.png'],
                ['img/b32.png','img/b32_rotated_90.png','img/b32_rotated_180.png','img/b32_rotated_270.png'],
                ['img/b33.png','img/b33_rotated_90.png','img/b33_rotated_180.png','img/b33_rotated_270.png']]
    for x in range(filas):
        for y in range(columnas):
            elementoActual = matrizGuardar[x][y]
            if elementoActual in imgInicial:
                dx, dy = 0, 0
                if elementoActual in derecha and y < columnas - 1:
                    dx, dy = 0, 1
                elif elementoActual in izquierda and y > 0:
                    dx, dy = 0, -1
                elif elementoActual in arriba and x > 0:
                    dx, dy = -1, 0
                elif elementoActual in abajo and x < filas - 1:
                    dx, dy = 1, 0

                nuevaX, nuevaY = x + dx, y + dy

                if 0 <= nuevaX < filas and 0 <= nuevaY < columnas and matrizGuardar[nuevaX][nuevaY] is None:
                    # Mover el elemento
                    matrizGuardar[nuevaX][nuevaY] = elementoActual
                    matrizGuardar[x][y] = None

    for x in range(filas):
        for y in range(columnas - 1, -1, -1):
            if matrizGuardar[x][y] is not None and ((matrizGuardar[x][y] in derecha and y == columnas - 1) or
                                                    (matrizGuardar[x][y] in izquierda and y == 0)):
                # Suponiendo que el barco tiene un tamaño fijo de 3 para este ejemplo
                if y + 2 < columnas and all(matrizGuardar[x][y + offset] is not None for offset in range(3)):
                    # Invertir las posiciones de las imágenes
                    matrizGuardar[x][y], matrizGuardar[x][y + 2] = matrizGuardar[x][y + 2], matrizGuardar[x][y]

def terminarPartida(vMenu,puntos):
    """
    Determina quien es el ganador o si la partida es un empate

    Args:
        vMenu (Tk): La ventana principal del juego que será cerrada al finalizar la partida.
        puntos (list): Lista de dos elementos, cada sublista tiene los atributos de cada jugador

    Returns:
        None: La función muestra cuadros de diálogo para interactuar con el usuario y no retorna ningún valor.

    """
    if fase==5:
        if len(puntos[0][2])==len(puntos[1][2]):
                messagebox.showinfo("Partida Terminada","se ha declarado empate")
        elif len(puntos[0][2])>len(puntos[1][2]):
            messagebox.showinfo("Partida Terminada","Gana Jugador 1!")
        elif len(puntos[0][2])<len(puntos[1][2]):
            messagebox.showinfo("Partida Terminada","Gana Jugador 1!")
        vMenu.destroy()
    elif fase==3:
        messagebox.showinfo("Terminar Partida","No se puede terminar la partida si Jugador 2 no ha terminado su turno")
    else:
        respuesta=messagebox.askyesno("Partida","¿desean terminar la partida?")
        if respuesta:
            if len(puntos[0][2])==len(puntos[1][2]):
                messagebox.showinfo("Partida Terminada","se ha declarado empate")
            elif len(puntos[0][2])>len(puntos[1][2]):
                messagebox.showinfo("Partida Terminada","Gana Jugador 1!")
            elif len(puntos[0][2])<len(puntos[1][2]):
                messagebox.showinfo("Partida Terminada","Gana Jugador 1!")
            vMenu.destroy()

def disparo(vtnMenu,x, y, mtrBotones,matrizGuardar,filas,columnas,aciertos,lstJuga):
    """
    Realiza un disparo en la posición especificada del tablero y actualiza el estado del juego 
    basándose en si el disparo acertó o falló.

    Args:
        vtnMenu (Tk): Ventana principal del juego.
        x (int): Índice de fila en el tablero donde se realiza el disparo.
        y (int): Índice de columna en el tablero donde se realiza el disparo.
        mtrBotones (list): Matriz de botones del tablero que se actualizará visualmente según el resultado del disparo.
        matrizGuardar (list): Matriz que almacena el estado actual del juego, usada para verificar si un disparo acierta.
        filas (int): Número total de filas en la matriz de juego.
        columnas (int): Número total de columnas en la matriz de juego.
        aciertos (list): Lista de listas donde se registran los aciertos de cada jugador.
        lstJuga (list): Lista de jugadores, usada para actualizar la puntuación y proporcionar feedback.

    Returns:
        None
    """

    global fase
    disparoAcertado=False
    if matrizGuardar[x][y] in lstTodasImagenes:
        mtrBotones[x][y].config(background="red")
        matrizGuardar[x][y]=f"{matrizGuardar[x][y]} "
        if fase==3:
            messagebox.showinfo("Jugador 1","Le diste!")
            lstJuga[0][2]+=1
            aciertos[0].append((x,y))
        else:
            messagebox.showinfo("Jugador 2","Le diste!")
            lstJuga[1][2]+=1
            aciertos[1].append((x,y))
        disparoAcertado=True
    elif matrizGuardar[x][y]==None:
        if fase==3:
            messagebox.showinfo("Jugador 1","Fallaste!")
        else:
            messagebox.showinfo("Jugador 2","Fallaste!")
    if disparoAcertado:
        aux=len(aciertos[0])
        aux2=len(aciertos[1])
        if fase==3:
            
            if aux==20:
                messagebox.showinfo("Jugador 2","ULTIMO TURNO!")
            else:
                messagebox.showinfo("Jugador 2","Tu turno!")
                fase=4
            
        else:
            if aux==20 or aux2==20:
                fase=5
                terminarPartida(vtnMenu,lstJuga)
            else:
                moverBarcos(matrizGuardar,filas,columnas)
                messagebox.showinfo("Atencion!","Los barcos se han movido!")
                messagebox.showinfo("Jugador 1", "Tu turno!")
                fase=3




def empezarJuego(vMenu,lstJugadores,mtrBotones,mtrImagenes,mtrBotones2,mtrImagenes2,matrizGuardar,matrizGuardar2,lstAciertos=[]):
    """
    Inicia la fase de combate del juego, actualizando la interfaz y preparando el juego para que los jugadores comiencen a interactuar en la fase de batalla.

    Args:
        vMenu (Tk): Ventana principal del juego donde se configurarán y mostrarán los elementos de la interfaz.
        lstJugadores (list): Lista que contiene la información de los jugadores, incluyendo nombres y puntuaciones.
        mtrBotones (list): Matriz de botones para el jugador 1 que será reconfigurada para la fase de combate.
        mtrImagenes (list): Matriz de imágenes para el jugador 1 que refleja el estado visual actual de los botones.
        mtrBotones2 (list): Matriz de botones para el jugador 2 que será reconfigurada para la fase de combate.
        mtrImagenes2 (list): Matriz de imágenes para el jugador 2 que refleja el estado visual actual de los botones.
        matrizGuardar (list): Matriz de control para guardar el estado del juego del jugador 1.
        matrizGuardar2 (list): Matriz de control para guardar el estado del juego del jugador 2.
        lstAciertos (list, optional): Lista de aciertos registrados en el juego, inicialmente vacía si no se provee.

    Returns:
        None
    """

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
    btnGuardar=Button(vMenu,text="Guardar Partida",font=("Arial", 12),command=lambda:guardarP(vMenu,lstJugadores,matrizGuardar,matrizGuardar2,lstAciertos))
    btnGuardar.place(x=320, y=600)

    btnEmpate=Button(vMenu,text="Terminar Partida",font=("Arial", 12),command=lambda:terminarPartida(vMenu,lstJugadores))
    btnEmpate.place(x=500, y=600)

    f=len(mtrImagenes)
    c=len(mtrImagenes[0])
    mtrBotones=matrizGrafica(mtrBotones,mtrImagenes,frameJugador1,f,c,mtrBotones2,mtrImagenes2,vMenu,lstJugadores,matrizGuardar,matrizGuardar2,lstAciertos)
    mtrBotones2=matrizGrafica(mtrBotones2,mtrImagenes2,frameJugador2,f,c,mtrBotones,mtrImagenes,vMenu,lstJugadores,matrizGuardar,matrizGuardar2,lstAciertos)
    mtrBotones=matrizGrafica(mtrBotones,mtrImagenes,frameJugador1,f,c,mtrBotones2,mtrImagenes2,vMenu,lstJugadores,matrizGuardar,matrizGuardar2,lstAciertos)
    
    
    

   

def barcoSeleccionado(n):
    """
    Establece el tipo de barco seleccionado en una variable global para uso en otras funciones del juego.

    Args:
        n (int): Número que representa el tipo de barco seleccionado.

    Returns:
        None
    """

    global barco
    barco=n


def orientacionSeleccionada(btnOrientacion):
    """
    Cambia la orientación global de los barcos y actualiza el texto del botón de orientación para reflejar la nueva orientación.

    Args:
        btnOrientacion (Tk.Button): Botón en la interfaz de usuario que muestra y cambia la orientación de los barcos.

    Returns:
        None
    """
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
    """
    Actualiza la matriz de imágenes con una nueva imagen en una posición específica.

    Args:
        imagen (str): La ruta de la imagen o el objeto de imagen que se colocará en la matriz.
        x (int): Índice de fila en la matriz donde se actualizará la imagen.
        y (int): Índice de columna en la matriz donde se actualizará la imagen.
        mtrImg (list): Matriz de imágenes que será actualizada.

    Returns:
        None
    """

    mtrImg[x][y]=imagen

def rotarImagen(imagen):
    """
    Rota una imagen dada según la orientación global actual del barco en el juego.

    Args:
        imagen (PIL.Image): La imagen del barco que será rotada.

    Returns:
        PIL.ImageTk.PhotoImage: La imagen rotada convertida en un formato utilizable por la interfaz gráfica Tkinter.
    """

    global barco,orientacion
    imagenRotada=imagen.rotate(orientacion*90)
    imagen=ImageTk.PhotoImage(imagenRotada)
    return imagen



def colocarBarcos(x, y, mtrBtn,mtrImg,filas,columnas,mtrOtrosBtn,mtrOtrasImg,vtnMenu,lstJugadores,matrizGuardar,matrizGuardar2):
    """
    Coloca barcos en la matriz gráfica según la orientación y el tipo de barco seleccionado,
    manejando los diferentes tamaños y tipos de barcos durante la fase de preparación del juego.

    Args:
        x (int): Índice de fila en la matriz donde el jugador intenta colocar un barco.
        y (int): Índice de columna en la matriz donde el jugador intenta colocar un barco.
        mtrBtn (list): Matriz de botones de la interfaz gráfica donde se mostrarán los barcos.
        mtrImg (list): Matriz de imágenes que refleja el estado visual actual de los botones.
        filas (int): Número total de filas en la matriz de juego.
        columnas (int): Número total de columnas en la matriz de juego.
        mtrOtrosBtn (list): Matriz de botones del oponente, utilizada para controlar la interacción durante el juego.
        mtrOtrasImg (list): Matriz de imágenes del oponente.
        vtnMenu (Tk): Ventana principal del juego.
        lstJugadores (list): Lista que contiene la información de los jugadores.
        matrizGuardar (list): Matriz de control para guardar el estado del juego del jugador actual.
        matrizGuardar2 (list): Matriz de control para guardar el estado del juego del oponente.

    Returns:
        list: Devuelve la matriz de botones actualizada después de colocar los barcos.
    """

    global barco,orientacion,imgAcorazado3,imgAcorazado2,imgAcorazado
    global imgCrusero,imgCrusero2,imgDestructor,barco1,barco2,barco3
    if orientacion==0:
        if barco==1 and barco1<6:
            if mtrBtn[x][y].cget('image')=='':
                img=rotarImagen(imgDestructor)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y].image=img
                barco1+=1
                actualizarImagen('img/b1.png',x,y,matrizGuardar)
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
                actualizarImagen('img/b22.png',x,y,matrizGuardar)
                actualizarImagen('img/b21.png',x,y+1,matrizGuardar)
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
                actualizarImagen('img/b33.png',x,y,matrizGuardar)
                actualizarImagen('img/b32.png',x,y+1,matrizGuardar)
                actualizarImagen('img/b31.png',x,y+2,matrizGuardar)
    elif orientacion==1:
        if barco==1 and barco1<6:
            if mtrBtn[x][y].cget('image')=='':
                img=rotarImagen(imgDestructor)
                mtrBtn[x][y].config(image=img)
                mtrBtn[x][y].image=img
                barco1+=1
                actualizarImagen(img,x,y,mtrImg)
                actualizarImagen('img/b1_rotated_90.png',x,y,matrizGuardar)
        elif barco == 2 and x>0 and barco2<4:
            if mtrBtn[x][y].cget('image')==''and mtrBtn[x-1][y].cget('image')=='':
                img=rotarImagen(imgCrusero)
                img2=rotarImagen(imgCrusero2)
                mtrBtn[x-1][y].config(image=img)
                mtrBtn[x][y].config(image=img2)
                mtrBtn[x-1][y].image=img
                mtrBtn[x][y].image=img2
                barco2+=1
                actualizarImagen('img/b21_rotated_90.png',x-1,y,matrizGuardar)
                actualizarImagen('img/b22_rotated_90.png',x,y,matrizGuardar)
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
                actualizarImagen('img/b33_rotated_90.png',x,y,matrizGuardar)
                actualizarImagen('img/b32_rotated_90.png',x-1,y,matrizGuardar)
                actualizarImagen('img/b31_rotated_90.png',x-2,y,matrizGuardar)
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
                actualizarImagen('img/b1_rotated_180.png',x,y,matrizGuardar)
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
                actualizarImagen('img/b22_rotated_180.png',x,y,matrizGuardar)
                actualizarImagen('img/b21_rotated_180.png',x,y-1,matrizGuardar)
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
                actualizarImagen('img/b33_rotated_180.png',x,y,matrizGuardar)
                actualizarImagen('img/b32_rotated_180.png',x,y-1,matrizGuardar)
                actualizarImagen('img/b31_rotated_180.png',x,y-2,matrizGuardar)
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
                actualizarImagen('img/b1_rotated_270.png',x,y,matrizGuardar)
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
                actualizarImagen('img/b22_rotated_270.png',x,y,matrizGuardar)
                actualizarImagen('img/b21_rotated_270.png',x+1,y,matrizGuardar)
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
                actualizarImagen('img/b33_rotated_270.png',x,y,matrizGuardar)
                actualizarImagen('img/b32_rotated_270.png',x+1,y,matrizGuardar)
                actualizarImagen('img/b31_rotated_270.png',x+2,y,matrizGuardar)

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
            fase+=1
            encenderBotones(mtrOtrosBtn)
        elif fase==1:
            empezarJuego(vtnMenu,lstJugadores,mtrOtrosBtn,mtrOtrasImg,mtrBtn,mtrImg,matrizGuardar,matrizGuardar2)
        
    


def matrizGrafica(mtrBtn,mtrImagenes,frame,filas,columnas,mtrOtrosBotones,mtrOtrasImagenes,vtnMenu,lstJugadores,matrizGuardar,matrizGuardar2,lstAciertos=[]):
    """
    Configura una matriz de botones dentro de un marco específico para la interfaz gráfica del juego, 
    con comportamientos dependientes del estado del juego. 

    Args:
        mtrBtn (list): Matriz de botones que será reconfigurada y devuelta.
        mtrImagenes (list): Matriz de imágenes correspondiente a los estados visuales de los botones.
        frame (Tk.Frame): Marco de la interfaz de usuario donde se colocarán los botones.
        filas (int): Número de filas para la matriz de botones.
        columnas (int): Número de columnas para la matriz de botones.
        mtrOtrosBotones (list): Matriz de botones correspondiente al otro jugador, utilizada en interacciones cruzadas.
        mtrOtrasImagenes (list): Matriz de imágenes correspondiente al otro jugador.
        vtnMenu (Tk): Ventana principal del juego.
        lstJugadores (list): Lista que contiene la información de los jugadores.
        matrizGuardar (list): Matriz de control para guardar el estado del juego para el jugador actual.
        matrizGuardar2 (list): Matriz de control para guardar el estado del juego para el otro jugador.
        lstAciertos (list, optional): Lista de aciertos registrados en el juego, por defecto es una lista vacía.

    Returns:
        list: Matriz de botones configurada según los parámetros y el estado del juego.
    """

    mtrBtn=[[None for _ in range(columnas)] for _ in range(filas)]
    for e in range(filas):
        for i in range(columnas):
            button = Button(frame, text="", width=4, height=2)
            button.grid(row=e, column=i,sticky="nsew")
            mtrBtn[e][i]=button
            if fase==0:
                button.config(command=lambda e=e, i=i: colocarBarcos(e, i, mtrBtn,mtrImagenes,filas,
                                                                 columnas,mtrOtrosBotones,mtrOtrasImagenes,vtnMenu,lstJugadores,matrizGuardar,matrizGuardar2))
            elif fase==2:
                button.config(image=mtrImagenes[e][i],command=lambda e=e, i=i:disparo(vtnMenu,e, i, mtrBtn,matrizGuardar,filas,columnas,lstAciertos,lstJugadores))
    return mtrBtn
    

def crearObjetos(vMenu,matriz,lstJugadores,mtrBotones,mtrBotones2,mtrImagenes,mtrImagenes2,matrizGuardar,matrizGuardar2):
    """
    Inicializa y coloca objetos en la interfaz gráfica del juego, incluyendo etiquetas, botones y marcos para cada jugador,
    y prepara las matrices de imágenes y botones para el juego.

    Args:
        vMenu (Tk): La ventana principal del juego donde se colocarán los objetos.
        matriz (list): Matriz utilizada para determinar dimensiones en algunas estructuras de datos.
        lstJugadores (list): Lista de jugadores, donde cada jugador es representado por una lista de datos (nombre, id, puntuación).
        mtrBotones (list): Lista inicial de botones para el jugador 1 que puede ser modificada durante la ejecución.
        mtrBotones2 (list): Lista inicial de botones para el jugador 2 que puede ser modificada durante la ejecución.
        mtrImagenes (list): Lista inicial de imágenes para el jugador 1 que puede ser modificada durante la ejecución.
        mtrImagenes2 (list): Lista inicial de imágenes para el jugador 2 que puede ser modificada durante la ejecución.
        matrizGuardar (list): Matriz para almacenar datos del juego para el jugador 1.
        matrizGuardar2 (list): Matriz para almacenar datos del juego para el jugador 2.

    Returns:
        None: Esta función no retorna ningún valor pero realiza la configuración inicial de la interfaz del usuario.
    """
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
    matrizGuardar=[[None for _ in range(c)] for _ in range(f)]
    matrizGuardar2=[[None for _ in range(c)] for _ in range(f)]
    mtrBotones=matrizGrafica(mtrBotones,mtrImagenes,frameJugador1,f,c,mtrBotones2,mtrImagenes2,vMenu,lstJugadores,matrizGuardar,matrizGuardar2)
    mtrBotones2=matrizGrafica(mtrBotones2,mtrImagenes2,frameJugador2,f,c,mtrBotones,mtrImagenes,vMenu,lstJugadores,matrizGuardar2,matrizGuardar)
    mtrBotones=matrizGrafica(mtrBotones,mtrImagenes,frameJugador1,f,c,mtrBotones2,mtrImagenes2,vMenu,lstJugadores,matrizGuardar,matrizGuardar2)
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
lstTodasImagenes=['img/b1.png','img/b1_rotated_90.png','img/b1_rotated_180.png','img/b1_rotated_270.png',
                      'img/b21.png','img/b21_rotated_90.png','img/b21_rotated_180.png','img/b21_rotated_270.png',
                      'img/b22.png','img/b22_rotated_90.png','img/b22_rotated_180.png','img/b22_rotated_270.png',
                      'img/b31.png','img/b31_rotated_90.png','img/b31_rotated_180.png','img/b31_rotated_270.png',
                      'img/b32.png','img/b32_rotated_90.png','img/b32_rotated_180.png','img/b32_rotated_270.png',
                      'img/b33.png','img/b33_rotated_90.png','img/b33_rotated_180.png','img/b33_rotated_270.png']