# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:00:41 2023

@author: shama
"""

"""
Problema 1

Escriba un programa que pida su edad y la de su mejor amigo.El
programa mostrara en pantalla quien es el mayor de los 2.
 
"""
#Comparacion edad

edad1 = int(input("Cual es tu edad?"))
edad2 = int(input("Cual es la edad de tu mejor amigo?"))

if edad1 > edad2:
    diff = edad1 - edad2
    print("Eres mayor que tu amigo por ", diff, " anios")
else:
    print("Tu amigo es mayor que tu por ", diff, " anios")
    



"""
Problema 2

Realiza un programa que pida un numero entero al usuario y muestre los
siguientes 5 numeros justificados a la derecha.
"""
num = int(input("Introduce un numero entero: "))
print("Los 5 numeros siguientes son: ")
just= num+5
for i in range(5):
    num += 1
    print(str(num).rjust(just))
    

"""
Problema 3

Escribe un programa que calcule el area de un rectangulo a partir de la base
y la altura especificadas por el usuario mediante teclado. Muestra la salidad
utilizando los siguientes metodos:
    a. Paso de valores como parametros
    b. Concatenacion de cadenas de texto.
    c. Operador%
    d. Funcion str.format()
    e. F-strings.
    
"""

print("Programa para calcular el area de un rectangulo.")
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))
area = base*altura

# Salida mediante paso de valores como parametros
print("El area del rectangulo de base ", base," y altura ", altura, " es: ", area)

# Salida mediante paso de valores como parametros
print("El area del rectangulo de base ", base," y altura ", altura, " es: ", area)

# Salida mediante paso de valores como parametros
print("El area del rectangulo de base ", base," y altura ", altura, " es: ", area)

# Salida mediante paso de valores como parametros
print("El area del rectangulo de base ", base," y altura ", altura, " es: ", area)

# Salida mediante paso de valores como parametros
print("El area del rectangulo de base ", base," y altura ", altura, " es: ", area)