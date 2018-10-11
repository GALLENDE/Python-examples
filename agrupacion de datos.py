# -*- coding: utf-8 -*-
#-*- coding: latin1 -*-


"""
Created on Tue Oct  9 00:17:01 2018

@author: DELL
"""

#para crear dataframes s neceista llamar a la libreria pandas 

import pandas as pd

datos = pd.read_csv("Movies2.csv")
df = pd.DataFrame(datos)

#Obtener  el maximo de Runtime y darlo en horas de la pelicula que dure más
Duration =  df["Runtime (Minutes)"].max()/60
peli = df.get_value(df["Runtime (Minutes)"].idxmax(),"Title")   
print ("La pelicula que dura más es : ", peli,"  ",round(Duration,2) ," hrs")

#Comparacion de votos entre generos 

df1 = df.groupby(["Genre"])[["Votes"]].sum()
print ("El genero que le gusta más a las personas es: ")
likes = df.groupby(["Genre"])[["Votes"]].sum()
print (likes["Votes"].idxmax(), end = "")
print(" con: ",likes["Votes"].max(), "likes")
print ("¿Cuál es el promedio que se gasta por director?")
df2 = df.groupby(["Director"])[["Revenue (Millions)"]].mean()
print ("¿Cuál es el genero  que gasta más dinero?")
money = df.groupby(["Genre"])[["Revenue (Millions)"]].sum()
print ("El monto es: ",money)
print ("\n" * 2)
print("el genero es: ",money ["Revenue (Millions)"].idxmax(), " con:", money["Revenue (Millions)"].max())
print ("¿Cuál es el actor principal que trae más ganancias?")
actor = df.groupby(["Actors"])[["Revenue (Millions)"]].sum()
print ("El Actor que trae más ganacias es: ", actor["Revenue (Millions)"].idxmax())
print ("\n" * 2)
