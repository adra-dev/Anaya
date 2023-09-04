# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:15:51 2023

@author: shama

Ejecuta las siguientes lindeas de codigo en la terminald IPython para crear
el archivo de texto archivo_ejercicio.txt con el contenido "Ya se
como trabajar con archivos en Python."

f = open("archivo_ejercicio.txt", "w")
f.write("Ya se como trabajar con archivos en Python.")
f.read()
f.close()
"""

# a) que significa el valor que ha devuelto el metodo write()?
## el numero de bytes/caracteres escritos


# b) por que se produce un error al ejecutar la entrada 3(In [3])?
## se produce un error porque no se puede leer el archivo ya que esta abierto en modo escritura


# c) Reescribe el codigo anterior para que no se produzca ningun error

f = open("archivo_ejercicio.txt", "r+")
f.write("Ya se como trabajar con archivos en Python.")
f.seek(0)
f.read()
f.close()


"""
Supon que quieres seguir aniadiendo contenido al archivo de texto "archivo_
ejercicio.txt", creado en el ejercicio anterior.Indica cuales de los 
siguientes metodos de apertura son adecuados para tal fin y justificalo.

a.f = open("archivo_ejercicio.txt")
b.f = open("archivo_ejercicio.txt", "r+")
c.f = open("archivo_ejercicio.txt", "w")
d.f = open("archivo_ejercicio.txt", "a")

"""
'''
El unico modo de apertura que es adecuado para seguir aniadiendo contenido 
es el del apartado d ya que el modo a solo lee el archivo, y los otros dos 
sobreescribirian el contenido existente.
'''

"""
Escribe dos progamas, uno teniendo en cuenta las especificaciones del
apartado a y otro teniendo en cuenta las del apartado b. Ambos deberan
guardar en un archivo la siguiente lista de tuplas:

lista_capitulos = [("capitulo 1", "Los ninos y la progamacion de ordenadores"), ("capitulo 2", 
"Introduccion a la progamacion"), ("capitulo 3", "El lenguaje Python y por que debemos aprenderlo")]

"""

'''
a. El programa A debera escribir el contenido de la lista en un archivo 
de texto, cerrarlo y posteriormente debera abrirlo para leer su contenido y
generar una lista con la misma esctructura.

'''

# Programa A

lista_capitulos = [("capitulo 1", "Los ninos y la progamacion de ordenadores"), ("capitulo 2", 
"Introduccion a la progamacion"), ("capitulo 3", "El lenguaje Python y por que debemos aprenderlo")]

# Abrimos el archivo de texto en modo escritura
with open("archivo_apartado_a.txt", "w") as f:
    #Escribimos cada capitulo junto con su titulo en una linea, separando ambos por un guion
    for cap, titulo in lista_capitulos:
        f.write(cap + "-" + titulo + "\n")
        
# Creamos la lista que tenemos que generar apartir del archivo
lista_generada = []

# Abrimos el archivo de texto en modo lectura 
with open("archivo_apartado_a.txt", "r") as f:
    #Recorremos todas las lineas del archivo
    for linea in f.readlines():
        # Eliminamos de cada linea el \n final 
        # y despues separamos su contenido en capitulo y titulo 
        # utilizando el caracter guion
        cap, titulo = linea.strip().split("-")
        # Aniadimos la tupla (cap, titulo) a la lista
        lista_generada.append((cap, titulo))
# Mostramos la lista generada para comprobar que su contenido es el mismo que el de la lista 
print(lista_generada)
    
'''
b. El programa B debera escribir el contenido de la lista en un archivo 
binario, cerrarlo y posteriormente debera abrirlo para leer su contenido y
generar una lista con la misma esctructura. Para ello utiliza el modulo pickle.

'''

# Programa B

import pickle

lista_capitulos = [("capitulo 1", "Los ninos y la progamacion de ordenadores"), ("capitulo 2", 
"Introduccion a la progamacion"), ("capitulo 3", "El lenguaje Python y por que debemos aprenderlo")]

# Abrimos el archivo de binario en modo escritura
with open("archivo_apartado_b.p", "wb") as f:
    #Escribimos en el el objeto lista_capitulos haciendo uso del metodo dump del modulo pickle
    pickle.dump(lista_capitulos, f)

# Abrimos el archivo de binario en modo lectura 
with open("archivo_apartado_b.p", "rb") as f:
    # Cargamos el objeto que contiene la lista que tenemos que generar
    lista_generada = pickle.load(f)
       
# Mostramos la lista generada para comprobar que su contenido es el mismo que el de la lista 
print(lista_generada)
    