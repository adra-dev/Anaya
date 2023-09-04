# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:58:51 2023

@author: shama

Programa principal Interfaces Graficas de Usuario
"""

from tkinter import *
import tkinter.ttk as ttk
from webfrec import *


max_frec = 20

def descargar(*args):
    """ Esta funcion se invoca al pulsar en el boton 'Descargar' """
    text = descargar_pagina(url.get())
    textcomp.replace(1.0, END, text)
    
    frec_items = contar_palabras(text)
    for entry in tree.get_children():
        tree.delete(entry)
    for k,v in frec_items[:max_frec]:
        tree.insert("", "end", values=(k,v))
        

def contar(*args):
    frec_items = contar_palabras(textcomp.get(1.0, END))
    for entry in tree.get_children():
        tree.delete(entry)
    for k,v in frec_items[:max_frec]:
        tree.insert("", "end", values=(k, v))
        
root = Tk()
root.title("Analizador de paginas web")

# Marco principal
mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#
# Marco para direccion web y boton de descarga
#
urlframe = ttk.Frame(mainframe)
urlframe.grid(column=1, row=1, sticky=W, pady="5 0")

# Eiqueta
ttk.Label(urlframe, text="Direccion:").grid(column=1, row=1, sticky=W)

# Campo de direccion web
url = StringVar()
urlentry = ttk.Entry(urlframe, width=83, textvariable=url)
urlentry.grid(column=3, row=1, sticky=W, padx="5 0")

# Boton de descarga
button = ttk.Button(urlframe, text="Descargar", command=descargar)
button.grid(column=3, row=1, sticky=E, padx="5 0")

# Boton de cuenta
button = ttk.Button(urlframe, text="Contar", command=contar)
button.grid(column=4, row=1, sticky=W, padx="5 0")

#
# Marco para mostrar datos de la pagina
#
showframe = ttk.Frame(mainframe)
showframe.grid(column=1, row=2, pady="5 0")

ttk.Label(showframe, text="Texto:").grid(column=1, row=1, sticky=W)
ttk.Label(showframe, text="Tabla de frecuencias:").grid(column=3, row=1, sticky=W)

#Lienzo de texto donde mostrar contenido
content = StringVar()
textcomp = Text(showframe, width=80, height=26)
textcomp.grid(column=1, row=2, sticky=W)


#Barra de desplazamiento para el are de texto
scrollbar = ttk.Scrollbar(showframe, command=textcomp.yview)
scrollbar.grid(column=2, row=2, sticky='wns')
textcomp['yscrollcommand'] = scrollbar.set


# Tabla donde se muestran las palabras mas frecuentes
tree = ttk.Treeview(showframe, height=max_frec, columns=("pal", "frec"))
tree.grid(column=3, row=2, sticky=(W, N), padx="5 0")
tree.column("#0", width=0, minwidth=0, stretch=NO)
tree.column("pal", width=100, minwidth=100, stretch=NO)
tree.column("frec", width=70, minwidth=70, stretch=NO)
tree.heading("pal", text="Palabra", anchor=W)
tree.heading("frec", text="Frecuencia", anchor=W)

# Configuracion final
urlentry.focus()
root.bind('<Return>', descargar)
root.resizable(width=False, height=False)
root.mainloop()
