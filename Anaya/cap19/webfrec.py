# -*- coding: utf-8 -*-
"""
Created on Sat May  6 19:01:22 2023

@author: shama
"""

import requests
import html2text
import re

def descargar_pagina(url):
    """

    Parameters
    ----------
    url : TYPE
        Lee una pagina web y la convierte en texto plano..

    Returns
    -------
    contenido de la pagina web en texto

    """
    
    try:
        page = requests.get(url)
        content = html2text.html2text(page.text)
    except Exception:
        pass
    return content

def contar_palabras(texto):
    """
    Calcula la fecuencia de aparicion de cada palabra en un texto y genera una
    lista de pares(palaba, frecuencia) ordenada de mayor a menor frecuencia.
    """
    frec = {}
    texto = re.sub('[^\w\s]+', '', texto)  # eliminamos signos de puntuacion
    for w in texto.lower().split():
        if len(w) > 3:
            frec[w] = frec.get(w, 0) + 1
    frec_sorted = sorted(frec.items(), key=lambda x: x[1], reverse=True)
        
    return frec_sorted