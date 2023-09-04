# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:45:56 2023

@author: shama
"""

import cadenas

if __name__ ==  "__main__":
    cadena1 = "coche,"
    cadena2 = "moto,"
    cadena3 = "bicicleta"
    
    cadena_concatenada = cadenas.concatenar(cadena1, cadena2)
    cadena_concatenada = cadenas.concatenar(cadena_concatenada, cadena3)
    
    cadenas_resultantes = cadenas.dividir(cadena_concatenada, ",")
    
    print("Las cadenas resultantes son:\n"+ '\n'.join(cadenas_resultantes))
    