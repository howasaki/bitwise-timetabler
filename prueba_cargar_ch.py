import control_se
from utils import *

#dict_materia = {'sigla':'INF428', 'grupo': 'SB', 'horario': {1: [3,4], 3: [3,4], 5: [3,4]}, 'turno': 'maniana'}

"""
DIAS:
Lunes : 1
Martes : 2
...

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

def execute():
    cplanif = control_se.CPlanifHorario()
    
    cplanif.agregar_materia_ch('FIS100', 'SW', {1: [14,15], 3: [14,15], 5: [14,15,16,17]})
    cplanif.agregar_materia_ch('FIS100', 'SX', {2: [1,2,3,8,9], 4: [1,2,3]})
    cplanif.agregar_materia_ch('FIS100', 'SY', {1: [14,15], 2: [1,2,3], 4: [1,2,3]})
    
    cplanif.agregar_materia_ch('INF110', 'SC', {1: [14,15], 3: [14,15], 5: [14,15]})
    cplanif.agregar_materia_ch('INF110', 'SD', {4: [9,10], 5: [9,10], 6: [5,6]})
    cplanif.agregar_materia_ch('INF110', 'SE', {1: [16,17], 3: [16,17], 5: [16,17]})
    cplanif.agregar_materia_ch('INF110', 'SF', {2: [7,8,9], 4: [7,8,9]})
    cplanif.agregar_materia_ch('INF110', 'SH', {2: [12,13], 4: [12,13], 5: [12,13]})
    cplanif.agregar_materia_ch('INF110', 'SI', {3: [16,17,18], 5: [16,17,18]})
    cplanif.agregar_materia_ch('INF110', 'SW', {1: [10,11], 3: [10,11], 5: [10,11]})
    cplanif.agregar_materia_ch('INF110', 'SX', {1: [3,4], 3: [3,4], 5:[3,4]})
    cplanif.agregar_materia_ch('INF110', 'SY', {1: [5,6,7], 3: [5,6,7]})
    cplanif.agregar_materia_ch('INF110', 'SZ', {2: [3,4], 4: [3,4], 5: [5,6]})
    
    cplanif.agregar_materia_ch('INF119', 'SA', {1: [1,2], 3: [1,2], 5: [1,2]})
    cplanif.agregar_materia_ch('INF119', 'SE', {1: [7,8], 3: [7,8], 5: [7,8]})
    cplanif.agregar_materia_ch('INF119', 'SF', {2: [1,2], 6: [1,2,3,4]})
    cplanif.agregar_materia_ch('INF119', 'SG', {1: [7,8], 3: [7,8], 5:[7,8]})
    cplanif.agregar_materia_ch('INF119', 'SH', {2: [8,9], 3: [8,9], 5: [8,9]})
    cplanif.agregar_materia_ch('INF119', 'SJ', {2: [3,4], 4: [3,4], 6: [3,4]})
    cplanif.agregar_materia_ch('INF119', 'SW', {1: [12,13], 3: [12,13], 5: [12,13]})
    cplanif.agregar_materia_ch('INF119', 'SX', {1: [1,2], 3: [1,2], 5: [1,2]})
    cplanif.agregar_materia_ch('INF119', 'SY', {1: [3,4], 3: [3,4], 5: [3,4]})
    
    cplanif.agregar_materia_ch('LIN100', 'SB', {1: [3,4], 3: [3,4], 5: [3,4]})
    cplanif.agregar_materia_ch('LIN100', 'SF', {1: [7,8], 3: [7,8], 5: [7,8]})
    cplanif.agregar_materia_ch('LIN100', 'SG', {2: [10,11,12], 4: [10,11,12]})
    cplanif.agregar_materia_ch('LIN100', 'SI', {2: [13,14,15], 4: [13,14,15]})
    cplanif.agregar_materia_ch('LIN100', 'SW', {2: [10,11,12], 4: [10,11,12]})
    cplanif.agregar_materia_ch('LIN100', 'SX', {1: [5,6], 3: [5,6], 5: [5,6]})
    cplanif.agregar_materia_ch('LIN100', 'SY', {2: [4,5,6], 4: [4,5,6]})
    
    cplanif.agregar_materia_ch('MAT101', 'SW', {2: [13,14,15], 4: [13,14,15]})
    cplanif.agregar_materia_ch('MAT101', 'SX', {2: [4,5,6], 4: [4,5,6]})
    cplanif.agregar_materia_ch('MAT101', 'SY', {1: [1,2], 3: [1,2], 5: [1,2]})
    
    cplanif.agregar_materia_ch('INF120', 'SB', {2: [1,2,3], 4: [1,2,3]})
    cplanif.agregar_materia_ch('INF120', 'SC', {1: [14,15], 3: [14,15], 5: [14,15]})
    cplanif.agregar_materia_ch('INF120', 'SD', {1: [14,15], 3: [14,15], 5: [14,15]})
    cplanif.agregar_materia_ch('INF120', 'SE', {2: [16,17,18], 4: [16,17,18]})
    cplanif.agregar_materia_ch('INF120', 'SF', {1: [14,15], 3: [14,15], 5: [14,15]})
    
    #db = UADMDB()
    #db.guardar(cplanif.get_materias_ch(), 'archivos/carga_horaria.t')
    
    #print cplanif.ch_materias_to_str()
    
    #print cplanif.get_materias_sel()
    import pickle
    #pickle.dump(cplanif.get_materias_ch(), open('prueeba.t', 'w'))
    carga_h = pickle.load(open('prueeba.t'))
    print carga_h
    
execute()
    