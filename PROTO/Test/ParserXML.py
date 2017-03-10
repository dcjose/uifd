import xml.etree.ElementTree as ET

def XmlParser(file):
	tree = ET.parse(file)
	root = tree.getroot()
	return root
