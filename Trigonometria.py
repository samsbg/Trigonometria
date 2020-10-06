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

trig = tk.Tk()
trig.title("Trogonometría")
trig.geometry("900x500")
#trig.resizable(width=False, height=False)
trig.configure(bg="#DEF0D9")

def segundaPagina():

    titulo.grid(column=3, row=0, columnspan=15, rowspan=2, sticky="WNSE")

    instrucciones = tk.Label(
        text="Poner la respuesta en fracción", font=(None, 20), bg="#DEF0D9")
    instrucciones.grid(column=5, row=3, columnspan=8)

    triangulos = (ImageTk.PhotoImage(Image.open(os.path.abspath(
        "Triangulo1.png")).resize((300, 300), Image.ANTIALIAS)), ImageTk.PhotoImage(Image.open(os.path.abspath(
            "Triangulo2.png")).resize((300, 300), Image.ANTIALIAS)))

    trianguloLabel = tk.Label(trig, bg = "#DEF0D9")
    trianguloLabel.grid(column=6, row=5, columnspan=6, rowspan=6)
    
    trigList = ("sen(A) =", "cos(A) =", "tan(A) =")

    triglabel = tk.Label(font=(None, 20), bg="#DEF0D9")
    triglabel.grid(column=6, row=13, columnspan=3, sticky="e")

    xlabel = tk.Label(font=(None, 20), bg="#DEF0D9")
    xlabel.grid(column=5, row=7, rowspan=2, sticky = "e")

    ylabel = tk.Label(font=(None, 20), bg="#DEF0D9")
    ylabel.grid(column=8, row=11, columnspan=2)

    zlabel = tk.Label(font=(None, 20), bg="#DEF0D9")
    zlabel.grid(column=12, row=7, rowspan=2, sticky = "w")

    respuesta = Entry(trig, width=10, font=(None,20))
    respuesta.grid(column=9, row=13, columnspan=3, sticky="w")

    verifica = tk.Button(text="Verificar", bg="#5BB346",
                         fg="white", font=(None, 20))
    verifica.grid(column=14, row=13, columnspan=3, pady=10)

    def nuevoEjercicio():

        trianguloInt = randint(0,1)
        ladosInt = randint(2,7)
        trigInt = randint(0,2)
        
        trianguloLabel.configure(image=triangulos[trianguloInt])
        trianguloLabel.image = triangulos[trianguloInt]
        
        y = (ladosInt*2)+1
        z = (y**2-1)//2
        x = (y**2+1)//2

        xlabel.configure(text=x)
        ylabel.configure(text=y)
        zlabel.configure(text=z)

        triglabel.configure(text=trigList[trigInt])

        def respuestaString():
            if(trianguloInt == 0):
                if(trigInt == 0): 
                    return("{}/{}".format(z,x))
                elif(trigInt == 1):
                    return("{}/{}".format(y, x))
                elif(trigInt == 2):
                    return("{}/{}".format(z, y))
            elif(trianguloInt == 1):
                if(trigInt == 0):
                    return("{}/{}".format(y, x))
                elif(trigInt == 1):
                    return("{}/{}".format(z, x))
                elif(trigInt == 2):
                    return("{}/{}".format(y, z))
        
        def versiguiente():
            respuesta.delete(0, "end")
            respuesta.configure(bg="white")
            verifica.configure(text="Verificar",command=verificar)
            nuevoEjercicio()
        
        def verificar():
            
            if(respuesta.get() == respuestaString()):
                respuesta.configure(bg="green")
                verifica.configure(text="Siguiente", command=versiguiente)
            else:
                respuesta.configure(bg="red")
                verifica.configure(text="Siguiente", command=versiguiente)

        verifica.configure(command = verificar)
        
    nuevoEjercicio()

    for y in range(15):
        trig.grid_rowconfigure(y, weight=1)

def primeraPagina():

    titulo.grid(column=3, row=0, columnspan=12, rowspan = 2, sticky="WNSE")

    def regresar():
        print("Pagina principal")

    regreso.configure(command=regresar)

    def irSiguiente():
        aprende.grid_forget()
        triangulolabel.grid_forget()
        reglas.grid_forget()
        xLabel.grid_forget()
        yLabel.grid_forget()
        zLabel.grid_forget()
        ejemploLabel.grid_forget()
        ejemploEntry.grid_forget()
        siguiente.grid_forget()

        segundaPagina()
    
    siguiente.configure(command=irSiguiente)
    siguiente.grid(column = 15, row = 0, rowspan = 2, columnspan = 3, sticky = "NSWE")

    regreso.configure(command=regresar)

    reglas = tk.Label(justify = LEFT, padx = 10, bg="#DEF0D9", font=(None, 18), text="\nsen(A) = cateto opuesto/hipotenusa = z/x\ncos(A) = cateto adyacente/hipotenusa = y/x\ntan(A) = cateto opuesto/cateto adyacente = z/y\n\nCateto opuesto = lado opuesto al ángulo\nCateto adyacente = lado al lado del ángulo\nHipotenusa = lado más largo del triángulo")
    reglas.grid(column = 0, row = 4, columnspan = 12, rowspan = 6, sticky = "N")

    aprende = tk.Label(bg="#DEF0D9", font=(None, 20), text="Aprende")
    aprende.grid(row = 2, column = 6, columnspan = 6, rowspan = 2)

    triangulo = ImageTk.PhotoImage(Image.open(os.path.abspath(
        "Triangulo1.png")).resize((200, 200), Image.ANTIALIAS))
    triangulolabel = tk.Label(trig, image=triangulo, bg="#DEF0D9")
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

    ejemploEntry = Entry(trig, width=3, font=(None,20))
    ejemploEntry.insert(END,"z/x")
    ejemploEntry.configure(state="disabled")
    ejemploEntry.grid(column = 15, row = 10, columnspan = 3, rowspan = 1, sticky="SW")

    for y in range(12):
        trig.grid_rowconfigure(y, weight=1)

    for x in range(18):
        trig.grid_columnconfigure(x, weight=1)


titulo = tk.Label(justify=LEFT, text="Trigonometría",
                  bg="#5BB346", fg="white", font=(None, 20))
siguiente = tk.Button(text=" 🡆 ", bg="#5BB346", fg="white", font=(None, 20))

regreso = tk.Button(text=" 🡄 ", bg="#5BB346", fg="white", font=(None, 20))
regreso.grid(column=0, row=0, columnspan=3, rowspan=2, sticky="NSWE")

primeraPagina()

trig.mainloop()
