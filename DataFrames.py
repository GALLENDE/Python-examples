# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 00:17:01 2018

@author: DELL
"""

#para crear dataframes s neceista llamar a la libreria pandas 

import pandas as pd

datos = {"Nombre":["gilberto","gabriela","turbo","pollo"],
         "calificaciones":["90","100","60","0"],
         "deportes":["mma","natación","pelota","N/A"],
         "materias":["calculo","inglés","Educacion perruna","N/A"]}

#creacion del Dataframe

df = pd.DataFrame(datos)

print (df )
print ('\n' * 2)

#Datos no validos



