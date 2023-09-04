# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 12:52:35 2023

@author: shama
"""

import re 

regex_email_gmail_outlook = re.compile(
    '''
    [\w\d.+-]+          #Usuario
    @   #@
    (gmail|outlook)     #Domino gmail o dominio outlook
    \.com               #.com
    ''',
    re.X)

lista_candidatos = ["sandrap@gmail.com", "jjtr@hotmail.es","ltm@outlook.com", "maria_jm_23@gmai.com", "mtr@prueba.es"]

for candidato in lista_candidatos:
    match = re.search(regex_email_gmail_outlook, candidato)
    if match:
        print(candidato + "- Direccion de correo Valida")
    else:
        print(candidato + "- Direccion de correo invalida")



"""
Problema 1

Escriba un programa que permita comprobar si las fechas de una lista son validas o no. Para que una fecha sea valida 
debera tener la estructura dd/mm/aaaa, es decir, dos digitos para el dia, dos para el mes y 4 para el ano. Ademas,
aaaa debera se un valor comprendido entre 1900 y 2019.

"""

# ^patron$ coincide con la cadena exacta patron
# '28/10/1985' coincide con patron
# 'El dia 28/10/1985' no coincide con patron puesto que la cadena completa no es una fecha, sino que lafecha forma parte de ella

regex_fecha_valida = re.compile(
    '''
    ^                                     # Metacaracter ^ para asegurar que la fecha aparece al principio de la cadena
    (0[1-9]|[12][0-9]|3[01])              # Dia en formado dd
    /                                     # Barra /
    (0[1-9]|1[012])                       # Mes en formato mm
    /                                     # Barra /
    (19\d\d|20[0-1][09])                  # Anio en formato aaaa comprendido entre 1900 y 2000
    $                                     # Metacaracter $ para asegurar que la fecha aparece al final de la cadena
    '''
    ,
    re.X)

lista_fechas = ['22/03/1985', '0y/12/2000', '15/04/0985', '12/08/2019']

for fecha in lista_fechas:
    if re.search(regex_fecha_valida, fecha): #Si la fecha cumple el patron
        print(fecha, "es una fecha valida.")
    else:
        print(fecha, "no es una fecha valida.")


"""
Problema 2

Escribe una expresion regular que permita extraer todas las palabras que terminen en os o as o sus equivalentes en
mayuscula usando banderas.

"""

regex_palabras_os_as = re.compile(r'\w*os|\w*as', re.I)

cad = "Todos los dias estoy deseando leer un nuevo capitulo del libro."

lista_palabras_terminadas_os_as = re.findall(regex_palabras_os_as, cad)

print(lista_palabras_terminadas_os_as)

"""
Problema 3

Escribe un programa para reemplazar por telefono los numeros de telefono de los clientes de una compania que aparezcan
en un texto. los numeros de telefono de los clientes tienen el formato XXX-XXX-XXX(ej.640-321-895).

"""

#\d{3} indica que deben aparecer 3 numeros seguidos
regex_telefono = re.compile(r'\d{3}-\d{3}-\d{3}')

texto = '''
Cliente: Antonio Martinez - Contacto: 678-376-290\n
Cliente: Maria Perez - Contacto: 654-910-243\n
Cliente: Sara Merino - Contacto: 696-973-510\n
'''

texto_reemplazado = re.sub(regex_telefono, "telefono", texto)

print(texto_reemplazado)