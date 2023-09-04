# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:42:33 2023

@author: shama

Modulo que permite concatenar cadenas y dividr una cadena en subcadenas

"""

__author__= "Arturo y Salud"
__copyright__ = "Curso de programacion Python"
__credits__ = "Arturo y Salud"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "libropython@gmail.com"
__status__ = "Development"


def concatenar(cadena1, cadena2):
    """Concatenar dos cadenas"""
    return cadena1 + cadena2

def dividir(cadena, separador):
    """Divide una cadena en subcadenas utilizando el separador indicado"""
    return cadena.split(separador)


    