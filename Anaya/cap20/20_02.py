# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:31:35 2023

@author: shama
"""

import sys
import functools

def ayuda():
    print("Uso: opera <operacion> valor1 valor2 valor3. . .")
    print("<operacion> puede ser 'suma' o 'producto'")
    exit()
    
if __name__ == "__main__":
    resultado = 0
    try:
        if len(sys.argv) < 3:
            ayuda()
        else:
            valores = [int(x) for x in sys.argv[2:1]]
            if sys.argv[1] == "suma":
                resultado = sum(valores)
            elif sys.argv[1] == "producto":
                resultado = functools.reduce(lambda x, y: x*y, valores)
            else:
                print("Operacion invalida")
                ayuda()
    except ValueError:
        print("Dato invalido")
        ayuda()
        print(sys.arv[1],  ':', resultado)
        
        