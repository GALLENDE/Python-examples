#lectura de archivos

def leer():
	archivos = open ("Texto.txt","r")
	fila = archivos.readline()

	while fila != "":
		print (fila)
		fila = archivos.readline()
	archivos.close()


leer ()
