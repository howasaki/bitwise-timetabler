import os

import gtk
"""
from SimpleGladeApp import SimpleGladeApp
from SimpleGladeApp import bindtextdomain

app_name = "iumain"
app_version = "0.0.1"

glade_dir = ""
locale_dir = ""

bindtextdomain(app_name, locale_dir)

def list_cero_a(num_lim):
    L = []
    for i in range(num_lim):
        L.append(i)
    return L

def get_text_buff(t_buff):
    return t_buff.get_text(t_buff.get_start_iter(), t_buff.get_end_iter())

def set_text_buff(text_view, str_):
    tb = gtk.TextBuffer()
    tb.set_text(str_)
    text_view.set_buffer(tb)

def mostrar_tabla(tree_view, list_cabec, data):
    
    #tree_view: gtk.TreeView
    #lis_cabec : Lista con los nombres de las cabeceras
    #data : Lista de tuplas Ejm: --> [(1,2,3), (4,5,6)]
    
    borrar_columnas(tree_view)
    ncols = len(list_cabec)
    nfils = len(data)
    liststore = gtk.ListStore(*[str]*ncols)
    for c in range(ncols):
        tvcol = gtk.TreeViewColumn(list_cabec[c], gtk.CellRendererText(), text=c)
        tree_view.insert_column(tvcol, c)
    for f in range(nfils):
        liststore.insert(f, list(data[f]))
    tree_view.set_model(liststore)
    
    
def borrar_columnas(tree_view):
    columnlist = tree_view.get_columns()
    for column in columnlist:
        tree_view.remove_column(column)
        
def obtener_fila_tv(tree_view, cols = 3):
    treeselection = tree_view.get_selection()
    t_sel = treeselection.get_selected()
    return tree_view.get_model().get(t_sel[1], *list_cero_a(cols))
    
def cargar_arbol(treeview, L, nombre_metodol):
    treestore = gtk.TreeStore(str)
    treeview.set_model(treestore)
    # create the TreeViewColumn to display the data
    tvcolumn = gtk.TreeViewColumn('Column 0')
    # add tvcolumn to treeview
    treeview.append_column(tvcolumn)
    # create a CellRendererText to render the data
    cell = gtk.CellRendererText()
    # add the cell to the tvcolumn and allow it to expand
    tvcolumn.pack_start(cell, True)
    
    #set the cell "text" attribute to column 0 - retrieve text
    # from that column in treestore
    tvcolumn.add_attribute(cell, 'text', 0)
    parent = treestore.append(None, [nombre_metodol])
    cargar_arbol_r(treestore, L, parent, None)

def cargar_arbol_r(treestore, L, hijo, padre):
    longitud = len(L)
    for i in range(longitud):
        L1 = L[i]
        if type(L1) is tuple:
            cargar_arbol_r(treestore, L1, padre, hijo)
        else:
            hijo = treestore.append(padre, [L1])
            
            
class Dialogo(SimpleGladeApp):

    def __init__(self, texto, path="iubc.glade",
                 root="dialogo",
                 domain=app_name, **kwargs):
        path = os.path.join(glade_dir, path)
        SimpleGladeApp.__init__(self, path, root, domain, **kwargs)
        self.label.set_text(texto)
        self.dialogo.show()

    #-- Dialogo.new {
    def new(self):
        print "A new %s has been created" % self.__class__.__name__
    #-- Dialogo.new }

    #-- Dialogo custom methods {
    #   Write your own methods here
    #-- Dialogo custom methods }

    #-- Dialogo.on_dialogo_response {
    def on_dialogo_response(self, widget, *args):
        print "on_dialogo_response called with self.%s" % widget.get_name()
    #-- Dialogo.on_dialogo_response }

    #-- Dialogo.on_bt_aceptar_activate {
    def on_bt_aceptar_activate(self, widget, *args):
        print "on_bt_aceptar_activate called with self.%s" % widget.get_name()
        self.dialogo.destroy()
    #-- Dialogo.on_bt_aceptar_activate }
    
"""
def show_yes_no_message(_parent, titulo, mensaje):
    msgbox = gtk.MessageDialog(parent = _parent, buttons = gtk.BUTTONS_YES_NO, flags = gtk.DIALOG_MODAL, type = gtk.MESSAGE_QUESTION, message_format = mensaje)
    msgbox.set_title(titulo)
    result = msgbox.run()
    msgbox.destroy()
    return result == gtk.RESPONSE_YES
