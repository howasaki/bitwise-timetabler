from frame import *
from bc import *
from bh import *
from mi import *
 
#CREACION DE FRAME: INICIO
slot_nombre = Slot('nombre', T)
slot_nombre.set_rango(['Prioridad', 'Asignacion', 'Restriccion', 'Cambio de Asignacion'])
slot_nombre.set_valor('Prioridad')
slot_nombre.set_default('Prioridad')

slot_ok = Slot('ok', T)
slot_ok.set_rango(['True', 'False'])
slot_ok.set_valor('True')
slot_ok.set_default('True')

#contexto = Frame('Contexto', [slot_nombre, slot_ok])

contexto = Frame('Contexto')
contexto.agregar_slot(slot_nombre)
contexto.agregar_slot(slot_ok)
print contexto.to_str()


slot_regla_activa = Slot('nombre', T)
slot_regla_activa.set_valor('Nada')
regla_activa = Frame('Regla_activa', [slot_regla_activa])

slot_regla_activa2 = Slot('nombre', T)
slot_regla_activa2.set_valor('Nada')
regla_activa2 = Frame('Regla_activa2', [slot_regla_activa2])

#print contexto.to_str()
#CREACION DE FRAME: FIN

#CREACION DE REGLAS DE CONTEXTO: INICIO
r1 = Regla(True)
r1.set_nombre('r1')
r1.set_premisa([Cuadrupla(False, slot_nombre, IGUAL, 'Prioridad')])
r1.set_conclusion(Hecho(slot_nombre, 'Asignacion'))
print r1.to_str()

r2 = Regla(True)
r2.set_nombre('r2')
r2.set_premisa([Cuadrupla(False, slot_nombre, IGUAL, 'Asignacion')])
r2.set_conclusion(Hecho(slot_nombre, 'Restriccion'))
print r2.to_str()

#CREACION DE REGLAS DE CONTEXTO: FIN

r3 = Regla()
r3.set_nombre('regla_prioridad1')
r3.set_premisa([Cuadrupla(False, slot_nombre, IGUAL, 'Prioridad'), Cuadrupla(False, slot_regla_activa, IGUAL, 'Nada')])
r3.set_conclusion(Hecho(slot_regla_activa2, 'ReglaPrioridad'))
print r3.to_str()

r5 = Regla()
r5.set_nombre('regla_asignacion1')
r5.set_premisa([Cuadrupla(False, slot_nombre, IGUAL, 'Asignacion'), Cuadrupla(False, slot_regla_activa, IGUAL, 'Nada')])
r5.set_conclusion(Hecho(slot_regla_activa2, 'ReglaAsignacion a partir de Nada'))
print r5.to_str()

r6 = Regla()
r6.set_nombre('regla_asignacion2')
#r6.set_premisa([Cuadrupla(False, slot_nombre, IGUAL, 'Asignacion'), Cuadrupla(False, slot_regla_activa, IGUAL, 'ReglaPrioridad')])
r6.insertar_literal(Cuadrupla(False, slot_nombre, IGUAL, 'Asignacion'))
r6.insertar_literal(Cuadrupla(False, slot_regla_activa, IGUAL, 'ReglaPrioridad'))
r6.set_conclusion(Hecho(slot_regla_activa2, 'ReglaAsignacion a partir de Prioridad'))
print r6.to_str()

_bc = BC()
_bc.set_slots([slot_nombre, slot_ok, slot_regla_activa, slot_regla_activa2])
_bc.set_reglas([r1, r3, r5, r6])

_bh = BH()
_bh.set_hechos([Hecho(slot_nombre, 'Prioridad'), Hecho(slot_regla_activa, 'Nada')])

_mi = CMotorInferencia(_bc, _bh)
unificados = _mi.fwc()

print _bh.to_str()

