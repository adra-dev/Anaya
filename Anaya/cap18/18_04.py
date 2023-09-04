# -*- coding: utf-8 -*-
"""
Created on Tue May  2 13:58:11 2023

@author: shama

Escribe un progama que reciba como entrada una lista con varios elemntos
de tipo entero, y el ultimo elemento de tipo cadena de caracteres. Recorre
todos los elementos de esa lista y calcula el numero factorial de cada elemento
(con el metodo math.factorial()), mostrando el resultado por consola si no se 
produce ninguna excepcion. Captura las excepciones convenientes y muestra 
un mensaje final, indicadno el valor que se ha procesado.

"""

# Importamos la calse math para el calculo del factorial
import math

lista = [5,7,-9,'cadena']

for valor in lista:
    try:
        factorial = math.factorial(valor)
    except TypeError:
        print("Excepcion TypeError: no se puede calcular el factorial para el tipo de dato", type(valor))
    except ValueError:
        print("Excepcion ValueError: Factorial solo acepta valores enteros positivos", valor, "no es un valor entero positivo")
    else:
        print("El factorial de", valor, "es", factorial)
    finally:
        print("Valor", valor, "procesado")
        
