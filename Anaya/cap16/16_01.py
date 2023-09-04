# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:27:19 2023

@author: shama

capitulo 16 ejercicios

1. Crea un progama que imprima por pantalla todos los componentes del 
modulo re que terminen en ch.

"""

import re

# Listamos los componentes del modulo re
componentes = dir(re)
# Creamos una expresion regular para buscar al fianl de una cadena la subcadena ch
regex_ch = re.compile(r'ch$')
# Lista de componentes terminados en ch
componentes_ch = []

for componente in componentes:
    # Si el componente termina en ch
    if(re.search(regex_ch, componente)):
        # Lo aniadimos a la lista
        componentes_ch.append(componente)
        
# Mostramos la lista resultante
print("La lista de componentes del modulo re terminados en ch es la siguiente:", componentes_ch)

"""
2. Indica cules de las siguientes formas de importacion y uso no son las correctas.Justificalo.

a. from math import sqrt                                valido
   math.sqrt(3)

b. from cuentaletras import contras_vocales             valido

c. from math import sqrt, pow as raiz, potencia         invalido

"""

"""
3. Crea el modulo cadenas con una funcion concatenar(cadena1,cadena2) que
realice la concatenacion de dos cadenas y una funcion dividir(cadena,
separador) que separe una cadena en subcadenas a partir del caracter separador
indicado.Crea un script ejercicio3.py que importe el modulo anterior y que 
utilizando sus funciones concatene las cadenas 'coche,' ,'moto,' y 
'bicicleta' y, una vez concatenadas las tres palabras, el script debera dividir
la cadena utilizando el caracter coma <<,>> antes de mostrar las palabras.

"""