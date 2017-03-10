from CC_Search import SearchCC_Component
from ParserXML import XmlParser
from componentClass import Complex_Component

ccc = []

root = XmlParser('spec.xml')
for a in root.iter(tag='Complete_Complex_Component'):
    for b in a.iterfind('Composition/'):
        ccc.append(SearchCC_Component(b.text,root))

for i in ccc:
    print(i)
