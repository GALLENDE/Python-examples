# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 22:27:41 2018

@author: DELL
"""


def escribir():
	archivo = open("Texto.txt","a")
	archivo.write("Nombre:Chonis y Pollo \n")
	archivo.write("Edad:10 \n")


escribir()

x = 1

while x != 10:
	escribir()
	x = x + 1
a = 89
for x in range (1,10):
	escribir()
