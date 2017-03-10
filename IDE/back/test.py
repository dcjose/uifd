import io, os, sys
from xml.dom import minidom
from xml.etree import cElementTree

from lxml import etree, objectify

from sc import *
from cc import *
from complex.State import *
from complex.StateStatus import *
from complex.StateDialogEvent import *
from complex.DelegateEvent import *
from complex.DelegateAction import *
from complex.StateDialogEventPrecond import *


def prettify(node):
    raw = cElementTree.tostring(node, 'utf-8')
    parsed = minidom.parseString(raw)
    return parsed.toprettyxml(indent="    ")

def save(file_name, root_node):
    with io.open(file_name+".xml", 'w') as file:
        file.write( prettify( root_node.toXML() ) )

def update(file_name, root_node):
    with io.open(file_name+".xml", 'a') as file:
        file.write( prettify( root_node.toXML() ) )

def file2xml(xml_file):
    xml_with_indentation = objectify.parse(xml_file)
    xml_without_indentation = etree.tostring(xml_with_indentation)
    return objectify.fromstring(xml_without_indentation)


# ----- SIMULACRO DE INTERACCION -----

a = Simple()
a.name = "SC_Ball_1_N"
a.visible = True
a.active = True
a.img = "Foot_Ball_N_70x70.png"
a.sizeType = "fixed"
a.sizeX = 70
a.sizeY = 70
a.posType = "Relative"
a.posX = 50
a.posY = 301

b = Simple()
b.name = "SC_Ball_1_S"
b.visible = True
b.active = True
b.img = "Foot_Ball_S_70x70.png"
b.sizeType = "fixed"
b.sizeX = 70
b.sizeY = 70
b.posType = "Relative"
b.posX = 50
b.posY = 301

# .......
c = Complex()
c.name = "Complejillo"
c.addComps(a.name, b.name)

s0 = State(0,True,True)
s1 = State(1,True,True)

a_st0 = StateStatus(a.name,True,True)
b_st0 = StateStatus(b.name,False,False)

a_st1 = StateStatus(a.name,False,False)
b_st1 = StateStatus(b.name,True,True)

a_diag0 = StateDialogEvent(0, '', a.name, 0, 1)
b_diag1 = StateDialogEvent(0, '', b.name, 1, 0)


s0.addStatus(a_st0, b_st0)
s1.addStatus(a_st1, a_st1)

pred0 = StateDialogEventPrecond("cc2", 1)
a_diag0.addPreconds(pred0)

s0.addDialogs(a_diag0)
s1.addDialogs(b_diag1)

trigDE1 = TriggerDE(0, '', 1, 2)
trigDE2 = TriggerDE(1, '', 2, 1)

trigDA1 = TriggerDA(0, 1, '', 2)
trigDA2 = TriggerDA(1, 2, '', 1)

c.addState(s0, s1)
c.addEvent(trigDE1, trigDE2)
c.addAction(trigDA1, trigDA2)

# print(c)

fileName = "test"
save(fileName, a)
save(fileName, b)
save(fileName, c)

iNode = Complex()
iNode.fromXML( file2xml('test.xml') )

print (iNode)

save('test2', iNode)

# ----- SIMULACRO DE INTERACCION -----
