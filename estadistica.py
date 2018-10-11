# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:57:25 2018

@author: DELL
"""
import pandas as pd
import numpy as np

datos = pd.read_csv("ATP.csv",encoding = "ISO-8859-1")
print(datos.info())
print(datos.head())
nuevo = pd.DataFrame(datos)
print (nuevo)

#Se remplazan los nullos por el cero
nuevo = nuevo.replace(np.nan,"0")
print ("***Impresion sin NAN****")
print(nuevo.info())
print ("\n" * 5)
print ("****Estadisticas sin NAN")
print (nuevo.describe())
print ("\n" * 5)
print ("****Estadisticas con NAN")
print (nuevo.describe(include=[np.number]))

nuevo = nuevo.replace("N/A","0")
nuevo = nuevo.replace("NR","0")
print ("******Estadisticas sin NA o NR****")
print (nuevo.describe())
print (list(nuevo))
print ("\n"*5)
nuevo['Wsets'] = nuevo.Wsets.astype(int)
nuevo['WRank'] = nuevo.WRank.astype(int)
print ("Estadisticas de Ranckin y Sets")
print (nuevo.describe())
# Eliminar filas que tienen NAN

datos.dropna(how = 'any', inplace = True)
print (datos.head())
 