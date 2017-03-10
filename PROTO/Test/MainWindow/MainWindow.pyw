import sys	#modulo sys de argumento argv
#Para trabajar con la aplicación y con ventanas respectivamente
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox	
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
		uic.loadUi("MainWindow.ui", self)
		self.setWindowTitle("Cambiando el título de la ventana")
		#Mostrar la ventana maximizada
		#self.showMaximized()

		#Fijar el tamaño de la ventana
		#Fijar el tamaño minimo
		self.setMinimumSize(800,600)
		#Fijar el tamaño maximo
		self.setMaximumSize(800,600)

		#Mover la ventana y centrarla en el escritorio
		resolucion = ctypes.windll.user32
		resolucion_ancho = resolucion.GetSystemMetrics(0)
		resolucion_alto = resolucion.GetSystemMetrics(1)
		left = (resolucion_ancho/2)-(self.frameSize().width()/2)
		top = (resolucion_alto/2)-(self.frameSize().height()/2)
		self.move(left, top)

		#Desactivar la ventana
		#self.setEnabled(False)

		#Asignar un tipo de fuente
		qfont = QFont("Arial",12,QFont.Bold)
		self.setFont(qfont)

		#Asignar un tipo de cursor
		self.setCursor(Qt.SizeAllCursor)

		#Asignar estilos CSS
		#self.setStyleSheet("background-color:#00f; color: fff;")
		self.boton1.setText("Archivo")
		self.boton2.setText("Ver")
		self.boton3.setText("Herramientas")
		self.boton4.setText("Perfiles")
		self.boton5.setText("Ayuda")
		self.boton6.setText("Salir")
		self.boton1.setStyleSheet("background-color: #535; color: #fff; font-size: 14px;")
		self.boton2.setStyleSheet("background-color: #535; color: #fff; font-size: 14px;")
		self.boton3.setStyleSheet("background-color: #535; color: #fff; font-size: 14px;")
		self.boton4.setStyleSheet("background-color: #535; color: #fff; font-size: 14px;")
		self.boton5.setStyleSheet("background-color: #535; color: #fff; font-size: 14px;")
		self.boton6.setStyleSheet("background-color: #535; color: #fff; font-size: 14px;")
		
	#Evento de muestra de texto en Label
	def showEvent(self, event):
		self.bienvenido.setText("Bienvenido!")

	#Evento de doble verificación en cierre de ventana 
	def closeEvent(self, event):
		resultado = QMessageBox.question(self, "Salir...", "¿Seguro que quieres salir?",QMessageBox.Yes |QMessageBox.No)
		if resultado == QMessageBox.Yes: 
			event.accept()
		else: 
			event.ignore()

	def moveEvent(self, event):
		x = str(event.pos().x())
		y = str(event.pos().y())
		self.posicion.setText("x: " + x + " y: " + y)

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)

#Crear un objeto de la clase creada anteriormente
_ventana = Ventana()

#Mostar la ventana
_ventana.show()

#Ejecutar la aplicación
app.exec_()