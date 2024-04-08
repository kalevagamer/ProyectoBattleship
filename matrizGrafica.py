import tkinter as tk
from PIL import ImageTk, Image

matriz_botones=[]


def accion(x,y):
  print (f"x={x},y={y}")
  global matriz_botones
  global imagen
  matriz_botones[y][x].configure(image=imagen)
  matriz_botones[y][x].configure(relief="solid")

 
def tablero (x:int,y:int)->tk.Tk:
  global matriz_botones 
  juego = tk.Tk()
  juego.title("Battleship")
  juego.config(bg='grey')
  resolucion=f"{x*50}x{y*50}+0+0"
  print (resolucion)
  juego.geometry(resolucion)

  matriz_botones=[[tk.Button(juego, command=lambda x=c,y=f:accion(x,y)) 
                   for c in range(x)] for f in range(y)]
  posx=1
  posy=1
  for fila_botones in matriz_botones:
    posx=0
    for btn in fila_botones:
      btn.place(x=posx,y=posy, height=49, width=49)
      btn.configure(bd=0)
      
      posx+=50 
    posy+=50
  print (matriz_botones)

  return juego 

juego=tablero(20,10)

imagen = Image.open("img/b1.png")
imagen = imagen.resize((50, 50))  # Ajusta el tamaño de la imagen
imagen_rotada = imagen.rotate(0)
imagen = ImageTk.PhotoImage(imagen_rotada)

juego.mainloop()
