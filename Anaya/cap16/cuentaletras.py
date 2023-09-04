# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:37:59 2023

@author: shama

Modulo para contar las vocales y consonantes de una cadena

"""

__author__= "Arturo y Salud"
__copyright__ = "Curso de programacion Python"
__credits__ = "Arturo y Salud"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "libropython@gmail.com"
__status__ = "Development"


import re 

def contar_vocales(texto):
    """Calcula el total de vocales que tiene un texto"""
    return len(re.findall("[aeiou]", texto, re.IGNORECASE))


def contar_consonantes(texto):
    """Calcula el total de consonantes que tiene un texto"""
    return len(re.findall("[bcdfghjklmnpqrstvwxyz]", texto, re.IGNORECASE))

if __name__ == "__main__":
    cadena = input("Escribe una cadena: ")
    vocales = contar_vocales(cadena)
    consonantes = contar_consonantes(cadena)
    print("La cadena", cadena,"tiene", vocales, "vocales y", consonantes, "consonantes.")
    

