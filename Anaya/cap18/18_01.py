# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:27:24 2023

@author: shama

manejo de errores archivo de practica

"""

try:
    archivo = open("resultado.txt", "w")
    print("Archivo resultado.txt abierto.")
    resultado = 15 * (3/0)
except IOError:
    # Instrucciones si ocurre la excepcion IOError
    print("Error de entrada/salida.")
except ZeroDivisionError:
    # Instrucciones si ocurre la excepcion ZeroDivisionError
    print("Error de division por cero.")
else:
    # Instrucciones si no ocurre ninguna excepcion
    print("El resultado de la division es", resultado)
    archivo.write(resultado)
finally:
    # Instrucciones si ocurren o no ocurren excepciones
    if not(archivo.closed):
        archivo.close()
        print("Archivo resultado.txt cerrado.")