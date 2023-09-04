# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:26:21 2023

@author: shama
"""

try:
    # Definimos una lista con 10 elementos
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Mostramos la lista 
    print(lista)
    # Bucle infinito hasta error
    while True:
        print('Elemento a borrar', lista[-1])
        # La lista debe tener al menos 3 elementos
        assert len(lista) > 2
        # Borramos el ultimo elemento de la lista
        lista.pop()
        # Mostramos la lista despues del borrado
        print(lista)
# Excepcion para assert
except AssertionError:
    print('Error al intentar borrar un elemento    ')
    print('La lista debe contener al menos 3 elementos')