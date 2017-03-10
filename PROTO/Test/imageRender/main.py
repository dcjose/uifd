from PyQt5 import QtCore, QtGui, QtWidgets

class ClickableLabel(QtWidgets.QLabel):
	clicked = QtCore.pyqtSignal(str)

	def __init__(self, width, height, name):
		super(ClickableLabel, self).__init__()
		pixmap = QtGui.QPixmap('imgsXML_Sample/'+name)
		#self.setPixmap(pixN)
		self.setPixmap(pixmap.scaled(width,height,QtCore.Qt.KeepAspectRatio));
		self.setObjectName(name)

	def mousePressEvent(self, event):
		self.clicked.emit(self.objectName())

class Window(QtWidgets.QWidget):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)

		self.layout = QtWidgets.QVBoxLayout()
		self.hbox = QtWidgets.QHBoxLayout()
		self.stackBall = QtWidgets.QStackedWidget();
		self.stackField = QtWidgets.QStackedWidget();

		self.flag = 0			#Valor para controlar el clic de label
		self.field = 0			#Valor para controlar el clic de field
		self.namesBall1 = ['Basket_Ball_N_70x70.png','Basket_Ball_S_70x70.png','Basket_Ball_C_70x70.png']
		self.namesField = ['Basket_Field_N_132x96.png','Basket_Field_C_132x96.png']

		self.labelN = ClickableLabel(70, 70,self.namesBall1[0])
		self.labelN.clicked.connect(self.handleLabelClicked)
		self.stackBall.addWidget(self.labelN)

		self.labelS = ClickableLabel(70, 70,self.namesBall1[1])
		self.labelS.clicked.connect(self.handleLabelClicked)
		self.stackBall.addWidget(self.labelS)

		self.labelC = ClickableLabel(70, 70,self.namesBall1[2])
		self.labelC.clicked.connect(self.handleLabelClicked)
		self.stackBall.addWidget(self.labelC)

		self.label2N = ClickableLabel(132, 96,self.namesField[0])
		self.label2N.clicked.connect(self.handleFieldClicked)
		self.stackField.addWidget(self.label2N)

		self.label2C = ClickableLabel(132, 96,self.namesField[1])
		self.label2C.clicked.connect(self.handleFieldClicked)
		self.stackField.addWidget(self.label2C)


		self.hbox.addWidget(self.stackBall)
		self.hbox.addWidget(self.stackField)
		self.layout.addLayout(self.hbox)
		self.setLayout(self.layout)

		self.setWindowTitle('PROTO')

	def handleLabelClicked(self, name): #Método-evento vinculado al click sobre Label (Pelotas)
		if self.flag==0:
			self.stackBall.setCurrentWidget(self.labelS)
		else:
			if self.flag==1:
				self.stackBall.setCurrentWidget(self.labelN)
		self.flag ^= 1					 #Cambiar valor de flag al contrario (0 o 1)
		print('"%s" clicked' % name)	#Traza por ventana de comandos que proporciona información de que label se ha clicado

	def handleFieldClicked(self, name): #Método-evento vinculado al click sobre Field (Campos)
		if self.flag==1:
			self.stackBall.setCurrentWidget(self.labelC)
			self.flag=2
			self.field^=1
			if self.field==0:
				self.stackBall.setCurrentWidget(self.label2N)
			else:
				self.stackField.setCurrentWidget(self.label2C)

		print('"%s" clicked' % name)


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 200, 200)
    window.show()
    sys.exit(app.exec_())
