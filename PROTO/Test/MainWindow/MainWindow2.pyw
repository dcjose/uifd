import sys	#modulo sys de argumento argv
#Para trabajar con la aplicación y con ventanas respectivamente
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic #Para poder usar los .ui directamente
from PyQt5.QtGui import QFont #Asignar un tipo de fuente
from PyQt5.QtCore import Qt #Añadir cursor
import ctypes #Permite acceder  a GetSystemMetrics que permite obtener ancho y alto del escritorio

#Clase heredada de QMainWindow (Constructor de la ventana)
class Ventana(QMainWindow):
	#Metodo constructor de la clasew
	def __init__(self):
		#Iniciar el objeto QMainWindow
		QMainWindow.__init__(self)
		 #Cargar la configuración del archivo .ui en el objeto
		uic.loadUi("MainWindow2.ui", self)
		self.setWindowTitle("Cambiando el título de la ventana")
		#Mostrar la ventana maximizada
		#self.showMaximized()

		#Fijar el tamaño de la ventana
		#Fijar el tamaño minimo
		self.setMinimumSize(800,600)
		#Fijar el tamaño maximo
		self.setMaximumSize(800,600)


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)

#Crear un objeto de la clase creada anteriormente
_ventana = Ventana()

#Mostar la ventana
_ventana.show()

#Ejecutar la aplicación
app.exec_()