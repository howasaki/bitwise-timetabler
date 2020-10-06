import pygtk
import gtk
import gtk.glade
import sys
import os

class GladeConnect:

    def __init__(self, gladeFile, widget=None):
        dirName = os.path.dirname(sys.argv[0])
        if dirName != "" :
            dirName = dirName + os.sep + gladeFile
        else:
            dirName = gladeFile
        
        # Comprobacion de que el fichero .glade existe.
        try :
            os.stat(dirName)
        except :
            raise AttributeError, "No existe el recurso %s" %gladeFile
        
        self.gui = gtk.glade.XML(dirName, widget)
        self.conectar()
        

    def conectar(self):
        self.gui.signal_autoconnect(self)

    def __getattr__(self, nombre):
        result = self.gui.get_widget(nombre)
        if result == None:
            raise AttributeError, nombre
        return result
