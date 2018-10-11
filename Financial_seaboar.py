# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 00:17:01 2018

@author: DELL
"""

#para crear dataframes s neceista llamar a la libreria pandas 

import pandas as pd

datos = open_csv("Movies1.csv")
df = pd.DataFrame(datos)
print (df)
