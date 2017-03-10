import sys
from PyQt5 import QtGui, QtCore, QtSvg
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QListWidget





class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		widget = QLabel(self)
		layout = QVBoxLayout(widget)
		self.setCentralWidget(widget)
		pixmapN = QtGui.QPixmap('imgsXML_Sample/Basket_Ball_N_70x70.png')
		pixmapS = QtGui.QPixmap('imgsXML_Sample/Basket_Ball_S_70x70.png')
		pixN = pixmapN.scaled(70, 70)
		pixS = pixmapS.scaled(70, 70)
		widget.setPixmap(pixN) 

	def eventFilter(self, source, event):
		if event.type() == QtCore.QEvent.GraphicsSceneHoverMove:
			widget.setPixmap(pixS)
		return QMainWindow.eventFilter(self, source, event)

if __name__ == '__main__':
	app = QApplication(sys.argv) 
	win = Window()
	win.show()
	app.installEventFilter(win)
	sys.exit(app.exec_())


