#! /usr/bin/env python

import sys

try:
    import pygtk
    # Se le dice a pyGTK, si es posible, q se trabaje con GTKv2
    pygtk.require("2.0")
except:
    # Algunas distribuciones vienen con GTK2 y no con pyGTK.
    pass

try:
    import gtk
    import gtk.glade
    print gtk.os
except:
    print "Se necesita instalar pyGTK o GTKv2",
    print "o defina bein la var de entorno PYTHONPATH."
    print "intente: export PYTHONPATH=",
    print "/usr/local/lib/python2.4/site-packages/"
    sys.exit(1)