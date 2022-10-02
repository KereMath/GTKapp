import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio

import subprocess

class MainWindow:
    def __init__(self, app):
        # Gtk Builder
        self.builder = Gtk.Builder()

        # Import UI file:
        self.builder.add_from_file("MainWindow.glade")
        self.builder.connect_signals(self)

        # Window
        self.window = self.builder.get_object("window")
        self.window.set_application(app)

        # Glade'deki elemanlari kullanmak icin degiskene atayalim:
        self.defineComponents()

        # Show window
        self.window.show_all()

    def defineComponents(self):
        self.lbl_output = self.builder.get_object("lbl_output")

    def on_btn_ben_kimim_clicked(self, btn):
        process = subprocess.run(["whoami"], capture_output=True)
        output = process.stdout.decode("utf-8")

        self.lbl_output.set_label(output)

    def on_btn_listele_clicked(self, btn):
        process = subprocess.run(["ls", "/"], capture_output=True)
        output = process.stdout.decode("utf-8")

        self.lbl_output.set_label(output)
