# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:45:19 2023

@author: shama

Crea una excepcion propia para gestionar la deteccion de una cadena inferior
a dos caracteres en una lista de nombres. Escribe un progama que haga uso 
de esa excepcion para evitar mostrarla por pantalla. Por ejemplo, dada la lista:

nombres = ['Turing', 'Feynman', '', 'Tintin', 'G']

"""

class InvalidNameException(Exception):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return "Error: " + str(self.valor)
        
nombres = ['Turing', 'Feynman', '', 'Tintin', 'G']
for n in nombres:
    try:
        if len(n) < 2:
            raise InvalidNameException(n)
        print(n)
    except InvalidNameException:
        pass
    