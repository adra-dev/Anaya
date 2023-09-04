# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:04:21 2023

@author: shama

La funcion siguiente formatea_nombre() pasa a mayusculas la primera letra 
de cada componenete de un nombre completo. Por ejemplo, la cadena 
"antonio flores" pasaria a ser "Antonio Flores ".

def formatea_nombre(nombre):
    return " ".join([x[0].upper() + x[1:] for x in nombre.split()])

"""

import unittest

def formatea_nombre(nombre):
    return " ".join([x[0].upper() + x[1:] for x in nombre.split()])
    
class Test(unittest.TestCase):
    
    def test_nombre_apellido(self):
        self.assertEqual(formatea_nombre('theon greyjoy'), 'Theon Greyjoy')
    
    def test_nombre_2apellido(self):
        self.assertEqual(formatea_nombre('antonio munoz molina'), 'Antonio Munoz Molina')
        
    def test_puntos(self):
        self.assertEqual(formatea_nombre('ursula k. le guin'), 'Ursula K. Le Guin')
        
    def test_nombre_castizo(self):
        self.assertEqual(formatea_nombre('calderon de la barca'), 'Calderon de la Barca')
        
    def test_nombre_guion(self):
        self.assertEqual(formatea_nombre('alberto vazquez-figueroa'), 'Alberto Vazquez-Figueroa')
        
if __name__ == '__main__':
    unittest.main()
    
