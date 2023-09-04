# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 18:07:58 2023

@author: shama
"""

"""
Problema 1

Mi coche gasta 5,5 litros cada 100 km y mi trabajo se encuentra a 15 kilometros 
de casa, Cuanto me gastare en gasolina en 20 dias laborales si el precio es de 1.12$/l?
 
"""

#Problema1

distancia = 2*15*20
litros = distancia/100*5.5
gasto= litros*1.12

print("En 20 dias laborales tu consumo de gasolina es $",gasto)

"""
Problema 2

En enero del anio actual tenia una cuenta con 3000$.Si cobro 1100$ mensuales y tengo unos 
gastos fijos al mes de 435$, a cuanto ascienden mis gastos extra mensuales si a final de
anio mi cuenta tiene un total de 6000$?
 
"""

#Problema2

saldo_inicial = 3000
salario_mensual =  1100
gastos_fijos_mensuales = 435
saldo_final = 6000

gastos_extra = saldo_inicial + salario_mensual *12 - gastos_fijos_mensuales *12 - saldo_final

gastos_extra_mensuales = gastos_extra/12

print("Tus gastos extra mensuales son de $", gastos_extra_mensuales)

"""
Problema 3

Tengo $50 para comprar una camisa, si la camisa cuesta $35 y tiene un descuento del 10%,
cuanto dinero tendre despues de comprar la camisa?
 
"""

#Problema3

efectivo_inicial = 50
precio_camisa =  35
descuento = 10
precio_final_camisa = precio_camisa - (precio_camisa*10/100)
efectivo_final = efectivo_inicial - precio_final_camisa

print("El dinero sobrante es de $", efectivo_final)