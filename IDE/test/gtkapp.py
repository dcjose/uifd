'''
For mac with python 3, need to run firs:.
1.- brew install gtk+3
2.- brew install pygobject3 --with-python3
'''

import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk


class IdeWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.main_layout = Gtk.Layout()


class Application(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="org.Daniel.Camba",
            **kwargs
        )
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
            self.window = IdeWindow(application=self, title="•UIFD•")
        # Muestra al usuario dicha ventana.
        self.window.present()

    def on_about(self, action, param):
        about_dialog = Gtk.AboutDialog(transient_for=self.window, modal=True)
        about_dialog.present()

    def on_quit(self, action, param):
        self.quit()


# Python main, lanza la aplicacion.
if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)
