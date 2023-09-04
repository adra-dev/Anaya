# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:44:01 2023

@author: shama
"""


a = 4
acc = 1 
while a > 1:
    acc *= a
    a-= 1
print(acc)


a=5
for f in range(2,a):
    a*=f
print(a)

num = 811
test = 'es primo'

for div in range(2, num):
    if num % div == 0:
        test = 'no es primo'
        break
print(num,test)

for d in range(1,31):
    print('----')
    print('Dia', d)
    if d % 7 == 6 or d % 7 == 0:
        print('Descansar')
        continue
    print('Levantarse temprano')
    print('Ir a trabajar')
    
for elemento in ['cerrado','cerrado','cerrado','cerrado','abierto',
'cerrado', 'cerrado']:
    if elemento =='abierto':
        print('Avisar a la policia')
        break
    
else:
    print('Todo en order')
        


"""
Problema 1

Observa como las versiones para el calculo del factorial, con while y for,
modifican la valiable a. Esto no siempre es deseable, pues el calcular un
valor a partir de una variable no dberia hacer perder el valor original de
la misma.
Reescribe ambos programas para evitar esto.
 
"""

a = 5
acc = a
for f in range(2,a):
    acc*= f
print(a,acc)


a = 4
b = a
acc = 1 
while b > 1:
    acc *= b
    b-= 1
print(acc, b, a)


"""
Problema 2

Escribe un programa que itere sobre la lista de nombres ['Pedro', 'Pablo',
'Judas', 'Juan'].Dentro del bucle, comprobara si el nombre es 'Judas'.texto
'es el culpable', sino, deberia escribir el nombre junto con el texto 'es 
inocente'
 
"""
l = ['Pedro', 'Pablo', 'Judas', 'Juan']

for n in l :
    if n == 'Judas':
        print(n, 'es el culpable')
    else:
        print(n,'es inocente')

"""
Problema 3

Modifica  el codigo para el caluclo de un numero primo usando la anidacion 
de bucles para obtener de forma automatica numeros primos menoras a 1000. 
aprovecha la opcion de usar else para mostrar solo los numeros primos.
 
"""

for num in range(1000):
    for div in range(2,num):
        if num % div == 0: 
            break
    else: 
        print(num)