# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 22:07:47 2023

@author: shama

Ejercicios capitulo 15

El siguiente codigo tiene una funcion cifrar() que toma una cadena, letra a
letra, obtiene su codigo ASCII y le suma un valor, para convertirla de nuevo
en un caracter y generar una cadena cifrada. Esto se conoce como <<metodo
de encriptacion Cesar>>. Implementa la funcion descifrar() para que el codigo
principal funcione correctamente:
    
"""

def cifrar(mensaje):
    desp = 4
    cif = "".join([chr(ord(c)+desp) for c in mensaje])
    return cif


### implementa aqui la funcion descifrar

def descifrar(mensaje):
    desp = 4
    desc = "".join([chr(ord(c)-desp) for c in mensaje])
    return desc 


mensaje = "tomate"
print('Original:', mensaje)
cifrado = cifrar(mensaje)
print('Cifrado:', cifrado)
descifrado = descifrar(mensaje)
print('Descifrado:', descifrado)



'''
El siguiente codigo implementa parcialmente el <<algoritmo de la burbuja>>
para ordenar los elementos de una lista. Aniade una funcion anidada en 
ordenar(), denominada intercambia(), que acepte como parametros tres 
argumentos: una lista y dos valores de posicion. La funcion debe modificar
la lista intercambiandolos valores de esas posiciones.
'''

def ordenar(l):
    ###Implementa aqui la funcion intercambia()
    def intercambia(l, a, b):
        x = l[a]
        l[a] = l[b]
        l[b] = x
    
    for i in range(len(l) -1,1,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                intercambia(l, j, j+1)
                
l = [7, 3, 9, 5, 4, 2, 8, 10]
ordenar(l)
print(l)


'''
Dada esta cabecera de la funcion def nuevo_pedido(producto, precio, 
descuento=0), determina cuales son llamada validas entre las propuestas.

a. nuevo_pedido('probeta', 5, 0.25)                                             Correcto.
b. nuevo_pedido()                                                               Incorrecto. los do primeros parametros son obligatorios
c. nuevo_pedido('libro')                                                        Incorrecto. 
d. nuevo_pedido('lupa', 12)                                                     Correcto.
e. nuevo_pedido(producto='pinzas', 10)                                          Incorrecto.
f. nuevo_pedido(producto='lazer', precio=25)                                    Correcto.
g. nuevo_pedido(producto='telescopio', descuento=0.2, precio=25)                Correcto.
h. pedido = ('laptop', 1200, 0.6)                                               Incorrecto
i. nuevo_pedido(pedido)                                                         Incorrecto.
j. pedido={'producto': 'calculadora', 'valor': 19.99, 'descuento': 0}
    nuevo_pedido(**pedido) 

'''

'''
Escribe, usando una funcion lambda y la funcion map(), una linea de codigo 
a mayuscula la primera letra de cada elemento en la lista siguiente:
['stark', 'lannister', 'bolton', 'greyjoy', 'targaryen']

'''

l = ['stark', 'lannister', 'bolton', 'greyjoy', 'targaryen']
print(list(map(lambda x: x[0].upper() + x[1:], l)))