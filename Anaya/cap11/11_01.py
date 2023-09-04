# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:41:52 2023

@author: shama
"""

"""
Problema 1

Escriba unm programa que lea una cadena escrita por teclado y compurebe si
el primer y el ultimo caracter son iguales. Si son iguales, mostrara un mensaje
con el numero total de caracteres distintos a dicho caracter. En caso contrario,
mostrara un mensaje con el numero total de caracteres de la cadena iguales al
caracter incial y al caracter final (sin incluirlos)

"""

# Solicitamos una cadena por teclado y la almacenamos 
cadena = input("Escriba una cadena de caracteres: ")
# Pasamos la cadena a minuscula 
cadena = cadena.lower()

# Si el caracter inicial es igual al final
if cadena[0] == cadena[-1]:
    # Calculamos el numero de caracteres distinto a ellos
    caracteres_distintos = len(cadena) - cadena.count(cadena[0])
    # Creamos una cadena con el mensaje a imprimir
    mensaje = f"La cadena introducidatiene {caracteres_distintos} caracteres distintos a los caracteres inicial y final."
else: # Si el caracter inicial es distinto al final
    # Calculamos el numero de caracteres iguales al caracter inicial (sin incluirlo)
    caracteres_iguales_inicio = cadena.count(cadena[0])-1
    # Calculamos el numero de caracteres iguales al caracter final (sin incluirlo)
    caracteres_iguales_fin = cadena.count(cadena[-1])-1
    # Calculamos el numero de caracteres igual al caracter inicial y al final (sin incluirlos)
    total_caracteres_iguales = caracteres_iguales_inicio + caracteres_iguales_fin 
    # Creamos una cadena con el mensaje a imprimir
    mensaje = f"La cadena introducida tiene {total_caracteres_iguales} caracteres iguales a los caracteres inicial y final."
#Imprimimos por pantalla el mensaje adecuado
print(mensaje)


"""
Problema 2

Utiliza los metodos split() y join() para sustituir el nombre de la cadena "Mi nombre es Paula" por tu nombre.

"""
# Cadena a modificar
cadena = "Mi nombre es Paula"
# Las cadenas son inmutables y no se pueden modificar 
# Las listas si son mutables
# Generamos una lista resultante de dividir la cena por esapcios 
lista_cadenas = cadena.split()
# Modificiamos el cuarto elemento por nuestro nombre
lista_cadenas[3] = "Adrian"
# Utilizamos el metodo join para unir las cadenas de la lista utilizando espacios
cadena = " ".join(lista_cadenas)
# Mostramos la cadena
print(cadena)

"""
Problema 3

Las siguientes cadenas formateadas tienen errores. Realiza las correcciones 
necesarias para que sean validas y pruebalas en la terminal de IPython.

"""

"""
 "No me canso de %s." %("aprender", "Python")
 format("Estoy deseando empezar el capitulo %d", 12)
 accion = "formatear"
 f"Ya se {s} cadneas en Python" % accion
"""

"No me canso de %s." %("aprender Python")

"Estoy deseando empezr el capitulo {0}".format(12)

accion = "formatear"
f"Ya se {accion} en Python"