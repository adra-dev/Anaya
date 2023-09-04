# -*- coding: utf-8 -*-
"""
Editor de spyder

Este es un archivo temporal.
"""

import datetime

def edad(anio_nac):
    """
    Esta funcion calcula los anios que cumples en el anio actual
    """
    
    hoy = datetime.datetime.today() 
    return hoy.year - anio_nac
mi_edad = edad(1998)

# mostramos el resultado en pantalla

print("Este anio cumples", mi_edad, "anios")
