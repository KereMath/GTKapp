#!/usr/bin/env python3

import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio

from MainWindow import MainWindow

class Uygulama(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
            application_id="",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
            **kwargs)
    
    def do_activate(self): # This method runs when the program is opened.
        self.window = MainWindow(self) # Created out Mainwindow object
      

# Creating our application object and running
app = Uygulama()
app.run(sys.argv)
