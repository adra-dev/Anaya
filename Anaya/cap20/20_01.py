# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:09:58 2023

@author: shama
"""

def enc_sim(msj, key=7):
    enc = bytearray()
    for b in msj:
        c = b ^ key
        enc.append(c)
    return enc

msj = bytearray("Me van a encriptar, ole", "utf-8")
msj = enc_sim(msj)
print(msj)
msj = enc_sim(msj)
print(msj.decode("utf-8"))