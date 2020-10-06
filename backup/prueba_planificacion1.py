from frame import *
from bc import *
from bh import *
from mi import *
from utils import *
from control_se import *

#-----------------------------------------------------------------
#---- PRUEBA PARA LA PLANIFICACION DE HORARIOS UNIVERSITARIOS ----
#-----------------------------------------------------------------

cbc = CBc()

#||||||||||||||||||||||||||||
#CREACION DE FRAMES -> INICIO

#FRAME contexto (inicio)
frm_contexto = Frame('contexto')

slot1 = Slot('nombre', T)
slot1.set_rango(['prioridad', 'asignacion', 'restriccion', 'cambio de asignacion'])

frm_contexto.agregar_slot(slot1)
cbc.insertar_frame(frm_contexto)
#FRAME contexto (fin)

#FRAME accion (inicio)
frm_accion = Frame('accion')

slot2 = Slot('accion', T)
slot2.set_rango(['buscar', 'cargar', 'vaciar', 'asignar', 'verificar_restr', 'asignar_a_ch', 'None'])
slot2.set_metodo(WHEN_CHANGED)
frm_accion.agregar_slot(slot2)

cbc.insertar_frame(frm_accion)
#FRAME accion (fin)

#FRAME restriccion_ph (inicio)
frm_restriccion_ph = Frame('restriccion_ph')

slot3 = Slot('positivo', T)
slot3.set_rango(['True', 'False'])
frm_restriccion_ph.agregar_slot(slot3)

slot4 = Slot('turno', T)
slot4.set_rango(['maniana', 'tarde', 'noche'])
frm_restriccion_ph.agregar_slot(slot4)

cbc.insertar_frame(frm_restriccion_ph)
#FRAME restriccion_ph (fin)

#FRAME bandera (inicio)
frm_bandera = Frame('bandera')

slot5 = Slot('ubicar_ok', T)
slot5.set_rango(['True', 'False'])
frm_bandera.agregar_slot(slot5)

slot6 = Slot('ubicar_ok_m', T)
slot6.set_rango(['True', 'False'])
frm_bandera.agregar_slot(slot6)

slot7 = Slot('ubicar_ok_t', T)
slot7.set_rango(['True', 'False'])
frm_bandera.agregar_slot(slot7)

slot8 = Slot('ubicar_ok_n', T)
slot8.set_rango(['True', 'False'])
frm_bandera.agregar_slot(slot8)

slot9 = Slot('hay_materias', T)
slot9.set_rango(['True', 'False'])
frm_bandera.agregar_slot(slot9)

slot10 = Slot('falta_asignar_mat_gr', T)
slot10.set_rango(['True', 'False'])
frm_bandera.agregar_slot(slot10)

slot11 = Slot('cumple_restricciones', T)
slot11.set_rango(['True', 'False'])
frm_bandera.agregar_slot(slot11)

slot12 = Slot('asignacion_completa', T)
slot12.set_rango(['True', 'False'])
frm_bandera.agregar_slot(slot12)

cbc.insertar_frame(frm_bandera)
#FRAME bandera (fin)

#FRAME materia_ph (inicio)
frm_materia_ph = Frame('materia_ph')

slot13 = Slot('sigla', T)
frm_materia_ph.agregar_slot(slot13)

slot14 = Slot('grupo', T)
frm_materia_ph.agregar_slot(slot14)

slot15 = Slot('aula', T)
frm_materia_ph.agregar_slot(slot15)

slot16 = Slot('horario', D)
frm_materia_ph.agregar_slot(slot16)

slot17 = Slot('turno', T)
slot17.set_rango(['maniana', 'tarde', 'noche', 'disperso'])
slot17.set_metodo(WHEN_CHANGED)
frm_materia_ph.agregar_slot(slot17)

cbc.insertar_frame(frm_materia_ph)
#FRAME materia_ph (fin)

#FRAME horario_ph (inicio)
frm_horario_ph = Frame('horario_ph')

slot18 = Slot('id', N)
frm_horario_ph.agregar_slot(slot18)

slot19 = Slot('horario', D)
frm_horario_ph.agregar_slot(slot19)

cbc.insertar_frame(frm_horario_ph)
#FRAME horario_ph (fin)

#CREACION DE FRAMES -> FIN
#||||||||||||||||||||||||||||

#||||||||||||||||||||||||||||
#CREACION DE REGLAS 

cbc.nueva_regla(True)
cbc.establecer_nombre_regla('regla_ph_1_m')
cbc.insertar_literal(False, 'contexto', 'nombre', IGUAL, 'planificacion')
cbc.insertar_literal(False, 'accion', 'accion', IGUAL, 'None')
cbc.establecer_conclusion('accion', 'accion', 'cargar')
cbc.guardar_regla()

cbc.nueva_regla(True)
cbc.establecer_nombre_regla('regla_ph_2_m')
cbc.insertar_literal(False, 'contexto', 'nombre', IGUAL, 'planificacion')
cbc.insertar_literal(False, 'accion', 'accion', IGUAL, 'asignar')
cbc.establecer_conclusion('accion', 'accion', 'cargar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_3')
cbc.insertar_literal(False, 'contexto', 'nombre', IGUAL, 'planificacion')
cbc.insertar_literal(False, 'restriccion_ph', 'positivo', IGUAL, 'True')
cbc.establecer_conclusion('bandera', 'ubicar_ok', 'True')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_4')
cbc.insertar_literal(False, 'contexto', 'nombre', IGUAL, 'planificacion')
cbc.insertar_literal(False, 'restriccion_ph', 'positivo', IGUAL, 'False')
cbc.establecer_conclusion('bandera', 'ubicar_ok', 'False')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_5')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok', IGUAL, 'True')
cbc.insertar_literal(False, 'restriccion_ph', 'turno', IGUAL, 'maniana')
cbc.establecer_conclusion('bandera', 'ubicar_ok_m', 'True')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_6')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok', IGUAL, 'True')
cbc.insertar_literal(False, 'restriccion_ph', 'turno', IGUAL, 'tarde')
cbc.establecer_conclusion('bandera', 'ubicar_ok_t', 'True')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_7')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok', IGUAL, 'True')
cbc.insertar_literal(False, 'restriccion_ph', 'turno', IGUAL, 'noche')
cbc.establecer_conclusion('bandera', 'ubicar_ok_n', 'True')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_8')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok', IGUAL, 'False')
cbc.insertar_literal(False, 'restriccion_ph', 'turno', IGUAL, 'maniana')
cbc.establecer_conclusion('bandera', 'ubicar_ok_m', 'False')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_9')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok', IGUAL, 'False')
cbc.insertar_literal(False, 'restriccion_ph', 'turno', IGUAL, 'tarde')
cbc.establecer_conclusion('bandera', 'ubicar_ok_t', 'False')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_10')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok', IGUAL, 'False')
cbc.insertar_literal(False, 'restriccion_ph', 'turno', IGUAL, 'noche')
cbc.establecer_conclusion('bandera', 'ubicar_ok_n', 'False')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_11')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_m', IGUAL, 'True')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'maniana')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_12')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_t', IGUAL, 'True')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'tarde')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_13')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_n', IGUAL, 'True')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'noche')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_15')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_m', IGUAL, 'False')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'tarde')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_16')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_m', IGUAL, 'False')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'noche')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_17')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_t', IGUAL, 'False')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'maniana')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_18')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_t', IGUAL, 'False')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'noche')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_19')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_n', IGUAL, 'False')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'maniana')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_20')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok_n', IGUAL, 'False')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'tarde')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_21')
cbc.insertar_literal(False, 'bandera', 'ubicar_ok', IGUAL, 'True')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'disperso')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

cbc.nueva_regla()
cbc.establecer_nombre_regla('regla_ph_22')
cbc.insertar_literal(False, 'accion', 'accion', IGUAL, 'cargar')
cbc.insertar_literal(False, 'materia_ph', 'turno', IGUAL, 'disperso')
cbc.establecer_conclusion('accion', 'accion', 'asignar')
cbc.guardar_regla()

print cbc.reglas_to_str()
