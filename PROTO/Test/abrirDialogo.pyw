import sys
from PyQt5 import (QtCore, QtGui, QtWidgets, QApplication, QMainWindow, 
  QDialog, QPushButton, QLabel)
class Dialogo(QDialog):
 def __init__(self):
  QDialog.__init__(self)
  self.resize(200, 100)
  self.setWindowTitle("Cuadro de diálogo")
  self.etiqueta = QLabel(self)
  
class Ventana(QMainWindow):
 def __init__(self):
  QMainWindow.__init__(self)
  self.resize(600, 300)
  self.setWindowTitle("Ventana principal")
  self.boton = QPushButton(self)
  self.boton.setText("Abrir cuadro de diálogo")
  self.boton.resize(200, 30)
  self.dialogo = Dialogo()
  self.boton.clicked.connect(self.abrirDialogo)
  
 def abrirDialogo(self):
  
  self.dialogo.etiqueta.setText("Diálogo abierto")
  self.dialogo.exec_()
  
app = QApplication(sys.argv)
ventana = Ventana()

pic = QtGui.QLabel(ventana)
pic.setGeometry(10, 10, 400, 100)
#use full ABSOLUTE path to the image, not relative
pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/logo.png"))

ventana.show()
app.exec_()