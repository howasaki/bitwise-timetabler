from control_se import CPlanifHorario
from bc import *
import ucommoniu

cplanif = CPlanifHorario()
regla = Regla()


titulo_msg = 'Planificacion de horarios'
msg_fallo_m = 'La materia %s no se pudo asignar al grupo %s en la maniana. Intentar con otro grupo en el mismo turno y/o asignar en cualquier otro turno?'
msg_fallo_t = 'La materia %s no se pudo asignar al grupo %s en la tarde. Intentar con otro grupo en el mismo turno y/o asignar en cualquier otro turno?'
msg_fallo_n = 'La materia %s no se pudo asignar al grupo %s en la noche. Intentar con otro grupo en el mismo turno y/o asignar en cualquier otro turno?'
msg_fallo_nm = 'La materia %s no se pudo asignar en la tarde o la noche. Intentar asignar en la maniana?'
msg_fallo_nt = 'La materia %s no se pudo asignar en la maniana o la noche. Intentar asignar en la tarde?'
msg_fallo_nn = 'La materia %s no se pudo asignar en la maniana o la tarde. Intentar asignar en la noche?'

def show_y_n_msg(msg):
    return ucommoniu.show_yes_no_message(None, titulo_msg, msg)

def ejecutar(nombre_metodo):
    return eval(nombre_metodo, globals(), locals())
    
#dict_materia = {'sigla':'INF428', 'grupo': 'SB', 'horario': {1: [3,4], 3: [3,4], 5: [3,4]}, 'turno': 'maniana'}


class CurrentMateria:
    def __init__(self, materia):
        """materia -> dict_materia"""
        self.current_materia = materia

c_materia = CurrentMateria(None)
        
def cargar_siguiente_materia():
    try:
        return cplanif.obtener_siguiente_materia()
    except:
        return []
    
def asignar_materia_t_maniana():
    """Asigna la materia si o si en la maniana"""
    turno = c_materia.current_materia['turno']
    sigla_materia = c_materia.current_materia['sigla']
    grupo_materia = c_materia.current_materia['grupo']
    if turno == 'maniana':
        if not cplanif.intentar_asignacion(sigla_materia, grupo_materia):
            if not cplanif.hay_mas_grupos(sigla_materia, turno):
                return show_fallo(msg_fallo_m, sigla_materia, grupo_materia)
    elif not cplanif.materia_asignada(sigla_materia) and not cplanif.hay_mas_grupos(sigla_materia, 'maniana'):
        return show_fallo(msg_fallo_n, sigla_materia, grupo_materia)

def asignar_materia_t_tarde():
    """Asigna la materia si o si en la tarde"""
    turno = c_materia.current_materia['turno']
    sigla_materia = c_materia.current_materia['sigla']
    grupo_materia = c_materia.current_materia['grupo']
    if turno == 'tarde':
        if not cplanif.intentar_asignacion(sigla_materia, grupo_materia):
            if not cplanif.hay_mas_grupos(sigla_materia, turno):
                return show_fallo(msg_fallo_t, sigla_materia, grupo_materia)
    elif not cplanif.materia_asignada(sigla_materia) and not cplanif.hay_mas_grupos(sigla_materia, 'tarde'):
        return show_fallo(msg_fallo_n, sigla_materia, grupo_materia)

def asignar_materia_t_noche():
    """Asigna la materia si o si en la noche"""
    turno = c_materia.current_materia['turno']
    sigla_materia = c_materia.current_materia['sigla']
    grupo_materia = c_materia.current_materia['grupo']
    if turno == 'noche':
        if not cplanif.intentar_asignacion(sigla_materia, grupo_materia):
            if not cplanif.hay_mas_grupos(sigla_materia, turno):
                return show_fallo(msg_fallo_n, sigla_materia, grupo_materia)
    elif not cplanif.materia_asignada(sigla_materia) and not cplanif.hay_mas_grupos(sigla_materia, 'noche'):
        return show_fallo(msg_fallo_n, sigla_materia, grupo_materia)

def show_fallo(msg, sigla, grupo):
    opcion = show_y_n_msg(msg % (sigla, grupo))
    if opcion:
        return asignar_materia_disperso()

def asignar_materia_disperso():
    """Asigna la materia a donde entre"""
    #turno = c_materia.current_materia['turno']
    #if turno == 'disperso':
    return cplanif.intentar_asignacion(c_materia.current_materia['sigla'], c_materia.current_materia['grupo'])
    #return False
    
def asignar_no_maniana():
    if not asignar_materia_t_tarde():
        return asignar_materia_t_noche()
    return True
    
def asignar_no_tarde():
    if not asignar_materia_t_maniana():
        return asignar_materia_t_noche()
    return True

def asignar_no_noche():
    if not asignar_materia_t_maniana():
        return asignar_materia_t_tarde()
    return True
    
def asignar_materia(regla):
    dict_frm_slot_val = {}
    if isinstance(regla, Regla):
        for literal in regla.get_premisa():
            if literal.get_oprel() == IGUAL and not literal.get_no():
                nombre_f = literal.nombre_frame
                nombre_s = literal.nombre_slot
                dict_frm_slot_val['%s.%s' % (nombre_f, nombre_s)] = literal.get_valor()
            
        if 'bandera.ubicar_ok_m' in dict_frm_slot_val.keys() and 'materia_ph.turno' in dict_frm_slot_val.keys():
            val1 = dict_frm_slot_val['bandera.ubicar_ok_m']
            val2 = dict_frm_slot_val['materia_ph.turno']
            if val1 == 'True' and val2 == 'maniana':
                return asignar_materia_t_maniana()
            elif val1 == 'False':
                #print 'ASIGNANDO HORARIOS EN CUALQUIER TURNO MENOS EN LA MANIANA'
                if not asignar_no_maniana():
                    pass
                    #opcion = show_y_n_msg(msg_fallo_nm % c_materia.current_materia['sigla'])
                    #if opcion:
                    #    asignar_materia_disperso()
        elif 'bandera.ubicar_ok_t' in dict_frm_slot_val.keys() and 'materia_ph.turno' in dict_frm_slot_val.keys():
            val1 = dict_frm_slot_val['bandera.ubicar_ok_t']
            val2 = dict_frm_slot_val['materia_ph.turno']
            if val1 == 'True' and val2 == 'tarde':
                return asignar_materia_t_tarde()
            elif val1 == 'False':
                #print 'ASIGNANDO HORARIOS EN CUALQUIER TURNO MENOS EN LA TARDE'
                if not asignar_no_tarde():
                    pass
                    #opcion = show_y_n_msg(msg_fallo_nt % c_materia.current_materia['sigla'])
                    #if opcion:
                    #    asignar_materia_disperso()
        elif 'bandera.ubicar_ok_n' in dict_frm_slot_val.keys() and 'materia_ph.turno' in dict_frm_slot_val.keys():
            val1 = dict_frm_slot_val['bandera.ubicar_ok_n']
            val2 = dict_frm_slot_val['materia_ph.turno']
            if val1 == 'True' and val2 == 'noche':
                return asignar_materia_t_noche()
            elif val1 == 'False':
                #print 'ASIGNANDO HORARIOS EN CUALQUIER TURNO MENOS EN LA NOCHE'
                if not asignar_no_noche():
                    pass
                    #opcion = show_y_n_msg(msg_fallo_nn % c_materia.current_materia['sigla'])
                    #if opcion:
                    #    asignar_materia_disperso()
        elif 'bandera.ubicar_ok' in dict_frm_slot_val.keys() and 'materia_ph.turno' in dict_frm_slot_val.keys():
            val1 = dict_frm_slot_val['bandera.ubicar_ok']
            val2 = dict_frm_slot_val['materia_ph.turno']
            if val1 == 'True' and val2 == 'disperso':
                return asignar_materia_disperso()
        elif 'accion.accion'  in dict_frm_slot_val.keys() and 'materia_ph.turno' in dict_frm_slot_val.keys():
            val1 = dict_frm_slot_val['accion.accion']
            val2 = dict_frm_slot_val['materia_ph.turno']
            if val1 == 'cargar' and val2 == 'disperso':
                return asignar_materia_disperso()
    
def accion_accion_when_changed(regla, accion):
    #print 'hoola accion = %s, regla = %s ' % (accion, regla.get_nombre())
    if accion == 'buscar':
        pass
    elif accion == 'cargar':
        c_materia.current_materia = cargar_siguiente_materia()
        #print 'siguiente_materia -> %s' % c_materia.current_materia
        return c_materia.current_materia
    elif accion == 'vaciar':
        pass
    elif accion == 'asignar':
        am = asignar_materia(regla)
        #print 'DENTRO DE ASIGNAR MATERIA, RETORNO %s' % am
        return True
    elif accion == 'verificar_restr':
        pass
    elif accion == 'asignar_a_ch':
        pass
    else:
        pass
    

"""
PERIODOS:
turno 'maniana' -> 1 - 9
turno 'tarde' -> 10 - 15
turno 'noche' -> 16 - 21

periodo 1:  07:00 - 07:45
periodo 2:  07:45 - 08:30
periodo 3:  08:30 - 09:15
periodo 4:  09:15 - 10:00
periodo 5:  10:00 - 10:45
periodo 6:  10:45 - 11:30
periodo 7:  11:30 - 12:15
periodo 8:  12:15 - 13:00
periodo 9:  13:00 - 13:45

periodo 10: 14:00 - 14:45
periodo 11: 14:45 - 15:30
periodo 12: 15:30 - 16:15
periodo 13: 16:15 - 17:00
periodo 14: 17:00 - 17:45
periodo 15: 17:45 - 18:30

periodo 16: 18:30 - 19:15
periodo 17: 19:15 - 20:00
periodo 18: 20:00 - 20:45
periodo 19: 20:45 - 21:30
periodo 20: 21:30 - 22:15
periodo 21: 22:15 - 23:00
"""