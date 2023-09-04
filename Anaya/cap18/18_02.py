# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:53:16 2023

@author: shama
"""

class MiExcepcion(Exception):
    def _init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return "Error: " + str(self.valor)
    
try:
    fin = False
    while not fin:
        entrada = input("Introduzca c para continuar o f para finalizar:")
        if entrada != "f" and entrada != "c":
            raise MiExcepcion(entrada + " no es un valor valido.")
        elif entrada == "f":
            fin = True
            
except MiExcepcion as e:
    print (e)