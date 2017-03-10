from lxml import etree as ET

class Simple:

    def __init__( self ):
        self.name     = str()
        self.img      = str()
        self.active   = bool(1)
        self.visible  = bool(1)
        self.sizeType = str()
        self.sizeX    = int()
        self.sizeY    = int()
        self.posType  = str()
        self.posX     = int()
        self.posY     = int()

    def __str__( self ):
        return "Name: {}\nImg: {}\nActive: {}\nVisible: {}\
            \nSizeType: {}\nSizeX: {}\nSizeY: {}\
            \nPosType: {}\nPosX: {}\nPosY: {}\n"\
            .format(
                self.name,
                self.img,
                self.active,
                self.visible,
                self.sizeType,
                self.sizeX,
                self.sizeY,
                self.posType,
                self.posX,
                self.posY
            )

    def strOnComplex( self ):
        return "\n\t~ Name: {}\n\tImg: {}\n\tActive: {}\n\tVisible: {}\
        \n\tSizeType: {}\n\tSizeX: {}\n\tSizeY: {}\
        \n\tPosType: {}\n\tPosX: {}\n\tPosY: {}"\
        .format(
                self.name,
                self.img,
                self.active,
                self.visible,
                self.sizeType,
                self.sizeX,
                self.sizeY,
                self.posType,
                self.posX,
                self.posY
            )


    def fromXML( self, node ):
        inside        = node.Visual_Appearance.Enumeration
        self.name     = node.get('Name')
        self.visible  = node.get('Visible')
        self.active   = node.get('Active')
        self.img      = inside.File
        self.sizeType = inside.Size.get('Type')
        self.sizeX    = int(inside.Size.ValueX)
        self.sizeY    = int(inside.Size.ValueY)
        self.posType  = inside.Position.Relative.tag
        self.posX     = int(inside.Position.Relative.Coordinate.Px)
        self.posY     = int(inside.Position.Relative.Coordinate.Py)

    def toXML( self ):
        sc         = ET.Element(
            'Simple_Component',
            {
                'Name'    : self.name,
                'Active'  : str(self.active),
                'Visible' : str(self.visible),
            }
        )
        va         = ET.SubElement( sc, 'Visual_Appearance' )
        enum       = ET.SubElement( va, 'Enumeration' )

        file       = ET.SubElement(enum, 'File')
        file.text  = self.img

        size       = ET.SubElement(enum, 'Size', {'Type':self.sizeType})
        sizeX      = ET.SubElement(size, 'ValueX')
        sizeX.text = str(self.sizeX)
        sizeY      = ET.SubElement(size, 'ValueY')
        sizeY.text = str(self.sizeY)

        position   = ET.SubElement(enum, 'Position')
        posType    = ET.SubElement(position, self.posType)
        cords      = ET.SubElement(posType, 'Coordinate')
        cordX      = ET.SubElement(cords, 'Px')
        cordX.text = str(self.posX)
        cordY      = ET.SubElement(cords, 'Py')
        cordY.text = str(self.posY)

        return sc
