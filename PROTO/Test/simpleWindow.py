import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, 
	QPushButton, QApplication)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    self = QWidget()
    self.setWindowTitle('Ventana PyQT-5')
    self.setWindowIcon(QIcon('icon.ico'))
    self.resize(800, 600)
    self.show()
    self.setToolTip('This is a <b>QWidget</b> widget')

    btn = QPushButton('Button', self)
	btn.setToolTip('This is a <b>QPushButton</b> widget')
	btn.move(50, 50)

    sys.exit(app.exec_())