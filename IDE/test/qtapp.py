#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class IDE_UIFD(QMainWindow) :

    # Constructor base.
    def __init__(self) :
        super().__init__()
        self.UI()

    # Definición de la interfaz.
    def UI(self) :
        # 0. Actions.
        AB_exit = self.new_action( 'Salir','Ctrl+Q','Dejar la app!',self.close )

        # 1. Canvas
        canvas = QTextEdit()
        self.setCentralWidget(canvas)

        # 2. Barra de menu.
        menubar = self.menuBar()
        self.new_menu_opt(menubar,'App',AB_exit)
        self.new_menu_opt(menubar,'Archivo',AB_exit)
        self.new_menu_opt(menubar,'Edición',AB_exit)
        self.new_menu_opt(menubar,'Visualización',AB_exit)
        self.new_menu_opt(menubar,'Ventana',AB_exit)
        self.new_menu_opt(menubar,'Ayuda',AB_exit)

        # 3. Barra de herramientas.
        toolbar = self.addToolBar('Tools')
        toolbar.addAction( AB_exit ) # Añadir cuadrado

        # 4. Barra lateral (izquierda).
        menubar = self.menuWidget()

        # 5. Barra de estado.
        self.statusBar()

        # 6. Barra de titulo y lanzar la app.
        self.setWindowTitle('• FreeDesignUI - IDE •')
        self.show()

    # Metodo para crear botones/acciones.
    def new_action(self,tag,shortcut,sb_text,action) :
        AB = QAction(tag, self)       # botón
        AB.setShortcut(shortcut)        # atajo
        AB.setStatusTip(sb_text)        # statusbar
        AB.triggered.connect(action)    # accion
        return AB

    #Metodo para añadir items a la barra de menu.
    def new_menu_opt(self,mb,opt_name,*actions) :
        menu_opt = mb.addMenu(opt_name)
        for act in actions :
            menu_opt.addAction(act)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = IDE_UIFD()
    sys.exit(app.exec_())
