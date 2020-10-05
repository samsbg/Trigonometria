#Autor: Samantha Bautista
#Matricula: A01284462
#Campus: Monterrey
#Fecha: 
#Actividad: Proyecto final PISA: trigonometria

from tkinter import *
import tkinter as tk
from random import randint
from PIL import ImageTk, Image
import os

ort = tk.Tk()
ort.title("Trogonometría")
ort.geometry("900x500")
#ort.resizable(width=False, height=False)
ort.configure(bg="#DEF0D9")

def segundaPagina():
    print("Siguiente pagina")

def primeraPagina():

    titulo.grid(column=3, row=0, columnspan=12, rowspan = 2, sticky="WNSE")

    def regresar():
        print("Pagina principal")

    regreso.configure(command=regresar)

    def irSiguiente():
        segundaPagina()
    
    siguiente.configure(command=irSiguiente)
    siguiente.grid(column = 15, row = 0, rowspan = 2, columnspan = 3, sticky = "NSWE")

    regreso.configure(command=regresar)
    regreso.grid(column=0, row=0, columnspan=3, rowspan=2, sticky="NSWE")

    reglas = tk.Label(justify = LEFT, padx = 10, bg="#DEF0D9", font=(None, 18), text="\nsen(A) = cateto opuesto/hipotenusa = z/x\ncos(A) = cateto adyacente/hipotenusa = y/x\ntan(A) = cateto opuesto/cateto adyacente = z/y\n\nCateto opuesto = lado opuesto al ángulo\nCateto adyacente = lado al lado del ángulo\nHipotenusa = lado más largo del triángulo")
    reglas.grid(column = 0, row = 4, columnspan = 12, rowspan = 6, sticky = "N")

    aprende = tk.Label(bg="#DEF0D9", font=(None, 20), text="Aprende")
    aprende.grid(row = 2, column = 6, columnspan = 6, rowspan = 2)

    triangulo = ImageTk.PhotoImage(Image.open(os.path.abspath(
        "Triangulo1.png")).resize((230, 230), Image.ANTIALIAS))
    triangulolabel = tk.Label(ort, image=triangulo, bg="#DEF0D9")
    triangulolabel.image = triangulo
    triangulolabel.grid(column = 13, row = 5, rowspan = 4, columnspan = 4)

    xLabel = tk.Label(text="x", font=(None, 20), bg="#DEF0D9")
    xLabel.grid(column = 12, row = 6, rowspan = 2)

    yLabel = tk.Label(text="y", font=(None, 20), bg="#DEF0D9")
    yLabel.grid(column=14, row=9, columnspan=2)

    zLabel = tk.Label(text="z", font=(None, 20), bg="#DEF0D9")
    zLabel.grid(column=17, row=6, rowspan=2, padx = 10)

    ejemploLabel = tk.Label(text="sen(A) =", bg="#DEF0D9", font=(None, 20))
    ejemploLabel.grid(column = 12, row = 10, columnspan = 3, rowspan = 2, sticky="E")

    ejemploEntry = Entry(ort, width=3, font=(None,20))
    ejemploEntry.insert(END,"z/x")
    ejemploEntry.configure(state="disabled")
    ejemploEntry.grid(column = 15, row = 10, columnspan = 3, rowspan = 1, sticky="SW")

    for y in range(12):
        ort.grid_rowconfigure(y, weight=1)

    for x in range(18):
        ort.grid_columnconfigure(x, weight=1)


siguiente = tk.Button(text=" 🡆 ", bg="#5BB346", fg="white", font=(None, 20))
regreso = tk.Button(text=" 🡄 ", bg="#5BB346", fg="white", font=(None, 20))
titulo = tk.Label(justify = LEFT, text="Ortografía", bg="#5BB346", fg="white", font=(None, 20))

primeraPagina()

ort.mainloop()
