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

	def obtener_estado(self):
                """MÃ©todo que devuelve un diccionario con los atributos de la criatura y su estado"""
                estado_atributos={}
                for clave in self.caracteristicas.keys():
                        estado_atributos[clave]=self.caracteristicas[clave]
                for clave in self.indicadores.keys():
                        estado_atributos[clave]=self.indicadores[clave]
                return estado_atributos
                
   def aplicar_consecuencias(self, consecuencias):
                """Aplica consecuencias al recibir ataque o realizar ataque"""
                for clave in consecuencias.keys():
                        self.indicadores[clave]=self.indicadores[clave]+consecuencias[clave]
                        self.caracteristicas[clave]=self.caracteristicas[clave]+consecuencias[clave]
   def obtenerhabilidades(self):
                """Metodo que devuelve diccionario con las habilidades de la criatura.
Las claves son el nombre de la habilidad y los valores son la instancia de la clase correspondiente"""
                habilidades_totales={"Big_Bang_Attack":Big_Bang_Attack(),"Psicoataque":Psicoataque(),"Chupacabras":Chupacabras(),"Golpe_martillo":Golpe_martillo(),
                "Ataque_wachenhausen":Ataque_wachenhausen(),"Fatality":Fatality(),"Furia_de_Ares":Furia_de_Ares()}
                habilidades_a_usar={}
                cont=3
                while cont>0:
                        for clave in habilidades_totales.keys():
                                habilidades_a_usar[clave]=habilidades_totales[clave]
                                cont-=1
                return  habilidades_a_usar
                        

class Golpe_martillo(object):
        """Modela la habilidad"""
        def __init__(self):
                self.nombre="Golpe martillo"
                self.descripcion="Golpe de puño ágil y poderoso"
                self.autor="Riemer - Masello"
        def obtener_costos(self):
                """Devuelve un diccionario con los valores mnimos de caractersticas
y/o indicadores que debe tener la criatura para poder aplicar la habilidad."""
                costos={"fuerza":14,"inteligencia":4, "contextura":13, "destreza":12, "carisma":4, "sabiduria":3}
                return costos

        def obtener_consecuencias(self, origen, final):
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
                modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":-1, "destreza":-1, "carisma":-1,"sabiduria":0,"xp":3,"hp":-20,"mp":0}
                modificaciones_criatura_origen={"fuerza":1,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":5,"hp":0,"mp":-10}   
                return modificaciones_criatura_origen, modificaciones_criatura_destino
                


class Ataque_wachenhausen(objecto):
        """Modela la habilidad"""
	def __init__(self):
                self.nombre="Wachenhausen"
                self.descripcion="Te quema la cabeza"
                self.autor="Riemer-Masello"
        def obtenercostos(self):
                """Devuelve un diccionario con los valores mnimos de caractersticas
y/o indicadores que debe tener la criatura para poder aplicar la habilidad."""
                costos={"fuerza":4,"inteligencia":16, "contextura":5, "destreza":14, "carisma":16, "sabiduria":16, "mp":10}
		return costos
	def obtener_consecuencias(self, origen, final):
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
                modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":-1, "destreza":-1, "carisma":-1,"sabiduria":0,"xp":2,"hp":-35,"mp":0}
                modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":2,"hp":0,"mp":-10}   
                return modificaciones_criatura_origen, modificaciones_criatura_destino
class Fatality(objecto):
        """Modela la habilidad"""
	def __init__(self):
                self.nombre="Fatality"
                self.descripcion="Te mata"
                self.autor="Riemer-Masello"
        def obtenercostos(self):
                """Devuelve un diccionario con los valores mnimos de caractersticas
y/o indicadores que debe tener la criatura para poder aplicar la habilidad."""
                costos={"fuerza":13,"inteligencia":16, "contextura":13, "destreza":14, "carisma":16, "sabiduria":16, "mp":40}
		return costos
	def obtener_consecuencias(self, origen, final):
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
                modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":-1, "destreza":-1, "carisma":-1,"sabiduria":0,"xp":2,"hp":-80,"mp":0}
                modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":2,"hp":0,"mp":-40}   
                return modificaciones_criatura_origen, modificaciones_criatura_destino
                
class Big_Bang_Attack(object):
    """Modela la habilidad. Tiene los metodos __init__, obtener_costos, y obtener_consecuencias"""
    def __init__(self):
        """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
        self.nombre="Big Bang Attack"
        self.descripcion="El ataque Big Bang es un enorme rayo de energia con un increible poder de destrucciÃ³n. La criatura extiende su mano hacia el enemigo y lanza el rayo"
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
        modificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":-1, "destreza":-1, "carisma":-1,"sabiduria":0,"xp":0,"hp":-35,"mp":0}
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":2,"hp":0,"mp":-10}   
        return modificaciones_criatura_origen, modificaciones_criatura_destino

class Psicoataque(object):
    """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
def __init__(self):
        """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
        self.nombre="Psicoataque"
        self.descripcion="El psicoataque es un ataque que utiliza la fuerza del oponente y la utiliza para causarle daños psicologicos. Este ataque lo podran utilizar aquellas criaturas que posean un elevado grado de inteligencia"
        self.autor="Masello-Riemer"
    def obtener_costos(self):
        """Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad"""
        valores_minimos={"inteligencia":6,"sabiduria":6,"xp":4,"mp":14}
        return valores_minimos
    def obtener_consecuencias(self,origen,destino):
        """Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
        precondiciones: origen y destino deben ser del tipo criatura
        postcondiciones: devuelve dos diccionarios.Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
        valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
        mofificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
        for clave in valores_minimos.keys():
            if atributos_criatura.haskey(clave):
                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
                    return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
        modificaciones_criatura_destino={"fuerza":0,"inteligencia":-2,"contextura":-1, "destreza":-1, "carisma":-1,"sabiduria":-2,"xp":1,"hp":-15,"mp":-2}
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":5,"contextura":0, "destreza":0, "carisma":0,"sabiduria":2,"xp":3,"hp":0,"mp":10}   
        return modificaciones_criatura_origen, modificaciones_criatura_destino

class Chupacabras(object):
    """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
def __init__(self):
        """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
        self.nombre="chupacabras"
        self.descripcion="En este ataque la criatura utiliza un metodo de seduccion otorgado por Afrodita (diosa griega) para seducir al oponente y asi lograr paralizarlo. Al paralizar a su oponente procede a chuparle parte de su vida, transfiriendola a su propio cuerpo"
        self.autor="Masello-Riemer"
    def obtener_costos(self):
        """Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad"""
        valores_minimos={"destreza":5,"carisma":6,"xp":2,"mp":7}
        return valores_minimos
    def obtener_consecuencias(self,origen,destino):
        """Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
        precondiciones: origen y destino deben ser del tipo criatura
        postcondiciones: devuelve dos diccionarios.Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
        valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
        mofificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
        for clave in valores_minimos.keys():
            if atributos_criatura.haskey(clave):
                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
                    return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
        modificaciones_criatura_destino={"fuerza":-1,"inteligencia":0,"contextura":-1, "destreza":0, "carisma":0,"sabiduria":0,"xp":1,"hp":-15,"mp":}
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":1, "destreza":3, "carisma":5,"sabiduria":2,"xp":3,"hp":15,"mp":2}   
        return modificaciones_criatura_origen, modificaciones_criatura_destino
class Furia_de_Ares(object):
    """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
def __init__(self):
        """Metodo constructor de la clase. Crea la instancia de la clase. Contiene los atributos nombre, descripcion, autor """
        self.nombre="Furia de Ares"
        self.descripcion="En este ataque la criatura invoca al dios griego de la guerra, el cual desatara una gran furia, quitandole fuerza y vida al oponente. La criatura que lo invoca debe tener un nivel elevado de magia"
        self.autor="Masello-Riemer"
    def obtener_costos(self):
        """Devuelve un diccionario con los valores minimos de caracteristicas y/o indicadores que debe tener la criatura para poder aplicar la habilidad"""
        valores_minimos={"sabiduria":5,"xp":2,"mp":8}
        return valores_minimos
    def obtener_consecuencias(self,origen,destino):
        """Devuelve dos diccionarios con las alteraciones a realizar sobre los atributos de la criatura origen y la criatura destino
        precondiciones: origen y destino deben ser del tipo criatura
        postcondiciones: devuelve dos diccionarios.Se devuelven diccionarios con valores 0 en caso en que la criatura de origen no tiene los atributos necesarios para realizar la habilidad"""
        valores_minimos=self.obtener_costos()    #Diccionario con los costos para ejecutar la habilidad
        atributos_criatura=origen.obtener_estado()          #Diccionario con los atributos de la criatura
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
        mofificaciones_criatura_destino={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":0,"xp":0,"hp":0,"mp":0}
        for clave in valores_minimos.keys():
            if atributos_criatura.haskey(clave):
                if valores_minimos[clave]>atributos_criatura[clave]:      #Caso en que los atributos de la criatura no alcanzan para realizar la habilidad
                    return  modificaciones_criatura_origen, modificaciones_criatura_destino   #Devuelve los diccionarios con dichos valores en 0
        #Si la criatura cumple con los requisitos necesarios, se procede
        modificaciones_criatura_destino={"fuerza":-5,"inteligencia":0,"contextura":-1, "destreza":0, "carisma":0,"sabiduria":0,"xp":1,"hp":-19,"mp":}
        modificaciones_criatura_origen={"fuerza":0,"inteligencia":0,"contextura":0, "destreza":0, "carisma":0,"sabiduria":5,"xp":3,"hp":0,"mp":-1}   
        return modificaciones_criatura_origen, modificaciones_criatura_destino
class Jugador (object):
    def __init__(self,nombre):
        self.criaturas=[]
        self.puntos=0
        self.nombre=None
        self.descripcion=None
        self.autor=None
    def agregar_criatura(self,criatura):
        """agrega una criatura de la lista de criaturas del jugador.
        precondiciones: criatura debe ser del tipo Criatura"""
        nombre_criatura=raw_input("Ingrese el nombre de su criatura:")
        criatura.nombre=nombre_criatura
        self.criaturas.append(criatura)
    def eliminar_criatura(self,criatura):
        """Elimina una criatura de la lista de criaturas del jugador.
        precondiciones: criatura debe ser del tipo Criatura y la lista de criaturas debe contener a dicha criatura"""
        try:
            self.criaturas.remove(self.criaturas[0])
        except:
            print "La criatura debe estar en la lista de criaturas"
    def elegir_criatura(self):
        """Metodo que devuelve la proxima criatura a utilizar en combate, o bien None si no tiene criaturas disponibles."""
        if self.criaturas==[]:  #Si la lista de criaturas es vacia devuelve None
            return None
        return self.criaturas[0]   #Si hay elementos en la lista de criaturas devuelve el 1º elemento de dicha lista
   def elegir_accion(self, destino):
                """Devuelve el nombre de la habilidad a utilizar y la criatura destino de la habilidad. En el caso de ser un jugador real, interactua con
el usuario para decidirlo, en el caso de ser un jugador artificial, evalua programaticamente sus posibilidades y elige una."""
                criatura_en_batalla=self.elegir_criatura()
                habilidades_criatura=criatura_en_batalla.obtenerhabilidades()
                print "Sus habilidades son:", habilidades.keys()
                habilidad_elegida=raw_input("Ingrese la habilidad elegida:")
                modificadores_jugadores=habilidades_criatura[habilidad_elegida]
                criatura_en_batalla.aplicar_consecuencias(modificadores_jugadores[0])
                destino.aplicar_consecuencias(modificadores_jugadores[1])


class Jugador_artificial_1(object):
    def __init__(self,nombre):
        self.criaturas=[]
        self.puntos=0
        self.nombre="Goku"
        self.descripcion="Elige una habilidad de forma aleatoria"
        self.autor="Masello-Riemer"
    def agregar_criatura(self,criatura):       #Al no ser humano no le asigna nombre a la criatura
        """agrega una criatura de la lista de criaturas del jugador.
        precondiciones: criatura debe ser del tipo Criatura"""
        self.criaturas.append(criatura)
    def eliminar_criatura(self,criatura):
        """Elimina una criatura de la lista de criaturas del jugador. Entendemos que la criatura a eliminar es la primera que se encuentra en la lista, ya que, al no tener posibilidades de elegirla, utiliza siempre la primera criatura de su lista de criaturas
        precondiciones: criatura debe ser del tipo Criatura y la lista de criaturas debe contener a dicha criatura"""
        try:
            self.criaturas.remove(self.criaturas[0])
        except:
            print "La criatura debe estar en la lista de criaturas"
    def elegir_criatura(self):
        """Metodo que devuelve la proxima criatura a utilizar en combate. Al no ser humano y no tener chances de elegirla se devolvera la primera criatura de su lista de criaturas, o bien None si no tiene criaturas disponibles. Entendemos que la proxima criatura a utilizar en combate es la que se encuentra primera en la lista"""
        if self.criaturas==[]:  #Si la lista de criaturas es vacia devuelve None
            return None
        return self.criaturas[0]   #Si hay elementos en la lista de criaturas devuelve el 1º elemento de dicha lista
   def elegir_accion(self, destino):
                """Devuelve el nombre de la habilidad a utilizar y la criatura destino de la habilidad."""
                criatura_en_batalla=self.elegir_criatura()
                habilidades_criatura=criatura_en_batalla.obtenerhabilidades()
                print "Sus habilidades son:", habilidades.keys()
                habilidad_elegida=raw_input("Ingrese la habilidad elegida:")
                modificadores_jugadores=habilidades_criatura[habilidad_elegida]
                criatura_en_batalla.aplicar_consecuencias(modificadores_jugadores[0])
                destino.aplicar_consecuencias(modificadores_jugadores[1])