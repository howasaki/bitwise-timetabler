from frame import *
from bc import *
from bh import *
from mi import *

#CREACION DE FRAME: INICIO
slot_nombre_contexto = Slot('nombre', T)
slot_nombre_contexto.set_valor('planificacion')

contexto = Frame('contexto', [slot_nombre_contexto])

slot_accion_accion = Slot('accion', T)
slot_accion_accion.set_valor('None')
accion = Frame('accion', [slot_accion_accion])

slot_positivo_restr = Slot('positivo', T)
slot_positivo_restr.set_valor('True')
slot_turno_restr = Slot('turno', T)
slot_turno_restr.set_valor('maniana')
restriccion = Frame('restriccion', [slot_positivo_restr, slot_turno_restr])

slot_ubicar_ok_aux = Slot('ubicar_ok', T)
slot_ubicar_ok_m_aux = Slot('ubicar_ok_m', T)
slot_ubicar_ok_t_aux = Slot('ubicar_ok_t', T)
slot_ubicar_ok_n_aux = Slot('ubicar_ok_n', T)
auxiliar = Frame('auxiliar', [slot_ubicar_ok_aux, slot_ubicar_ok_m_aux, slot_ubicar_ok_t_aux, slot_ubicar_ok_n_aux])

slot_sigla_mat = Slot('sigla', T)
slot_sigla_mat.set_valor('INF428')
slot_grupo_mat = Slot('grupo', T)
slot_grupo_mat.set_valor('SB')
slot_aula_mat = Slot('aula', T)
slot_aula_mat.set_valor('214-23')
slot_hor_mat = Slot('horario', D)
slot_hor_mat.set_valor({1: [3,4], 3: [3,4], 5: [3,4]})
slot_turno_mat = Slot('turno', T)
materia = Frame('materia', [slot_sigla_mat, slot_grupo_mat, slot_aula_mat, slot_hor_mat, slot_turno_mat])

slot_id_hor = Slot('id', N)
slot_id_hor.set_valor(1)
slot_hor_hor = Slot('horario', D)
slot_hor_hor.set_valor({1: [3,4], 2: [5,6,7], 3: [3,4], 4: [5,6,7], 5: [3,4]})
#CREACION DE FRAME: FIN

#CREACION DE REGLAS: INICIO
#Metarregla
r1 = Regla(True)
r1.set_nombre('r1')
r1.set_premisa([Cuadrupla(False, slot_nombre_contexto, IGUAL, 'planificacion'), Cuadrupla(False, slot_accion_accion, IGUAL, 'None')])
r1.set_conclusion(Hecho(slot_accion_accion, 'cargar'))
print r1.to_str()

r2 = Regla(True)
r2.set_nombre('r2')
r2.set_premisa([Cuadrupla(False, slot_nombre_contexto, IGUAL, 'planificacion'), Cuadrupla(False, slot_accion_accion, IGUAL, 'asignar')])
r2.set_conclusion(Hecho(slot_accion_accion, 'cargar'))
print r2.to_str()

r3 = Regla(True)
r3.set_nombre('r3')
r3.set_premisa([Cuadrupla(False, slot_nombre_contexto, IGUAL, 'planificacion'), Cuadrupla(False, slot_positivo_restr, IGUAL, 'True')])
r3.set_conclusion(Hecho(slot_ubicar_ok_aux, 'True'))
print r3.to_str()