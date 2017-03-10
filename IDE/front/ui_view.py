'''
For mac with python 3, need to run firs:.
1.- brew install gtk+3
2.- brew install pygobject3 --with-python3
'''

import ui_core

import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk, Gdk


class IdeWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Secciones principales de la UI.
        main = Gtk.Layout()
        view_box = Gtk.HBox(False,5)

        # Elementos de la parte izquierda.
        # ... Contenedor principal.
        left_area = Gtk.VBox(False,5)
        # left_title = Gtk.Label("Tools")
        # ... Botonera.
        # 1
        tools_area = Gtk.VBox(False,5)
        button = Gtk.Button.new_with_mnemonic("_Add")
        button.connect("clicked", self.on_add_comp)
        tools_area.pack_start(button, True, True, 0)
        # 2
        button = Gtk.Button.new_with_mnemonic("_Connection")
        button.connect("clicked", self.on_make_connection)
        tools_area.pack_start(button, True, True, 0)
        ### Conexiones de los elementos de la izquierda.
        # left_area.add(left_title)
        left_area.add(tools_area)

        # Elementos de la parte derecha.
        # ... Contenedor principal.
        right_area = Gtk.VBox(False,5)
        # right_title = Gtk.Label("Canvas")
        # ... Canvas.
        canvas_area = Gtk.Layout()
        ### Conexiones de los elementos de la derecha.
        # right_area.add(right_title)
        right_area.add(canvas_area)

        # Conexion de seccion izq y drch. (H=0, V=1)
        view_box.add(left_area)
        view_box.add(Gtk.Separator())
        view_box.add(right_area)
        # Anhadir la caja principal a un layout para visualizado correcto.
        main.add(view_box)

        self.add(main)
        self.show_all()

    def on_add_comp(self, btn):
        print("click_NewComp")

    def on_make_connection(self, btn):
        print("click_MakeConnection")


class IdeApplication(Gtk.Application):

    def __init__(self):
        super().__init__(application_id="org.Daniel.Camba")
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.on_about)
        self.add_action(action)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

    def do_activate(self):
        # Construccion SINGLETON de la ventana de la app.
        if not self.window:
            self.window = IdeWindow(
                title="•UIFD•",
                resizable=False,
                application=self,
                default_height=(int)(Gdk.Screen.height()/3),
                default_width=(int)(Gdk.Screen.width()/3)
            )
        # Muestra al usuario dicha ventana.
        self.window.present()

    def on_about(self, action, param):
        about_dialog = Gtk.AboutDialog(
            transient_for=self.window, modal=True
        )
        about_dialog.present()

    def on_quit(self, action, param):
        self.quit()


# Python main, lanza la aplicacion.
if __name__ == "__main__":
    app = IdeApplication()
    app.run(sys.argv)
