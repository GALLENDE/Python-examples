#Lectura de archivos
#En este caso se va a crear una funcion

def creacion():
	archivo= open('Texto.txt','w')
	archivo.close()

def escribir():
	archivo = open("Texto.txt","a")
	archivo.write("Nombre:Chonis y Pollo \n")
	archivo.write("Edad:10 \n")
	archivo.close()

escribir()

x = 1

while x != 10:
	escribir()
	x = x + 1
a = 89
for x in range (1,10):
	escribir()


archivo = open("Texto.txt","r")
	