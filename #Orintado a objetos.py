#Orintado a objetos
class mascota:
#contructor para definir un constructor se utiliza lo siguinte
	def __init__(self, name, edge, tall):
		self.nombre = name
		self.edad = edge
		self.altura = tall

	def correr(self, firts):
		return self.nombre + " corre " + firts


perro = mascota("Perrin", 6,.30)
gato =  mascota("Bichi", 2,.15)

print("La mascota se llama:", perro.nombre)
print("la mascota se llama: ", gato.nombre)

print(perro.correr("rapido"))

print(perro)