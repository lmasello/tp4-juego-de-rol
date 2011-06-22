import random
class Criatura(object):
	"""Objeto donde se encuentran los atributos y habilidades de las criaturas. Tiene los metodos: __init__, obtener_estado, aplicar_consecuencias, obtenerhabilidades"""
	def __init__(self):
                 """Metodo constructor de la clase. Crea la instancia de la clase de las criaturas. Se inicializan las caracteristicas y los indicadores en 0. Para cada caracteristica, se tiran 3 dados y la suma de estas 3 tiradas sera el puntaje inicial. Los puntos de hp seran la suma de todas las habilidades, mientras que los puntos de magia sera la suma de inteligencia y sabiduria"""
                 self.caracteristicas={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0}
                 for clave in self.caracteristicas.keys():
                         tirar_dados=random.randrange(1,7)+random.randrange(1,7)+random.randrange(1,7)
                         self.caracteristicas[clave]=tirar_dados
                 suma_caracteristicas=0
                 for valor in self.caracteristicas.values():
                         suma_caracteristicas+=valor
                 self.indicadores={"hp":suma_caracteristicas,"mp":self.caracteristicas["inteligencia"]+self.caracteristicas["sabiduria"],"xp":0}
                 self.nombre=None

	def obtener_estado(self):
                """Metodo que devuelve un diccionario con los atributos de la criatura y su estado
                precondiciones: Los diccionarios no deben estar vacios.
                postcondiciones: Devuelve diccionario con los atributos de la criatura"""
                estado_atributos={}
                for clave in self.caracteristicas.keys():
                        estado_atributos[clave]=self.caracteristicas[clave]
                for clave in self.indicadores.keys():
                        estado_atributos[clave]=self.indicadores[clave]
                return estado_atributos

        def aplicar_consecuencias(self, consecuencias):
                """Aplica las consecuencias a los atributos de la criatura al recibir ataque o realizar ataque.
                precondiciones: Consecuencias debe ser un diccionario
                postcondiciones: Realiza una transformacion en los indicadores y en las caracteristicas de la criatura"""
                if isinstance(consecuencias, dict):
                    for clave in consecuencias.keys():
                            if clave in self.indicadores:
                                    self.indicadores[clave]=self.indicadores[clave]+consecuencias[clave]
                            elif clave in self.caracteristicas:
                                    self.caracteristicas[clave]=self.caracteristicas[clave]+consecuencias[clave]
                else:
                    raise ValueError("consecuencias debe ser del tipo dict")
                
        def obtenerhabilidades(self):
                """Metodo que devuelve diccionario con las habilidades de la criatura.
                Las claves son el nombre de la habilidad y los valores son la instancia de la clase correspondiente.
                postcondiciones: Devuelve un diccionario con las 3 habilidades a usar. Dicho diccionario tiene como claves al nombre de la habilidad y como valor a dicho objeto """
                habilidades_totales={"Big_Bang_Attack":Big_Bang_Attack(),"Psicoataque":Psicoataque(),"Chupacabras":Chupacabras(),"Golpe_martillo":Golpe_martillo(),"Ataque_wachenhausen":Ataque_wachenhausen(),"Fatality":Fatality(),"Furia_de_Ares":Furia_de_Ares(),"Posion":Posion(),"Jugo_de_trebol":Jugo_de_trebol()}
                habilidades_a_usar={} #Diccionario que contendr� las 3 habilidades de la criatura
                numeros_usados=[] #Lista de n�meros aleatorios
                nombre_habilidades=habilidades_totales.keys() #Lista con los nombres de habilidades
                while len(numeros_usados)<3:
                        numero_aleatorio=random.randrange(0,10)
			if numero_aleatorio not numeros_usados:
                                habilidad=nombre_habilidades[numero_aleatorio]
				habilidades_a_usar[habilidad]=habilidades_totales[habilidad]
				numeros_usados.append(numero_aleatorio)
                return  habilidades_a_usar

                        

class Golpe_martillo(object):
	"""Modela la habilidad. Posee los metodos: __init__, obtener_costos, obtener_consecuencias"""
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
                self.nombre="Golpe martillo"
                self.descripcion="Golpe de puÃ±o Ã¡gil y poderoso"
                self.autor="Riemer - Masello"
        def obtener_costos(self):
                """Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
                costos={"fuerza":8, "contextura":5, "destreza":6}
                return costos

        def obtener_consecuencias(self, origen, destino):
                """Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino.
		precondiciones: origen y destino deben ser del tipo criatura
	        postcondiciones: devuelve dos diccionarios con valores negativos cuando se decrementan los atributos y positivos cuando se aumentan los atributos .Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
                if isinstance (origen, Criatura) and isinstance (destino, Criatura):
			valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
			atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
	                modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
			for clave in valores_minimos.keys():
				if atributos_criatura.has_key(clave):
					if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
						return modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
			modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":-1, "destreza":-1, "carisma":0,"sabiduria":0,"xp":3,"hp":-30,"mp":0}
	                modificaciones_criatura_origen={"fuerza":1,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":5,"hp":0,"mp":0}
		        return modificaciones_criatura_origen, modificaciones_criatura_destino
                else:
			raise ValueError ("origen y destino deben ser del tipo Criatura")
		    
class Ataque_wachenhausen(object):
	"""Modela la habilidad. Posee los metodos: __init__, obtener_costos, obtener_consecuencias"""
        def __init__(self):
	        """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
                self.nombre="Ataque_wachenhausen"
                self.descripcion="Utilizado por aquellas criaturas con un grado de inteligencia notable. El Ataque_wachenhausen incorpora a la criatura una determiada inteligencia y la posibilidad de usar un ataque utilizado con la telepatia para daÃ±ar al oponente"
                self.autor="Riemer-Masello"
        def obtenercostos(self):
                """Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
                costos={"inteligencia":7, "destreza":6, "carisma":6, "sabiduria":7, "mp":10}
                return costos
        def obtener_consecuencias(self, origen, destino):
                """Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino.
	        precondiciones: origen y destino deben ser del tipo criatura
	        postcondiciones: devuelve dos diccionarios con valores negativos cuando se decrementan los atributos y positivos cuando se aumentan los atributos .Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
                if isinstance (origen, Criatura) and isinstance (destino, Criatura):
			valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
	                atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
			modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
			for clave in valores_minimos.keys():
				if atributos_criatura.has_key(clave):
					if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
						return modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
	          #Si la criatura cumple con los requisitos necesarios, se procede
			modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":-1, "destreza":0, "carisma":-1,"sabiduria":0,"xp":2,"hp":-25,"mp":0}
	                modificaciones_criatura_origen={"fuerza":0,"inteligencia":6,"contextura":0, "destreza":0, "carisma":0,"sabiduria":3,"xp":4,"hp":0,"mp":10}
		        return modificaciones_criatura_origen, modificaciones_criatura_destino
                else:
			raise ValueError("origen y destino deben ser del tipo Criatura")
		    
class Fatality(object):
	"""Modela la habilidad. Posee los metodos: __init__, obtener_costos, obtener_consecuencias"""
        def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
                self.nombre="Fatality"
                self.descripcion="Fatality es una habilidad que solo podran acceder aquellas criaturas que posean un grado de magia y de experiencia equivalente a 40. Ya que es u ataque que requiere de una energia muy elevada. Y solo aquellas criaturas que logren obtener ea cantidad de puntos podran utilizarla"
                self.autor="Riemer-Masello"
        def obtenercostos(self):
                """Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
                costos={"mp":40,"xp":40}
                return costos
        def obtener_consecuencias(self, origen, destino):
                """Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino.
	        precondiciones: origen y destino deben ser del tipo criatura
	        postcondiciones: devuelve dos diccionarios con valores negativos cuando se decrementan los atributos y positivos cuando se aumentan los atributos .Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
                if isinstance (origen, Criatura) and isinstance (destino, Criatura):
			valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
	                atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
			modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
	                for clave in valores_minimos.keys():
				if atributos_criatura.has_key(clave):
		                        if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
				                return modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
	        #Si la criatura cumple con los requisitos necesarios, se procede
		        modificaciones_criatura_destino={"fuerza":-6,"inteligencia":-6,"contextura":-6, "destreza":-6, "carisma":-6,"sabiduria":-6,"xp":2,"hp":-80,"mp":0}
			modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":16,"hp":0,"mp":-40}   
	                return modificaciones_criatura_origen, modificaciones_criatura_destino
                else:
		        raise ValueError("origen y destino deben sert del tipo Criatura")
		    
class Big_Bang_Attack(object):
	"""Modela la habilidad. Tiene los metodos __init__, obtener_costos, y obtener_consecuencias"""
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	        self.nombre="Big Bang Attack"
	        self.descripcion="El ataque Big Bang es un enorme rayo de energia con un increible poder de destrucciÃÂ³n. La criatura extiende su mano hacia el enemigo y lanza el rayo"
		self.autor="Masello-Riemer"
	def obtener_costos(self):
		"""Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
	        valores_minimos={"fuerza":7,"contextura":6,"destreza":5,"xp":8}
		return valores_minimos
	def obtener_consecuencias(self,origen,destino):
		"""Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
	        precondiciones: origen y destino deben ser del tipo criatura
	        postcondiciones: devuelve dos diccionarios con valores negativos cuando se decrementan los atributos y positivos cuando se aumentan los atributos .Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
		if isinstance (origen, Criatura) and isinstance (final, Criatura):
		        valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
		        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        for clave in valores_minimos.keys():
				if atributos_criatura.has_key(clave):
			                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
				                return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
	        #Si la criatura cumple con los requisitos necesarios, se procede
			modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":-1, "destreza":-1, "carisma":0,"sabiduria":0,"xp":2,"hp":-25,"mp":0}
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":4,"hp":0,"mp":-2}   
		        return modificaciones_criatura_origen, modificaciones_criatura_destino
	        else:
		        raise ValueError ("origen y destino deben ser del tipo Criatura")
		    
class Psicoataque(object):
	"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	        self.nombre="Psicoataque"
	        self.descripcion="El psicoataque es un ataque que utiliza la fuerza del oponente y la utiliza para causarle daÃ±os psicologicos. Este ataque lo podran utilizar aquellas criaturas que posean un elevado grado de inteligencia"
	        self.autor="Masello-Riemer"
	def obtener_costos(self):
		"""Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
	        valores_minimos={"inteligencia":6,"sabiduria":6,"xp":9,"mp":8}
		return valores_minimos
	def obtener_consecuencias(self,origen,destino):
		"""Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
	        precondiciones: origen y destino deben ser del tipo criatura
		postcondiciones: devuelve dos diccionarios.Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
		if isinstance (origen, Criatura) and isinstance (destino, Criatura):
		        valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
		        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        for clave in valores_minimos.keys():
			            if atributos_criatura.has_key(clave):
				                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
					                    return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":-2,"contextura":0, "destreza":0, "carisma":0,"sabiduria":-2,"xp":2,"hp":-20,"mp":-2}
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":5,"contextura":0, "destreza":0, "carisma":0,"sabiduria":2,"xp":4,"hp":0,"mp":15}   
		        return modificaciones_criatura_origen, modificaciones_criatura_destino
		else:
		        raise ValueError ("origen y destino deben ser del tipo Criatura")
		    
class Chupacabras(object):
	"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	        self.nombre="chupacabras"
		self.descripcion="En este ataque la criatura utiliza un metodo de seduccion otorgado por Afrodita (diosa griega) para seducir al oponente y asi lograr paralizarlo. Al paralizar a su oponente procede a chuparle parte de su vida, transfiriendola a su propio cuerpo"
	        self.autor="Masello-Riemer"
	def obtener_costos(self):
		"""Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
	        valores_minimos={"destreza":5,"carisma":6,"mp":5}
		return valores_minimos
	def obtener_consecuencias(self,origen,destino):
		"""Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
	        precondiciones: origen y destino deben ser del tipo criatura
		postcondiciones: devuelve dos diccionarios.Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
	        if isinstance (origen, Criatura) and isinstance (destino, Criatura):
			valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
		        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        for clave in valores_minimos.keys():
			        if atributos_criatura.has_key(clave):
			                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
				                return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
		        modificaciones_criatura_destino={"fuerza":-1,"inteligencia":0,"contextura":-1, "destreza":0, "carisma":0,"sabiduria":0,"xp":1,"hp":-15,"mp":0}
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":1, "destreza":3,"xp":2,"hp":15,"mp":2}   
		        return modificaciones_criatura_origen, modificaciones_criatura_destino
	        else:
			raise ValueError ("origen y destino deben ser del tipo Criatura")
		    
class Furia_de_Ares(object):
	"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	        self.nombre="Furia de Ares"
		self.descripcion="En este ataque la criatura invoca al dios griego de la guerra, el cual desatara una gran furia, quitandole fuerza y vida al oponente. La criatura que lo invoca debe tener un nivel elevado de magia"
	        self.autor="Masello-Riemer"
	def obtener_costos(self):
		"""Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
	        valores_minimos={"sabiduria":5,"xp":12,"mp":8}
		return valores_minimos
	def obtener_consecuencias(self,origen,destino):
		"""Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
	        precondiciones: origen y destino deben ser del tipo criatura
		postcondiciones: devuelve dos diccionarios.Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
	        if isinstance (origen, Criatura) and isinstance (destino, Criatura):
			valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
		        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        for clave in valores_minimos.keys():
			        if atributos_criatura.has_key(clave):
			                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
				                return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
		        modificaciones_criatura_destino={"fuerza":-5,"inteligencia":0,"contextura":-1, "destreza":0, "carisma":0,"sabiduria":0,"xp":3,"hp":-35,"mp":0}
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":5,"xp":5,"hp":0,"mp":-8}   
		        return modificaciones_criatura_origen, modificaciones_criatura_destino
	        else:
			raise ValueError ("origen y destino deben ser del tipo Criatura")
    
class Posion(object):
	"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	        self.nombre="Posion"
		self.descripcion="Esta habilidad le permite al personaje aumentar puntos de vida"
	        self.autor="Masello-Riemer"
	def obtener_costos(self):
		"""Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
	        valores_minimos={"xp":8,"mp":8}
		return valores_minimos
	def obtener_consecuencias(self,origen,destino):
		"""Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
	        precondiciones: origen y destino deben ser del tipo criatura
		postcondiciones: devuelve dos diccionarios.Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
	        if isinstance (origen, Criatura) and isinstance (destino, Criatura):
			valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
		        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        for clave in valores_minimos.keys():
			        if atributos_criatura.has_key(clave):
			                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
			                        return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":40,"mp":0}   
		        return modificaciones_criatura_origen, modificaciones_criatura_destino
	        else:
			raise ValueError ("origen y destino deben ser del tipo Criatura")
		    
class Jugo_de_trebol(object):
	"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	def __init__(self):
		"""Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
	        self.nombre="Jugo_de_trebol"
		self.descripcion="Esta habilidad le permite al personaje aumentar puntos de magia"
	        self.autor="Masello-Riemer"
	def obtener_costos(self):
		"""Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad.
                postcondiciones: Devuelve diccionario, cuyas claves contienen atributos de la criatura, y cuyo valor es el minimo necesario de dicho atributo para poder utilizar la habilidad"""
	        valores_minimos={"xp":8,"hp":40}
		return valores_minimos
	def obtener_consecuencias(self,origen,destino):
		"""Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
	        precondiciones: origen y destino deben ser del tipo criatura
		postcondiciones: devuelve dos diccionarios.Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
	        if isinstance (origen, Criatura) and isinstance (destino, Criatura):
			valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
		        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
			modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        for clave in valores_minimos.keys():
				if atributos_criatura.has_key(clave):
				        if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
					        return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
		        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
		        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":40}
		        return modificaciones_criatura_origen, modificaciones_criatura_destino
	        else:
			raise ValueError ("origen y destino deben ser del tipo Criatura")



class Jugador (object):
	"""Modela a jugador humano. Tiene los metodos: __init__, agregar_criatura, eliminar_criatura, elegir_criatura"""
	def __init__(self):
		"""Metodo constructor de la clase. Contiene una lista con las criaturas que poseee el jugador, los puntos del jugador(que aumentaran cada vez que el jugador gane una batalla)y el nombre, descripcion y autor del jugador"""
	        self.criaturas=[]
		self.puntos=0
	        self.nombre=None
		self.descripcion=None
	        self.autor=None
	def agregar_criatura(self,criatura):
		"""agrega una criatura de la lista de criaturas del jugador.
	        precondiciones: criatura debe ser del tipo Criatura y el nombre de dicha criatura no lo debe poseer ninguna otra"""
		if isinstance (criatura,Criatura):
		        if self.criaturas==[]:  #Caso en que sea la primera criatura que se agrega.
				nombre_criatura=raw_input("Ingrese el nombre de su criatura:")
		                criatura.nombre=nombre_criatura
			        self.criaturas.append(criatura)
		        else:
			        nombres_criaturas=[]
		                for creature in self.criaturas:        #Se itera en las criaturas del jugador, para obtener los nombres de aquellas y asi verificar que el jugador no ingresa un nombre que posea otra criatura
					nombres_criaturas.append(creature.nombre)
				nombre_criatura=raw_input("Ingrese el nombre de su criatura:")
		                while nombre_criatura in nombres_criaturas:   #No lo deja continuar hasta que no ingrese un nombre valido
			                print "Ya posee una criatura con ese nombre"
			                nombre_criatura=raw_input("Ingrese nuevamente el nombre de su criatura:")
		                criatura.nombre=nombre_criatura
		                self.criaturas.append(criatura)
		else:
		        raise ValueError ("criatura debe ser del tipo Criatura")

	def eliminar_criatura(self,criatura):
		"""Elimina una criatura de la lista de criaturas del jugador.
	        precondiciones: criatura debe ser del tipo Criatura y la lista de criaturas debe contener a dicha criatura"""
		try:
		        if isinstace (criatura,Criatura):
				self.criaturas.remove(criatura)
	                else:
			        raise ValueError ("criatura debe ser del tipo Criatura")
		except ValueError:
		        print "criatura debe ser del tipo criatura"
	        except:
			print "La criatura debe estar en la lista de criaturas"

	def elegir_criatura(self):
		"""Metodo que devuelve la proxima criatura a utilizar en combate, o bien None si no tiene criaturas disponibles. Se le pregunta al usuario que criatura desea utilizar.
	        postcondiciones: Devuelve la criatura a utilizar obien None si no tiene criaturas"""
		if self.criaturas==[]:  #Si la lista de criaturas es vacia devuelve None
		        return None
	        nombres_criaturas=[]
		for criatura in self.criaturas:        #Se itera en las criaturas del jugador, para obtener los nombres de aquellas y asi verificar si el nombre de la criatura que ingresa el usuario es de alguna criatura
		        nombres_criaturas.append(criatura.nombre)
		print nombres_criaturas
      print self.nombre
	        criatura_elegida=raw_input("Que criatura desea elegir para el combate?:")
		while criatura_elegida not in nombres_criaturas:     #Caso en que el usuario ingresa incorrectamente la criatura
	                print "El nombre de la criatura ingresada no se encuentra en su lista de criaturas"
		        print "Usted posee la/s siguiente/s criaturas:",nombres_criaturas
	                criatura_elegida=raw_input("Que criatura desea elegir para el combate?:")
        #Para devolver el objeto criatura elegida, se itera con las criaturas de la lista de las criaturas. Y se devuelve la que coincida con el nombre
	        for criatura in self.criaturas:
		        if criatura.nombre==criatura_elegida:
				return criatura      #Devuelve la criatura que posee el nombre indicado
	def elegir_accion(self,origen, destino):
		"""Devuelve el nombre de la habilidad a utilizar y la criatura destino de la habilidad.
	        precondiciones: origen y detino deben ser del tipo Criatura
		postcondiciones: La habilidad que devuelve debe ser objeto o bien None, si es que la criatura logra huir. El destino que devuelve es del tipo Criatura"""
		if isinstance (origen, Criatura) and isinstance(destino,Criatura):
			habilidades_criatura=origen.obtenerhabilidades()
			estado_criatura_origen=origen.obtener_estado() #Diccionario con atributos e indicadores de origen
		        hp_criatura_origen=estado_criatura_origen["hp"]
			print "Le toco pelear contra:", destino.nombre
		        print "Su monstruo es:", origen.nombre
			print "Sus habilidades son:", habilidades_criatura.keys()
			#Si tiene vida menor a 15 le pregunta si desea huir
			if hp_criatura_origen<15:
				opcion_huir=raw_input("Su criatura posee un hp menor a 15.Â¿Desea huir de la batalla?:").upper()
				while opcion_huir!="SI" or opcion_huir!="NO":  #No lo deja continuar si no ingrese si o no
					print "Ingrese si o no"
					opcion_huir=raw_input("Su criatura posee un hp menor a 15.Â¿Desea huir de la batalla?:").upper()
				if opcion_huir=="SI":    #Si el jugador elige huir. Huye. Sino, continua el metodo
					return None, destino
		        habilidad_elegida=raw_input("Ingrese la habilidad elegida:")
			while habilidad_elegida not in habilidades_criatura:
				print "Sus habilidades son:", habilidades_criatura.keys()
			        habilidad_elegida=raw_input("Ingrese la habilidad elegida:")
			return habilidad_elegida, destino
		else:
		        raise ValueError("origeny destino deben ser del tipo Criatura")

class Jugador_artificial_1(object):
	"""Modela a jugador de inteligencia artificial. Tiene los metodos: __init__, agregar_criatura, eliminar_criatura, elegir_criatura"""
	def __init__(self):
		"""Metodo constructor de la clase. Contiene una lista con las criaturas que poseee el jugador, los puntos del jugador(que aumentaran cada vez que el jugador gane una batalla)y el nombre, descripcion y autor del jugador"""
	        self.criaturas=[]
		self.puntos=0
	        self.nombre="Vegueta"
		self.descripcion="Vegueta es un jugador que elige las habilidades de forma aleatoria"
	        self.autor="Masello-Riemer"
	def agregar_criatura(self,criatura):       #Al no ser humano no le asigna nombre a la criatura
		"""agrega una criatura de la lista de criaturas del jugador.
	        precondiciones: criatura debe ser del tipo Criatura"""
		if isinstance (criatura, Criatura):
		        self.criaturas.append(criatura)
		else:
			raise ValueError ("criatura debe ser del tipo Criatura")
	def eliminar_criatura(self,criatura):
		"""Elimina una criatura de la lista de criaturas del jugador. 
		precondiciones: criatura debe ser del tipo Criatura y la lista de criaturas debe contener a dicha criatura"""
	        try:
			if isinstace (criatura,Criatura):
				self.criaturas.remove(criatura)
	                else:
				raise ValueError ("criatura debe ser del tipo Criatura")
	        except ValueError:
			print "criatura debe ser del tipo criatura"        
	        except:
			print "La criatura debe estar en la lista de criaturas"
	def elegir_criatura(self):
		"""Metodo que devuelve la proxima criatura a utilizar en combate. Al no ser humano y no tener chances de elegirla se devolvera la primera criatura de su lista de criaturas, o bien None si no tiene criaturas disponibles. Entendemos que la proxima criatura a utilizar en combate es la que se encuentra primera en la lista.
		postcondiciones: Devuelve un objeto del tipo Criatura"""
		if self.criaturas==[]:  #Si la lista de criaturas es vacia devuelve None
		        return None
	        return self.criaturas[0]   #Si hay elementos en la lista de criaturas devuelve el 1Âº elemento de dicha lista
	def elegir_accion(self,origen, destino):
		"""Devuelve el nombre de la habilidad a utilizar y la criatura destino de la habilidad. El jugador Vegueta elige aleatoriamente la accion a utilizar.
		precondiciones: origen y destino deben ser del tipo Criatura.
		postcondiciones: devuelve un objeto habilidad, o bien None en el caso de que huya y otro objeto de tipo Criatura"""
	        if isinstance (origen,Criatura) and isinstance(destino, Criatura):
		        habilidades_criatura=origen.obtenerhabilidades()     
			lista_habilidades=habilidades_criatura.keys()
		        numero_aleatorio=random.randrange(0,len(lista_habilidades))    #Se guarda en una variable un numero de rango (0 a long de la lista de habilidades)
		#Para la opcion huir
		        indicadores_de_criatura=origen.indicadores
			try:
		            valor_hp=indicadores_de_criatura["hp"]
		    #Si la vida es menor a 15 y el numero que sale de tirar los dados es 1 o 2, podra escapar
			    tirar_dados=random.randrange(1,7)
		            if valor_hp<=15 and tirar_dados==1 or valor_hp<=15 and tirar_dados==0:
				    return None, destino      #La criatura logra huir
			    return habilidades_criatura[lista_habilidades[numero_aleatorio]], destino     # Devuelve dos objetos: uno de tipo habilidad y otro de tipo Criatura
			except:
			        print "Hay error en el diccionario de la criatura"
		else:
			raise ValueError ("origen y destino deben ser del tipo Criatura")

                  
class Jugador_artificial_2(object):
	"""Modela a jugador de inteligencia artificial. Tiene los metodos: __init__, agregar_criatura, eliminar_criatura, elegir_criatura"""
	def __init__(self):
		"""Metodo constructor de la clase. Contiene una lista con las criaturas que poseee el jugador, los puntos del jugador(que aumentaran cada vez que el jugador gane una batalla)y el nombre, descripcion y autor del jugador"""
	        self.criaturas=[]
		self.puntos=0
	        self.nombre="Goku"
		self.descripcion="Jugador que posee un nivel de inteligencia superior. Esto le permitira decidir cual sera aquella habilidad mas conveniente a elegir"
	        self.autor="Masello-Riemer"
	def agregar_criatura(self,criatura):       #Al no ser humano no le asigna nombre a la criatura
		"""agrega una criatura de la lista de criaturas del jugador.
	        precondiciones: criatura debe ser del tipo Criatura"""
		if isinstance (criatura, Criatura):
			self.criaturas.append(criatura)
		else:
			raise ValueError ("criatura debe ser del tipo Criatura")
	def eliminar_criatura(self,criatura):
		"""Elimina una criatura de la lista de criaturas del jugador. Entendemos que la criatura a eliminar es la primera que se encuentra en la lista, ya que, al no tener posibilidades de elegirla, utiliza siempre la primera criatura de su lista de criaturas
	        precondiciones: criatura debe ser del tipo Criatura y la lista de criaturas debe contener a dicha criatura"""
		try:
			if isinstance (criatura,Criatura): #mirar que habia error d tipeado
				self.criaturas.remove(criatura)
	                else:
		                raise ValueError ("criatura debe ser del tipo Criatura")
	        except ValueError:
			print "criatura debe ser del tipo criatura"        
	        except:
		        print "La criatura debe estar en la lista de criaturas"
	def elegir_criatura(self):
		"""Metodo que devuelve la proxima criatura a utilizar en combate. Al no ser humano y no tener chances de elegirla se devolvera la primera criatura de su lista de criaturas, o bien None si no tiene criaturas disponibles. Entendemos que la proxima criatura a utilizar en combate es la que se encuentra primera en la lista
		postcondiciones: Devuelve un objeto del tipo Criatura"""
		if self.criaturas==[]:  #Si la lista de criaturas es vacia devuelve None
			return None
		return self.criaturas[0]   #Si hay elementos en la lista de criaturas devuelve el 1Âº elemento de dicha lista
	def elegir_accion(self,origen, destino):
		"""Devuelve el nombre de la habilidad a utilizar y la criatura destino de la habilidad. El jugador Goku podra elegir entre sus opciones mas convenientes a utilizar.
		precondiciones: origen y destino deben ser del tipo Criatura.
		postcondiciones: devuelve un objeto habilidad, o bien None en el caso de que huya y otro objeto de tipo Criatura"""
	        if isinstance (origen,Criatura) and isinstance(destino, Criatura):
		        estado_criatura=origen.obtener_estado() #Diccionario con atributos e indicadores de origen
			hp_origen=estado_criatura["hp"]
		        habilidades_criatura=origen.obtenerhabilidades() #Diccionario con habilidades de criatura origen
			posibles_habilidades_a_usar=habilidades_criatura.keys() #Lista con nombres de habilidades a usar        
			for habilidad in habilidades_criatura.values(): #Itera sobre los objetos habilidades del diccionario
				costos=habilidad.obtener_costos() #Costos de la habilidad
				for clave in costos: #Itera sobre las claves de los costos que son atributos e indicadores mÃ­nimos
					if estado_criatura[clave]<costos[clave]: #Verifica que tenga lo requerido para usar dicha habilidad
						posibles_habilidades_a_usar.remove(habilidad.nombre) #Si no alcanza ese atributo, borra esa opciÃ³n  
		        diccionario_habilidades_hp={} #Diccionario que tiene como claves el hp que quita y como valor nombres filtrados de habilidad
			for habilidad in posibles_habilidades_a_usar: #Itera sobre el nombre de las habilidades filtradas
				objeto_habilidad=habilidades_criatura[habilidad] #Busca la instancia de dicha habilidad
				(modificaciones_criatura_origen, modificaciones_criatura_destino)=objeto_habilidad.obtener_consecuencias()
			        if hp_origen<15: #Si tiene poca vida
			                if modificador_criatura_origen["hp"]>0: #Si dicha habilidad disponible le otorga vida, la elige
					        return habilidad, destino
				hp_absoluto=abs(modificaciones_criatura_destino["hp"]) #Valor en absoluto del HP que quita dicha habilidad
			        diccionario_habilidades_hp[hp_absoluto]=habilidad #Guarda el HP que quita, como clave, y como valor el nombre de habilidad
		        if hp_origen<15:#Si la vida es menor a 15 le permite huir
				return None, origen     #El jugador huye
		        lista_hp=diccionario_habilidades_hp.keys() #Lista con valores de HP que quitan las habilidades
			lista_hp.sort() #Ordena de menor a mayor
			mayor_hp=lista_hp[len(lista_hp)-1] #Guardo el mayor HP
			habilidad_elegida=diccionario_habilidades_hp[mayor_hp]
		        return habilidad_elegida, destino
		else:
			raise ValueError ("origen y destino deben ser del tipo Criatura")


#Motor del juego
# -*- coding: latin-1 -*-
import random
from habilidades import Golpe_martillo, Ataque_wachenhausen, Fatality, Big_Bang_Attack, Psicoataque, Chupacabras, Furia_de_Ares, Posion, Jugo_de_trebol
from jugadores import Jugador, Jugador_artificial_1, Jugador_artificial_2
from criatura import Criatura
import habilidades
import jugadores
import criatura

def menu():
    criatura1=Criatura()
    criatura2=Criatura()
    criatura3=Criatura()
    criatura4=Criatura()
    print "Bienvenido al juego de rol"
    print "1) Yo vs Computadora"
    print "2) Computadora vs Computadora"
    print "3) Yo vs otro jugador"
    opcion=raw_input("Ingrese su nÃºmero de opcion:")
    if opcion=="1":
        jugador1=Jugador()
        nombre=raw_input("Ingrese su nombre:")
        jugador1.nombre=nombre
        jugador2=Jugador_artificial_2()
        batalla(jugador1,jugador2)
    if opcion=="2":
        jugador1=Jugador_artificial_2()
        jugador2=Jugador_artificial_1()
        jugador1.agregar_criatura(criatura1)
        jugador1.agregar_criatura(criatura2)
        jugador2.agregar_criatura(criatura3)
        jugador2.agregar_criatura(criatura4)
        batalla(jugador1, jugador2)
    if opcion=="3": 
        jugador1=Jugador()
        nombre=raw_input("Ingrese nombre de jugador 1:")
        jugador1.nombre=nombre
        jugador2=Jugador()
        nombre=raw_input("Ingrese nombre de jugador 2:")
        jugador2.nombre=nombre
        print jugador1.nombre, "Ingrese el nombre de sus criaturas:"
        jugador1.agregar_criatura(criatura1) #Carga las criaturas del jugador 1
        jugador1.agregar_criatura(criatura2)
        print jugador2.nombre, "Ingrese el nombre de sus criaturas"
        jugador2.agregar_criatura(criatura3) #Carga las criaturas del jugador 2
        jugador2.agregar_criatura(criatura4)
        batalla(jugador1, jugador2)

def batalla(jugador1, jugador2):
    """FunciÃ³n que recibe dos jugadores, y crea la batalla entre sus monstruos"""
    while True: #Cicla hasta que se desee no jugar m�s
        if len(jugador1.criaturas)==0:
                print jugador1.nombre, "no tiene más criaturas, se le creará una nueva"
                criatura_nueva_1=Criatura()
                jugador1.agregar_criatura(criatura_nueva_1)
        if len(jugador2.criaturas)==0:
                print jugador2.nombre, "no tiene más criaturas, se le creará una nueva"
                criatura_nueva_2=Criatura()
                jugador2.agregar_criatura(criatura_nueva_2)
                
        criatura_elegida_1=jugador1.elegir_criatura() # El jugador 1, elije la criatura para luchar
        estado_criatura_jugador1=criatura_elegida_1.obtener_estado()
        indicadores_criatura_1=criatura_elegida_1.indicadores #Diccionario de indicadores de la criatura elegida del Jugador 1
        print estado_criatura_jugador1 # Le muestra el estado de dicha criatura
        
        criatura_elegida_2=jugador2.elegir_criatura() #El jugador 2, elije la criatura para luchar
        estado_criatura_jugador2=criatura_elegida_2.obtener_estado()
        indicadores_criatura_2=criatura_elegida_2.indicadores #Diccionario de indicadores de la criatura elegida del Jugador 2
        print estado_criatura_jugador2 # Le muestra el estado de la criatura
        
        while True: #Cicla hasta que una de las criaturas muera
                suma_contex_destreza_criatura_jug1=estado_criatura_jugador1["contextura"]+estado_criatura_jugador1["destreza"]
                suma_contex_destreza_criatura_jug2=estado_criatura_jugador2["contextura"]+estado_criatura_jugador2["destreza"]
        
                if suma_contex_destreza_criatura_jug1>suma_contex_destreza_criatura_jug2:    #Si la criatura del jugador 1 tiene una contextura y destreza cuya suma es mayor a la de la criatura del jugador 2, comienza el turno la criatura 1
                    #Ataca la criatura del jugador 1
                    accion_elegida_1, destino_1 =jugador1.elegir_accion(criatura_elegida_1, criatura_elegida_2) #Jugador 1 elije accion
                    diccionario_habilidades_1=criatura_elegida_1.obtenerhabilidades()#Guarda el diccionario de habilidades de dicha criatura del jugador 1
                    habilidad_elegida_1=diccionario_habilidades_1[accion_elegida_1] #Busca y guarda el OBJETO habilidad elegida por el jugador 1
                    (modificador_origen_1, modificador_destino_1)=habilidad_elegida_1.obtener_consecuencias(criatura_elegida_1, criatura_elegida_2) #Guarda las consecuencias de la habilidad elegida por jugador1
                    criatura_elegida_1.aplicar_consecuencias(modificador_origen_1) #Aplica las consecuencias del ataque que realizÃ³ el jugador 1, en su monstruo
                    criatura_elegida_1.aplicar_consecuencias(modificador_destino_2) #Aplica las consecuencias del ataque que realizÃ³ el jugador 1, en el destino
                    #Luego del estado se modifican los atributos de las criaturas, por lo dicho se cargan de nuevo los estados de la criatura atacada, para ver si perdio
                    estado_criatura_jugador2=criatura_elegida_2.obtener_estado()
                        #Si con el ataque mata a la criatura
                    if estado_criatura_jugador2["hp"]<=0:
                        #se le agrega un punto al jugador poseedor de la criatura triunfante
                        jugador1.puntos+=1
                        criatura_elegida_1.indicadores=indicadores_criatura_1 #Recupera su estado la criatura ganadora
                        #Se reestablecen los puntos de vida y magia con los que la criatura comenzo el combate. HACER
                        print "La batalla la ha ganado:",jugador1
                        jugador2.criaturas.remove(criatura_elegida_2)  #Borra a la criatura de la lista de criaturas del jugador
                        break  #Sale del ciclo
                #Si la criatura del jugador dos tiene mayores puntos de contextura y destreza comienza el turno el jugador 2
                else:
                    accion_elegida_2, destino_2 =jugador2.elegir_accion(criatura_elegida_2, criatura_elegida_1) #Jugador 2 elije accion
                    diccionario_habilidades_2=criatura_elegida_2.obtenerhabilidades() #Guarda el diccionario de habilidades de la criatura del jugador 2
                    habilidad_elegida_2=diccionario_habilidades_2[accion_elegida_2] #Busca y guarda el OBJETO habilidad elegida por el jugador 2
                    (modificador_origen_2, modificador_destino_2)=habilidad_elegida_2.obtener_consecuencias(criatura_elegida_2, criatura_elegida_1) #Guarda las consecuencias de la habilidad elegida por jugador2
                    criatura_elegida_2.aplicar_consecuencias(modificador_origen_2) #Aplica las consecuencias del ataque que realizÃ³ el jugador 2, en su monstruo
                    criatura_elegida_2.aplicar_consecuencias(modificador_destino_1) #Aplica las consecuencias del ataque que realizÃ³ el jugador 2, en el destino
                    estado_2=criatura_elegida_2.obtener_estado() #Diccionario de esto de la criatura del jugador 2
                    #Luego del estado se modifican los atributos de las criaturas, por lo dicho se cargan de nuevo los estados de la criatura atacada, para ver si perdio
                    estado_criatura_jugador1=criatura_elegida_1.obtener_estado()
                    #Si con el ataque mata a la criatura
                    if estado_criatura_jugador1["hp"]<=0:
                        #se le agrega un punto al jugador poseedor de la criatura triunfante
                        jugador2.puntos+=1
                        criatura_elegida_2.indicadores=indicadores_criatura_2 #Recupera su estado la criatura ganadora
                        #Se reestablecen los puntos de vida y magia con los que la criatura comenzo el combate. HACER
                        print "La batalla la ha ganado:",jugador2
                        jugador1.criaturas.remove(criatura_elegida_1)  #Borra a la criatura de la lista de criaturas del jugador
                        break  #Sale del ciclo        
                
                        


                        

                        

                        


                        

                        

                                               
