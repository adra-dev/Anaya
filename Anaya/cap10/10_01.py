# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:52:21 2023

@author: shama
"""

"""
Problema 1

Escriba usando comprension de listas, como generar una lista con los numeros
pares comprendidos entre 0 y 99 en una sola linea de codigo
 
"""

[x for x in range(100) if x % 2 == 0]



"""
Problema 2

El siguiente codigo es de un programa que calcula el mes mas lluvioso a partir
del registro mensual en litros.Debes completar este codigo sustituyendo los 
comentarios en negrita en las operaciones sobre listas adecuadas para una
correcta ejecucuion del programa.

"""
"""
lluvia_mensual = [65, 70, 87, 62, 44, 14, 5, 5, 24, 50, 57, 69]
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
max_lluvia = # calcula aqui el maximo valor de lluvia registrada
mes_max = # obten el indice del mes correspondiente
print('El mes mas lluvioso ha sido', meses[mes_max], 'con', max_lluvia, 'litros')
"""
lluvia_mensual = [65, 70, 87, 62, 44, 14, 5, 5, 24, 50, 57, 69]
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
max_lluvia = max(lluvia_mensual)
mes_max = lluvia_mensual.index(max_lluvia)
print('El mes mas lluvioso ha sido', meses[mes_max], 'con', max_lluvia, 'litros')