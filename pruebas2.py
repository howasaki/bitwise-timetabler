"""
Plantilla Materia: Ejemplo
materia = {'sigla': 'INF521', 'nombre':'Taller de Gado I', 'nivel': 9, 'sem':1, 'gest':2008, 'cred':5, 'por_asignar':4,
           'prerreq':['INF510','INF512'], 'educador':'Ing. Rolando martinez', 'tipo':'troncal', 'horario':<EstructuraHorario>}
    
'por_asignar' -> El numero de periodos que falta asignar
'tipo' -> Si es Troncal, No Troncal u Optativa
'horario' -> Diccionario que representa a la plantilla horario, que se explica a continuacion

Plantilla Horario: Ejemplo
horario =  {'grupo':'sa',
               'carrera':'Ingenieria Informatica',
               #         L    M    X    J    V    S    D
               'hor': [ 'v', 'v', 'v', 'v', 'v', 'v', 'v',   # 07:00 
                        'v', 'v', 'v', 'v', 'v', 'v', 'v',   # 07:45
                        'v', 'v', 'v', 'v', 'v', 'v', 'v',   # 08:30
                        'v', 'v', 'v', 'v', 'v', 'v', 'v',   # 09:15
                        'v', 'v', 'v', 'v', 'v', 'v', 'v',   # 10:00
                        'v', 'v', 'v', 'v', 'v', 'v', 'v']   # 10:45  ...
                
            }
"""