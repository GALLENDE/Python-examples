#Definici+on de tuplas

uno = (10, 20,30,40, "yoney")

# son inmutables no se pueden cambiar

for indice in uno:
	print (indice) 

indice = 0

while indice < len(uno):
	print (uno[indice])
	indice	= indice + 1