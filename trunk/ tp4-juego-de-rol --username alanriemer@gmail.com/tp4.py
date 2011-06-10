import random
class Criatura(object):
	"""Objeto donde se encuentran los atributos y habilidades de las criaturas"""
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase de las criaturas.
		precondiciones: Las 6 caracteristicas de la criatura deben ser numeros naturales, con el 0 incluido"""
		self.caracteristicas={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0}
		for clave in self.caracteristicas.keys():
                    tirar_dados=random.randrange(1,7)+random.randrange(1,7)+random.randrange(1,7)
                    self.caracteristicas[clave]=tirar_dados
		suma_caracteristicas=0
		for valor in self.caracteristicas.values():
                    suma_caracteristicas+=valor
		self.indicadores={"hp":suma_caracteristicas,"mp":self.caracteristicas["inteligencia"]+self.caracteristicas["sabiduria"],"xp":0}
	