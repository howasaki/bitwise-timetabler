import pygtk
import gtk

dias = ['Hora', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

class RepHorario:
   
   # close the window and quit
   def delete_event(self, widget, event, data=None):
      gtk.main_quit()
      return False
   def __init__(self, data_horario_res = None):
      # Create a new window
      self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
      self.window.set_title("Planificacion de horario - Horario Resultante!!!")
      self.window.set_size_request(200, 200)
      self.window.connect("delete_event", self.delete_event)
      self.treeview = gtk.TreeView()
      
      if data_horario_res:
         self.crear(self.treeview, dias, data_horario_res)
      
      self.window.add(self.treeview)
      self.window.show_all()
      
   def crear(self, tree_view, list_cabec, data):
      """
      data : Lista de tuplas --> [(1,2,3), (4,5,6)]
      """
      
      ncols = len(list_cabec)
      nfils = len(data)
      liststore = gtk.ListStore(*[str]*ncols)
      
      for c in range(ncols):
	 tvcol = gtk.TreeViewColumn(list_cabec[c], gtk.CellRendererText(), text=c)
	 tree_view.append_column(tvcol)
      for f in range(nfils):
	 liststore.append(list(data[f]))
      tree_view.set_model(liststore)
      
      
      
def mostrar_horario(data_horario_res):
   rep_horario = RepHorario(data_horario_res)
   gtk.main()
   
   
"""
if __name__ == "__main__":
   rep_horario = RepHorario()
   main()
"""
