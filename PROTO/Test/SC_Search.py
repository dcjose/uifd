from componentClass import Simple_Component, Position

#Método de búsqueda que printa como resultado
#todos los datos (propiedades) del SC recibido por parámetro
def SearchSC_Component(name, xmlParsed):
	for a in xmlParsed.iter(tag='Simple_Component'):
		sc = Simple_Component()
		if name == a.get('Name'):
			sc.setName(a.get('Name'))
			#sc.setVisible(a.get('Visible'))
			#sc.setActive(a.get('Active'))
			for b in a.iterfind('Visual_Appearance/Enumeration'):
				for c in b.findall('File'):
					sc.setFile(c.text)	#Añadimos a la variable file de la clase el valor del XML
				for c in b.findall('Size'):
					tamX = c.find('ValueX').text
					tamY = c.find('ValueY').text
					size = Position(tamX, tamY)
					sc.setSize(size)
				for c in b.iterfind('Position/'):
					sc.setPosType(c.tag)
					for d in c.findall('Coordinate'):
						pX = d.find('Px').text
						pY = d.find('Py').text
						pos = Position(pX, pY)
						sc.setPos(pos)
			break

	return sc #Retorna el sc con todos los datos encontrados en el XML
