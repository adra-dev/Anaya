# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:14:18 2023

@author: shama

Realiza pruebas unitarias utilizando assert para comprobar si la siguiente 
funcion calcula correctamente el factorial de un numero. En caso de que haya
algun error, indica cual seria la solucion correcta.

"""

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

resultado = factorial(0)
assert resultado == 1

resultado = factorial(1)
assert resultado == 1

resultado = factorial(2)
assert resultado == 2

resultado = factorial(3)
assert resultado == 6

