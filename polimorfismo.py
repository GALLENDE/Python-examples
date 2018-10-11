class uno():
	def accion(self ):
		print ("Primera accion")

class dos():
	def accion(self):
		print("Segunda accion")


def funcion (polimorfismo):
	polimorfismo.accion()

ejemplo1 =uno ()
ejemplo2 =dos ()

funcion(ejemplo1)