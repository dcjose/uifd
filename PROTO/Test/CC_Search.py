import xml.etree.ElementTree as ET
from SC_Search import SearchSC_Component

from componentClass import Complex_Component, State, Status, Event

def SearchCC_Component(name,xmlParsed):
#Llamada al método de parseo principal para obtener un objeto root del xml entrante

	for a in xmlParsed.iter(tag='Complex_Component'):
		cc = Complex_Component()
		if name == a.get('Name'):
			cc.setName(name)
			for b in a.iterfind('Composition/'):
			#	Consigo los nombre de los componentes de la composición, los busco en el xml
			#y creo un objeto con sus atributos.
				if(b.tag=='SC'):
					cc.components.append(SearchSC_Component(b.text, xmlParsed))
				else:
					#Llamada recursiva
					cc.components.append(SearchCC_Component(b.text, xmlParsed))

			for b in a.findall('Visual_Appearance'):
				pass

			for b in a.iterfind('CC_States/'):
				if (len(cc.states)==0):#Si el numero de estados almacenados es cero:
					state = State(b.get('ID'),True, True) #Creo un state 0 con Visible y Active a True
				else:
					state = State(b.get('ID')) #Creo un state con Visible y Active con los valores por defecto del constructor
				for c in b.iter('SC'):
					status = Status(c.get('Name'), c.get('Visible'), c.get('Active'))
					state.comp.append(status)
				#NO ES DEL TODO CORRECTO YA QUE UN COMPONENTE COMPLEJO DE CC PUEDE NO TENER ESTADOS
				for c in b.iterfind('Dialog_State/'):
					 #Añado id al state
					event = Event(c.get('ID'),c.get('Event'), c.get('End_State'))
					state.events.append(event)
				cc.states.append(state)
			break
	return cc
	#En cuantas divisiones esta hecho el xml? como detectarlas para realizar el bucle de parseo?
