# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:57:52 2018

@author: DELL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

datos = pd.read_csv("Movies2.csv")
df= pd.DataFrame(datos)
x = df["Votes"].values
y = df ["Metascore"].values

print ("Valor máximo de votos: ", df["Votes"].max())

# generacion de arreglos
info = df[["Votes","Metascore"]].as_matrix()

X =np.array(list(zip(x,y)))
print (X)

KMeans = KMeans(n_clusters=2)
KMeans = KMeans.fit(X)
labels = KMeans.predict(X)
centroids=KMeans.cluster_centers_

colors =["n.","r.","c.","y.","b."]

for i in range (len(X)):
    print("Coordenada: ", X[i]," Label: ", labels[i])
    plt.plot(X[i][0],X[i][1], colors[labels[i]],markersize = 10)

plt.scatter(centroids[:,0],centroids[:,1],marker ="x",s=150,linewidths = 5, zorder=10)
plt.show()
