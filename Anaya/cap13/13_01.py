# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:43:12 2023

@author: shama

El siguiente programa  lee valores desde el teclado  para crear una coleccion de contactos
bajo la forma de lista de diccionarios. Solo cuando se introducen valores no vacios, se
almacenan en el diccionario.

El numero total de contactos es indefinido y depende del usuario, al que se le 
pregunta si desea introducir mas contactos despues de cada uno de ellos.

"""

# estos son los datos que vamos a solicitar para cada contacto
campos = ('nombre', 'apellidos', 'email', 'telefono')

# esta lista contendra todos los contactos
contactos = [] 

# iniciamos la variable 'seguir'
seguir = 's'

# mientras el valor de seguir sea 's' o 'S' introducimos contactos 
while seguir in ('s', 'S'):
    
    # este diccionario almacena los valores de un contacto
    contacto = {}
    
    # con este bucle preguntamos campo a campo
    for campo in campos:
        valor = input(campo + ': ')
        
        # si el usuario introduce algo, se almacena
        if len(valor) > 0:
            contacto[campo] = valor
            
    # aniadimos el contacto a la lista
    contactos.append(contacto)
            
    # preguntamos si seguimos aniadiendo contactos
    seguir = input('Introducir otro contaco? s\n:')
            
# mostramos todos los contactos 
for contacto in contactos:
    
    for k,v in contacto.items():
        print(k + ': ' +v)
        
        #mostramos esto para facilitar la lectura 
        print('------')

'''
Aumenta el programa con el codigo necesario para calcular y mostrar el numero 
total de contactos almacenados y cuantos de ellos disponen de correo electronico.
'''
# Solucion 1 

contador = 0
for contacto in contactos:
    if 'email' in contacto:
        contador += 1
        
print(len(contactos), 'contactos en total')
print(contador, 'contactos tienen email')

# Solucion 2 usando comprension de listas

contador = len([c for c in contactos if 'email' in c])
print(len(contactos), 'contactos en total')
print(contador, 'contactos tienen email')


'''
Una vez introducidos los datos, que codigo de una sola linea serviria para 
asignar al primer contacto los mismo valores asociado al ultimo  
'''

contactos[0].update(contactos[-1])

'''
Escribe el codigo para mostrar los datos del usuario cuyo correo electronico 
haya sido introducido por teclado.Si no existe contacto alguno con ese correo 
electronico, se mostrara el mensaje <<No encontrado>>.
'''

email = input('Introduce el correo electronico del contacto a busar: ')
encontrado = False
for contacto in contactos:
    if email == contacto.get('email'):
        encontrado = True
        print('Encontrado:')
        for k,v in contacto.items():
            print(k + '->' +v)
        break
if not encontrado:
    print('No encontrado')
    
'''
Escribe un progama que calcule la frecuencia de aparicion de cada letra en 
una cadena.Por ejemplo, para la cadena "abracadabra" deberia mostrar:
    {'a':5, 'b':2, 'r':2, 'c':1, 'd':1}
'''

texto = 'abracadabra'

frecuencias = {}
for l in texto:
    frecuencias[l] = frecuencias.get(l, 0) + 1
    print(frecuencias)