import random
class Criatura(object):
	"""Objeto donde se encuentran los atributos y habilidades de las criaturas"""
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase de las criaturas.
		precondiciones: """
		self.caracteristicas={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0}
		for clave in self.caracteristicas.keys():
                    tirar_dados=random.randrange(1,7)+random.randrange(1,7)+random.randrange(1,7)
                    self.caracteristicas[clave]=tirar_dados
		suma_caracteristicas=0
		for valor in self.caracteristicas.values():
                    suma_caracteristicas+=valor
		self.indicadores={"hp":suma_caracteristicas,"mp":self.caracteristicas["inteligencia"]+self.caracteristicas["sabiduria"],"xp":0}
    self.nombre=None
		self.habilidades={}
	def obtener_estado(self):
                """Método que devuelve un diccionario con los atributos de la criatura y su estado"""
                estado_atributos={}
                for clave in self.caracteristicas.keys():
                        estado_atributos[clave]=self.caracteristicas[clave]
                for clave in self.indicadores.keys():
                        estado_atributos[clave]=self.indicadores[clave]
                return estado_atributos
                
                
class Big_Bang_Attack(object):
    """Modela la habilidad. Tiene los metodos __init__, obtener_costos, y obtener_consecuencias"""
    def __init__(self):
        """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
        self.nombre="Big Bang Attack"
        self.descripcion="El ataque Big Bang es un enorme rayo de energia con un increible poder de destrucción. La criatura extiende su mano hacia el enemigo y lanza el rayo"
        self.autor="Masello-Riemer"
    def obtener_costos(self):
        """Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad"""
        valores_minimos={"fuerza":7,"contextura":6,"destreza":5,"xp":4}
        return valores_minimos
    def obtener_consecuencias(self,origen,destino):
        """Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
        precondiciones: origen y destino deben ser del tipo criatura
        postcondiciones: devuelve dos diccionarios con valores negativos cuando se decrementan los atributos y positivos cuando se aumentan los atributos .Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
        valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
        mofificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
        for clave in valores_minimos.keys():
            if atributos_criatura.haskey(clave):
                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
                    return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
        modificaciones_criatura_destino={"fuerza"-1,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":1,"hp":-25,"mp":0}
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":3,"hp":0,"mp":-10}   
        return modificaciones_criatura_origen, modificaciones_criatura_destino

