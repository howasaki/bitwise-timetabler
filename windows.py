import pygtk
import gtk
from gladeConnect import GladeConnect

#import gtksourceview

class WinMain(GladeConnect):
    
    def __init__(self):
        GladeConnect.__init__(self, 'main.glade', 'winMain')
        self.winMain.set_title('UAGRM Expert Timetabler v1.0')
        self.winMain.show_all()

    def delete_event(self, widget, event, data=None):
        return False
    
    def destroy(self, data=None):
        gtk.main_quit()

    # Manejadores.
    def on_winMain_destroy(self, ventana=None):
        self.destroy()
    
    def on_mnsalir_activate(self, menuitem=None):
        self.destroy()
    
    def on_mnabout_activate(self, menuitem=None):
        DlgAbout().show()

    def on_toolbtnNuevo_clicked(self, toolbtn=None):
        WinPlanHorario1().show()
    
    def on_toolbtnAbout_clicked(self, toolbtn=None):
        DlgAbout().show()

    def on_mnplanificarhorario_activate(self, menuitem=None):
        print("mostrando el formulario planificar horario 1")
        WinPlanHorario1().show()

class WinConfiguracion(GladeConnect):
    def __init__(self):
        GladeConnect.__init__(self, 'main.glade', 'winConfig')
    
    def show(self):
        self.winConfig.show_all()
    
    # Manejadores.
    def on_conf_btnAniadir_clicked(self, btn=None):
        pass

    def on_conf_btnBorrar_clicked(self, btn=None):
        pass

class WinPlanHorario1(GladeConnect):
    def __init__(self):
        GladeConnect.__init__(self, 'main.glade', 'winPlanHorario1')
        ## TODO: inicializar componentes de este formulario.
        """self.mimodelo = gtk.ListStore(str);
        self.cmbUniversidad.set_model(self.mimodelo)
        self.cell = gtk.CellRendererText()
        self.mimodelo.append(['UAGRM Universidad Autonoma Gabriel Rene Moreno'])
        self.mimodelo.append(['UDABOL Unversidad de Aquino Bolivia '])
        self.cmbUniversidad.pack_start(self.cell, True)
        self.cmbUniversidad.add_attribute(self.cell,'text',0)"""
        self.lista_siglas = []

    def show(self):
        self.winPlanHorario1.show_all()

    def destroy(self, data=None):
        self.winPlanHorario1.hide()
    
    # Manejadores.
    def on_cmbUniversidad_changed(self, combo=None):
        print("cmbUniversidad cambiado, active: " + str(combo.get_active()))

        ## TODO: Capturar el valor seleccionado en la variable universidad
        self.universidad = combo.child.get_text()
        print(self.universidad)
        # mod = combo.get_model()
        # print mod[combo.get_active()][0]

    def on_cmbFacultad_changed(self, combo=None):
        print("cmbFacultad cambiado, active: " + str(combo.get_active()))
	    
    def on_plan1_btnCerrar_clicked(self, btn=None):
        self.destroy()
	
    def on_plan1_btnAtras_clicked(self, btn=None):
        self.destroy()
    
    def on_plan1_btnSiguiente_clicked(self, btn=None):
        self.destroy()
        WinPlanHorario2(self.lista_siglas).show()

    list_siglas = [] # Lista de SIGLAS de las materias elegidas en el Treeview derecho.

class WinPlanHorario2(GladeConnect):
    def __init__(self, lista_siglas):
        GladeConnect.__init__(self, 'main.glade', 'winPlanHorario2')
        self.iniciar_treeviews()
        self.__lista_siglas = lista_siglas
    
    def iniciar_treeviews(self):
        """ Carga los nombres de las materias y sus siglas en el TreeView de materias disponibles. """
        ## TODO: hacer global la variable list_siglas.
        self.renderer = gtk.CellRendererText()
        self.modeloDisp = gtk.ListStore(str, str) # modelo para trvwMateriasDisp.
        self.modeloEleg = gtk.ListStore(str, str) # modelo para trvwMateriasEleg.
        
        self.trvwMateriasDisp.set_model(self.modeloDisp)
        self.trvwMateriasEleg.set_model(self.modeloEleg)
        
        self.colDisp1 = gtk.TreeViewColumn('Materia', self.renderer, text=0)
        self.colDisp2 = gtk.TreeViewColumn('Sigla', self.renderer, text=1)
        
        self.colEleg1 = gtk.TreeViewColumn('Materia', self.renderer, text=0)
        self.colEleg2 = gtk.TreeViewColumn('Sigla', self.renderer, text=1)
        
        self.trvwMateriasDisp.append_column(self.colDisp1)
        self.trvwMateriasDisp.append_column(self.colDisp2)
        
        self.trvwMateriasEleg.append_column(self.colEleg1)
        self.trvwMateriasEleg.append_column(self.colEleg2)	
        
        # self.modeloDisp.clear()
        # col = self.trvwMateriasDisp.get_column(0)
        # print col
        
        # Obtiene las materias y siglas del archivo.
        f = open("materias_informatica.txt", 'r')
        for linea in f:
            
            s1 = linea.split('\t')
            materia = s1[0]
            sigla = s1[-1].strip('\n()')
            print(materia)
            print(sigla)
            iter = self.modeloDisp.append()
            self.modeloDisp.set(iter, 0, materia)
            self.modeloDisp.set(iter, 1, sigla)
            # self.list_siglas.append(self.sigla)
    
    def show(self):
        self.winPlanHorario2.show_all()
    
    def destroy(self, data=None):
        self.winPlanHorario2.hide()
    
    # Manejadores.
    def on_trvwMateriasDisp_cursor_changed(self, trvw=None):
        trvwCol = trvw.get_cursor()
        print(trvwCol)
	
    # OBTIENE LA FILA DE UN TREE VIEW
    def list_cero_a(self, num_lim):
        L = []
        for i in range(num_lim):
            L.append(i)
        return L

    def obtener_fila_tv(self, tree_view, cols = 2):
        treeselection = tree_view.get_selection()
        t_sel = treeselection.get_selected()
        return tree_view.get_model().get(t_sel[1], *self.list_cero_a(cols))
    
    def on_plan2_btnAgregar_clicked(self, btn=None):
        """ Evento donde agrega materias al TreeView derecho."""

        ## TODO: Obtener fila seleccionada
        tupla = self.obtener_fila_tv(self.trvwMateriasDisp)
        self.modeloEleg.append(list(tupla))
        self.__lista_siglas.append(tupla[1])
        #
        treeselection = self.trvwMateriasDisp.get_selection()
        t_sel = treeselection.get_selected()
        self.trvwMateriasDisp.get_model().remove(t_sel[1])

    def on_plan2_btnQuitar_clicked(self, btn=None):
        tupla = self.obtener_fila_tv(self.trvwMateriasEleg)
        self.trvwMateriasDisp.get_model().append(list(tupla))
        try:
            self.__lista_siglas.remove(tupla[1])
        except:
            print("errorrrrr")
            pass
        #
        treeselection = self.trvwMateriasEleg.get_selection()
        t_sel = treeselection.get_selected()
        self.trvwMateriasEleg.get_model().remove(t_sel[1])
    
    def on_plan2_btnCerrar_clicked(self, btn=None):
        self.destroy()
	
    def on_plan2_btnAtras_clicked(self, btn=None):
        ## TODO: actualizar formulario winPlanHorario1.
        self.destroy()
    
    def on_plan2_btnFin_clicked(self, btn=None):
        ## TODO: generar Horario.
        WinPlanHorario3(self.__lista_siglas).show()
        self.destroy()

from mi import CMotorInferencia
from utils import *
from control_se import *
from utils import UADMDB
import rhorario
	
class WinPlanHorario3(GladeConnect):
  
    def __init__(self, lista_siglas):
        GladeConnect.__init__(self, 'main.glade', 'winPlanHorario3')
        self.__lista_siglas = lista_siglas
        self.iniciar()
        
    def iniciar(self):
        self.cbc = CBc()
        self._mi = CMotorInferencia(self.cbc.obtener_bc_())
        self._mi.agregar_hecho2('contexto', 'nombre', 'planificacion')
        self._mi.agregar_hecho2('accion', 'accion', 'None')
        self.cplanif = CPlanifHorario()
        self.__cur_turno = None
        self.cargar_ch()
	 
    def show(self):
        self.winPlanHorario3.show_all()
    
    def destroy(self, data=None):
        self.winPlanHorario3.hide()
    
    def on_plan3_btnAyuda_clicked(self, btn=None):
        pass
	
    def on_plan3_btnGenerar_clicked(self, btn=None):
        ## TODO: Generar Horario.
        print(self.cplanif.get_materias_ch())
        self.set_preferencia()
        self.establecer_materias()
        self._mi.fwc() # AQUI SE PONE EN MARCHA EL MOTOR INFERENCIA
        rhorario.mostrar_horario(self.cplanif.obtener_matriz_horario_res())
        self.destroy()
	
    def cargar_ch(self):
        db = UADMDB()
        carga_horaria = db.obtener('archivos/carga_horaria.t')
        self.cplanif.set_materias_ch(carga_horaria)
	
    def establecer_materias(self):
        if self.__cur_turno:
            self.cplanif.establecer_materias(self.__lista_siglas, self.__cur_turno)
	
    def set_preferencia(self):
        if self.rdbtnCompactoDia.get_active():
            self.set_compacto_dia()
        elif self.rdbtnCompactoTarde.get_active():
            self.set_compacto_tarde()
        elif self.rdbtnCompactoNoche.get_active():
            self.set_compacto_noche()
        elif self.rdbtnDispersoDia.get_active():
            pass
        elif self.rdbtnDispersoTarde.get_active():
            pass
        else:
            pass
	
    def set_compacto_dia(self):
        self._mi.agregar_hecho2('restriccion_ph', 'positivo', 'True')
        self._mi.agregar_hecho2('restriccion_ph', 'turno', 'maniana')
        self._mi.agregar_hecho2('materia_ph', 'turno', 'maniana')
        self.__cur_turno = 'maniana'
	
    def set_compacto_tarde(self):
        self._mi.agregar_hecho2('restriccion_ph', 'positivo', 'True')
        self._mi.agregar_hecho2('restriccion_ph', 'turno', 'tarde')
        self._mi.agregar_hecho2('materia_ph', 'turno', 'tarde')
        self.__cur_turno = 'tarde'
	
    def set_compacto_noche(self):
        self._mi.agregar_hecho2('restriccion_ph', 'positivo', 'True')
        self._mi.agregar_hecho2('restriccion_ph', 'turno', 'noche')
        self._mi.agregar_hecho2('materia_ph', 'turno', 'noche')
        self.__cur_turno = 'noche'
	
	
    def on_rdbtnCompactoDia_group_changed(self, rdbtn=None):
        print(rdbtn)
    
    def on_rdbtnCompactoTarde_toggled(self, *args):
        pass

class DlgAbout(GladeConnect):
    def __init__(self):
        GladeConnect.__init__(self, 'main.glade', 'dlgAbout')
    
    def show(self):
        self.dlgAbout.show()
