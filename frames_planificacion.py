from frame import *
from bc import *
from bh import *
from mi import *
from utils import *
from control_se import *

cbc = CBc()

slot_nombre = Slot('nombre', T)
slot_nombre.set_rango(['Prioridad', 'Asignacion', 'Restriccion', 'Cambio de Asignacion'])
slot_nombre.set_valor('Prioridad')
slot_nombre.set_default('Prioridad')

slot_ok = Slot('ok', T)
slot_ok.set_rango(['True', 'False'])
slot_ok.set_valor('True')
slot_ok.set_default('True')

contexto = Frame('Contexto', [slot_nombre, slot_ok])
#
slot_regla_activa = Slot('nombre', T)
slot_regla_activa.set_valor('Nada')
regla_activa = Frame('Regla_activa', [slot_regla_activa])
#
slot_regla_activa2 = Slot('nombre', T)
slot_regla_activa2.set_valor('Nada')
regla_activa2 = Frame('Regla_activa2', [slot_regla_activa2])

#------------------------------------------------------------
cbc.insertar_frame(contexto)
cbc.insertar_frame(regla_activa)
cbc.insertar_frame(regla_activa2)

L = cbc.obtener_lista_frames()

for l in L:
    print l.get_nombre()
    
print ""

cbc.nueva_regla(True)
cbc.establecer_nombre_regla('r1')
cbc.insertar_literal(False, 'Contexto', 'nombre', IGUAL, 'Prioridad')
cbc.establecer_conclusion('Contexto', 'nombre', 'Asignacion')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_prioridad1')
cbc.insertar_literal(False, 'Contexto', 'nombre', IGUAL, 'Prioridad')
cbc.insertar_literal(False, 'Regla_activa', 'nombre', IGUAL, 'Nada')
cbc.establecer_conclusion('Regla_activa2', 'nombre', 'ReglaPrioridad')
cbc.guardar_regla()


cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_asignacion1')
cbc.insertar_literal(False, 'Contexto', 'nombre', IGUAL, 'Asignacion')
cbc.insertar_literal(False, 'Regla_activa', 'nombre', IGUAL, 'Nada')
cbc.establecer_conclusion('Regla_activa2', 'nombre', 'ReglaAsignacion a partir de Nada')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_asignacion2')
cbc.insertar_literal(False, 'Contexto', 'nombre', IGUAL, 'Asignacion')
cbc.insertar_literal(False, 'Regla_activa', 'nombre', IGUAL, 'ReglaPrioridad')
cbc.establecer_conclusion('Regla_activa2', 'nombre', 'ReglaAsignacion a partir de Prioridad')
cbc.guardar_regla()


print cbc.reglas_to_str()

_mi = CMotorInferencia(cbc.obtener_bc_())
_mi.agregar_hecho2('Contexto', 'nombre', 'Prioridad')
_mi.agregar_hecho2('Regla_activa', 'nombre', 'Nada')
_mi.fwc()

print _mi.get_bh().to_str()