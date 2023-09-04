# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:22:22 2023

@author: shama

Ejercicios capitulo 15 funciones

"""

def extrae(valores, comp):
    a = valores[0]
    for x in valores [1:]:
        if comp(x, a):
            a = x
    return a
    

def mayor(a, b):
    return a > b
    

def menor(a , b):
    return a < b
    

print(extrae([2, 3, 6, 8, 10], mayor))


print(extrae([2, 3, 6, 8, 10], menor))


def comprueba(items):
    def desechar(item):
        print('El item', item, 'no es valido')
    for i,x in enumerate(items):
        if x > 100:
            desechar(i)


def comparaciones(tipo):
    
    def mayor(a,b):
        if a > b:
            return a
        return b
    if tipo == 'mayor':
        return mayor 
    if tipo == 'menor':
        return lambda x,y: x if x < y else y
    
f = comparaciones('mayor')
print(f(10,7))
f = comparaciones('menor')
print(f(10,7))
