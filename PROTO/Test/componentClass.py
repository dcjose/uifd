#CLASE POSICION Y TAMAÑO
class Position(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(X,Y)=({},{})".format(self.x,self.y)


class Event():
	def __init__(self, eventId, event, endState):
		self.eventId = eventId
		self.event = event
		self.endState = endState
		self.preconditions = []

	def __str__(self):
		return "\tEventId: {} | Evento: {} | Estado Final en caso de evento: {}".format(self.eventId, self.event, self.endState)

#-------------------------------------------------------------------------------
#CLASE COMPONENTE
class Component(object):
	def __init__(self, name=None):
		self.name = name

#CLASE COMPONENTE SIMPLE QUE HEREDA DE LA CLASE Component
class Simple_Component(Component):
	#Constructor de Componente Simple
	def __init__(self, name=None, sVisible=True, sActive=True, file=None, size=None, positionType=None, position=None):
	#nombre / sVisible / sActive / file / size / positionType /position
		super().__init__(name)
		self.sVisible = sVisible
		self.sActive = sActive
		self.file = file
		self.size = size
		self.positionType = positionType
		self.position = position

	#Metodo para variar el nombre en la clase padre
	def setName(self, name):
		self.name = name
	#Metodo para variar estado de componente "Visible"
	def setVisible(self, sVisible):
		self.sVisible = sVisible
	#Metodo para variar estado de componente "Active"
	def setActive(self, sActive):
		self.sActive = sActive

	def setFile(self, file):
		self.file = file

	def setSize(self, size):	#FALTA AÑADIRLO COMO DOS VALORES
		self.size = size

	def setPosType(self, positionType):
		self.positionType = positionType

	def setPos(self, position):		#FALTA AÑADIRLO COMO DOS VALORES
		self.position = position

	def __str__(self):
		return "SC: {} | Visible: {} | Activo: {} | Archivo: {} | Size: {} | Position: {} | TipoPosicion: {}".format(self.name, self.sVisible, self.sActive, self.file, self.size,  self.position, self.positionType)

#CLASE ESTADO INDIVIDUAL CON NOMBRE DE COMPONENTE, VISIBLE Y ACTIVE
class Status(object):
	#Constructor de estado individual
	def __init__(self, cName, cVisible, cActive):
		self.cName = cName
		self.cVisible = cVisible
		self.cActive = cActive
	def __str__(self):
		return "\tNombre Comp: {} | Visible: {} | Activo: {}".format(self.cName, self.cVisible, self.cActive)


#CLASE DE LA ENTIDAD STATE QUE ENGLOBA VARIOS STATUS.
class State(object):
	#Constructor de State
	def __init__(self, stateId=None,stateVisible=False, stateActive=False):
		self.stateId = stateId
		self.stateVisible = stateVisible
		self.stateActive = stateActive
		self.comp = [] #Lista de componentes asociados al estado
		self.events = [] #Lista de eventos

	def setId(self, id):
		self.id = id

	def __str__(self):
		print("StateId: {} | Visible: {} | Active: {}".format(self.stateId, self.stateVisible, self.stateActive))
		for i in self.comp:
			print("\t",i)
		for i in self.events:
			print("\t",i)
		return ""



#CLASE COMPONENTE COMPLEJO
class Complex_Component(Component):
	#Constructor de Componente Complejo
	def __init__(self, name=None):
		super().__init__(name)
		#components = [] #ARRAY DE COMPONENTES HIJO
		self.states = []	#ARRAY DE ESTADOS DE COMPONENTE COMPLEJO
		self.components = []
		self.activeState = "0" #ESTADO ACTIVO POR DEFECTO

	def setName(self, name):
		self.name = name

	def __str__(self):
		print ("Componente Complejo: {}".format(self.name))
		for i in self.states:
			print("\t",i)
		for s in self.components:
			print("\t",s)
		return ""



#*Debe ponerse object de parametro cuando la clase no hereda de nadie
#TEST
#a= Simple_Component('Cosa',True, True, 'cosa.png', 'cosa', 'al lado', 'ahi')
#b= Complex_Component('CC_ball1')
#print (a)
#print(b)
