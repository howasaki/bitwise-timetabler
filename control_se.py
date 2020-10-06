from frame import *
from bc import *
from bh import *
#from mi import *
from utils import *
import pickle

PATH_LFRAMES = 'archivos/frames.t'
PATH_BC = 'archivos/bc.t'

uarchivo_bc = UArchivoBC()

class CBc:
    
    def __init__(self):
        self.__frames = []
        self.__regla = Regla()
        self.__id_regla = -1
	self.__bc = BC()
        
    def nueva_regla(self, es_metarregla = False):
        self.__id_regla = -1
        self.__regla = Regla(es_metarregla)
	
    def __guardar_slots_de_frame(self, frame):
	if isinstance(frame, Frame):
	    if self.__obtener_bc():
		slots = self.__bc.get_slots()
		slots.extend(frame.get_slots())
		#uarchivo_bc.guardar_bc(self.__bc, PATH_BC)
		pickle.dump(self.__bc, open(PATH_BC, 'w'))
		
    def __actualizar_slots_bc(self):
	if self.__obtener_bc():
	    slots = []
	    for frame in self.__frames:
		slots.extend(frame.get_slots())
	    self.__bc.set_slots(slots)
	    #uarchivo_bc.guardar_bc(self.__bc, PATH_BC)
	    pickle.dump(self.__bc, open(PATH_BC, 'w'))
        
    def insertar_frame(self, frame):
        if isinstance(frame, Frame):
	    i = self.__buscar_frame(frame.get_nombre())
	    if i > -1:
		self.__frames[i] = frame
		self.__actualizar_slots_bc()
	    else:
		self.__frames.append(frame)
		self.__guardar_slots_de_frame(frame)
	    #uarchivo_bc.guardar_frames(self.__frames, PATH_LFRAMES)
	    pickle.dump(self.__frames, open(PATH_LFRAMES, 'w'))
        
    def borrar_frame(self, nombre_frame):
        if isinstance(nombre_frame, str):
            i = self.__buscar_frame(nombre_frame)
            if i > -1:
                del self.__frames[i]
                #uarchivo_bc.guardar_frames(self.__frames, PATH_LFRAMES)
		pickle.dump(self.__frames, open(PATH_LFRAMES, 'w'))
                return True
        return False
    
    def obtener_lista_frames(self):
        #return uarchivo_bc.obtener_frames(PATH_LFRAMES)
	return pickle.load(open(PATH_LFRAMES))
        
    def __buscar_frame(self, nombre_frame):
        #frames = uarchivo_bc.obtener_frames(PATH_LFRAMES)
	try:
	    frames = pickle.load(open(PATH_LFRAMES))
	except:
	    frames = None
        i = -1
        if frames:
            self.__frames = frames
            for f in self.__frames:
                i = i + 1
                if f.get_nombre() == nombre_frame:
                    return i
        return -1
    
    def establecer_nombre_regla(self, nombre):
        self.__regla.set_nombre(nombre)
        
    def es_regla_valida(self):
	return self.__regla is not None and self.__regla.cant_literales() > 0 and self.__regla.get_conclusion() is not None and not self.slot_en_premisa()
    
    def slot_en_premisa():
	for i in range(self.__regla.cant_literales()):
	    slot_c = self.obtener_slot_conclusion()
	    slot_p = self.obtener_slot_literal(i)
	    if slot_c.to_str() == slot_p.to_str():
		return True
	return False
	    
    def obtener_slot_conclusion(self):
	if not self.__regla.get_conclusion():
	    return self.__regla.get_conclusion().get_slot()
    
    def obtener_slot_literal(self, i):
	return self.__regla.get_literal(i).get_slot()
    
    def __obtener_bc(self):
	#bc_ = uarchivo_bc.obtener_bc(PATH_BC)
	try:
	    bc_ = pickle.load(open(PATH_BC))
	except:
	    bc_ = None
	self.__bc = bc_ and bc_ or BC()
	return True
    
    def obtener_bc_(self):
	self.__obtener_bc()
	return self.__bc
    
    def insertar_literal(self, no, nombre_f, nombre_s, oprel_, val_):
	if self.__obtener_bc():
	    slot_ = self.__bc.get_slot(nombre_f, nombre_s)
	    if slot_:
		literal = Cuadrupla(no, slot_, oprel_, val_)
		try:
		    self.__regla.insertar_literal(literal)
		except:
		    pass
	    
    def modificar_literal(self, index, no, nombre_f, nombre_s, oprel_, val_):
	if self.__obtener_bc():
	    slot_ = self.__bc.get_slot(nombre_f, nombre_s)
	    if slot_:
		literal = Cuadrupla(no, slot_, oprel_, val_)
		try:
		    self.__regla.modificar_literal(index, literal)
		except:
		    pass
	    
    def eliminar_literal(self, index):
	self.__regla.eliminar_literal(index)
	
    def establecer_conclusion(self, nombre_f, nombre_s, valor):
	if self.__obtener_bc():
	    slot_ = self.__bc.get_slot(nombre_f, nombre_s)
	    if slot_:
		self.__regla.set_conclusion(Hecho(slot_, valor))
	
    def validar_regla(self):
	if self.es_regla_valida():
	    return self.__regla
	return None
        
    def guardar_regla(self):
        if not self.__buscar_regla():
	    self.__bc.get_reglas().append(self.__regla)
	    #uarchivo_bc.guardar_bc(self.__bc, PATH_BC)
	    pickle.dump(self.__bc, open(PATH_BC, 'w'))
	    
    def __buscar_regla(self):
	if self.__obtener_bc():
	    reglas = self.__bc.get_reglas()
	    for regla in reglas:
		if regla.get_nombre() == self.__regla.get_nombre():
		    return True
	return False
    
    def modificar_regla(self, index):
	pass
    
    def borrar_regla(self, index):
	if self.__obtener_bc():
	    try:
		del self.__bc.get_reglas()[index]
		#uarchivo_bc.guardar_bc(self.__bc, PATH_BC)
		pickle.dump(self.__bc, open(PATH_BC, 'w'))
	    except:
		pass
	
    def insertar_valor(self, nombre_f, nombre_s, valor):
	if self.__obtener_bc():
	    slot_ = self.__bc.get_slot(nombre_f, nombre_s)
	    if slot_:
		slot_.set_valor(valor)
		#uarchivo_bc.guardar_bc(self.__bc)
		pickle.dump(self.__bc, open(PATH_BC, 'w'))
    
    def reglas_to_str(self):
	s = ''
	if self.__obtener_bc():
	    reglas = self.__bc.get_reglas()
	    for regla in reglas:
		s = s + '-> %s <-\r\n' % regla.get_nombre()
		s = s + (regla.es_metarregla() and '[Metarregla]\r\n' or ' ')
		s = s + regla.to_str() + '\r\n\r\n'
	return s
	   
    def frames_to_str(self):
	s = ''
	#frames = uarchivo_bc.obtener_frames(PATH_LFRAMES)
	frames = pickle.load(open(PATH_LFRAMES))
	self.__frames = frames and frames or []
	for frame in frames:
	    s = s + frame.to_str() + '\r\n\r\n'
        return s
    
periodos = {1: '07:00 - 07:45', 2: '07:45 - 08:30', 3: '08:30 - 09:15',
	    4: '09:15 - 10:00', 5: '10:00 - 10:45', 6: '10:45 - 11:30',
	    7: '11:30 - 12:15', 8: '12:15 - 13:00', 9: '13:00 - 13:45',
	    10:'14:00 - 14:45', 11:'14:45 - 15:30', 12:'15:30 - 16:15',
	    13:'16:15 - 17:00', 14:'17:00 - 17:45', 15:'17:45 - 18:30',
	    16:'18:30 - 19:15', 17:'19:15 - 20:00', 18:'20:00 - 20:45',
	    19:'20:45 - 21:30', 20:'21:30 - 22:15', 21:'22:15 - 23:00'}

dias = {1: 'Lunes', 2: 'Martes', 3: 'Miercoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sabado', 7: 'Domingo'}

class CPlanifHorario:
    
    __metaclass__ = Singleton
    """
    Materia = {'sigla':'INF428', 'grupo': 'SB',
	       'horario': {1: [3,4], 3: [3,4], 5: [3,4]}, 'turno': 'maniana'}
             
    self.__materias -> [<Materia>, ...] materias seleccionadas para planificar
    self.__carga_horaria -> [<Materia>, ...] carga horaria predefenida
    self.__frame_materias -> Lista de frames instancia del frame "materia_ph"
    """
    def __init__(self):
	self.__frame_materias = []
	self.__materias = []
	self.__materias_temp = [] #Tiene una copia de self.__materias, del cual se extraeran las materias.
	self.__carga_horaria = []
	self.__horario_res = {1: [], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]} #Contendra el horario resultante
	self.__materias_res = [] #Contendra las materias de sigla-grupo que se lograron planificar
	self.__index = -1
	self.__hay_mas_grupo = True
	self.__grupos_marcados = []
	self.__criterio_orden = [] # Contendra solo las siglas de las materias..ordenadas segun un criterio de turno
	
    def set_materias_ch(self, carga_horaria):
	self.__carga_horaria = carga_horaria
    
    def obtener_materias_sel(self):
	return self.__materias
	
    def agregar_materia_sel(self, nombre_materia):
	"""
	sigla: str -> Sigla de la materia
	grupo: str -> Grupo de la materia
	aula: str -> aula donde se pasa
	"""
	#CCargaFrame.cargar_materia_pnombre(nombre_materia)
	pass
    
    def get_materias_sel(self):
	# convertir la lista de self.__frame_materias al formato de self.__materias y retornarlo
	return self.__materias
    
    def get_materias_res(self):
	return self.__materias_res
    
    def agregar_materia_sel2(self, sigla, grupo = None):
	"""
	Agrega una materia directamente a la lista self.__materias
	por medio de sigla y grupo, buscar una materia con la sigla y el grupo dados..
	y si existe lo agrega a la lista self.__materias.
	"""
	materia_s = self.__buscar_materia(sigla, grupo)
	if isinstance(materia_s, dict):
	    self.__materias.append(materia_s)
	    self.__materias_temp.append(materia_s)
	elif isinstance(materia_s, list):
	    self.__materias.extend(materia_s)
	    self.__materias_temp.extend(materia_s)
	
		
    def __buscar_materia(self, sigla, grupo = None):
	"""
	Devuelve una lista con los diccionarios relacionados a materias con sigla o sigla-grupo dados
	"""
	list_materia = []
	for dic in self.__carga_horaria:
	    if grupo:
		if dic['sigla'] == sigla and dic['grupo'] == grupo:
		    return dic
	    else:
		if dic['sigla'] == sigla:
		    list_materia.append(dic)
	return list_materia
		
    
    def agregar_materia_ch(self, sigla, grupo, horario, turno = None):
	if isinstance(horario, dict):
	    dict_materia = {'sigla':sigla, 'grupo':grupo, 'horario': horario, 'turno': turno and turno or self.__obtener_turno(horario)}
	    if dict_materia not in self.__materias:
		self.__carga_horaria.append(dict_materia)
		
    def __obtener_turno(self, horario):
	if isinstance(horario, dict):
	    list_periodos = horario.values()
	    list_per_max = max(list_periodos)
	    list_per_min = min(list_periodos)
	    turno1 = self.__obtener_turno_de_periodos(list_per_max)
	    turno2 = self.__obtener_turno_de_periodos(list_per_min)
	    if turno1 == turno2:
		return turno1
	    else:
		return 'disperso'
		
    def __obtener_turno_de_periodos(self, list_periodos):
	if isinstance(list_periodos, list):
	    periodo_min = min(list_periodos)
	    periodo_max = max(list_periodos)
	    turno_min = self.__obtener_turno_de_periodo(periodo_min)
	    turno_max = self.__obtener_turno_de_periodo(periodo_max)
	    if turno_min == turno_max:
		return turno_min
	    else:
		return 'disperso'
	    
    def __obtener_turno_de_periodo(self, periodo):
	if periodo in range(1, 10):
	    return 'maniana'
	elif periodo in range(10, 16):
	    return 'tarde'
	elif periodo in range(16, 22):
	    return 'noche'
		
    def get_materias_ch(self):
	return self.__carga_horaria
    
    def get_horario_res(self):
	return self.__horario_res
    
    def obtener_siguiente_materia(self):
	try:
	    #return self.__materias_temp.pop()
	    self.__index = self.__index + 1
	    return self.__materias_temp[self.__index]
	except:
	    return []
	
    def establecer_materias(self, list_siglas_mat, turno):
	res = []
	i = 0
	for sigla_mat in list_siglas_mat:
	    cant_grupos = self.__contar_grupos_materia_turno(sigla_mat, turno)
	    res.append((cant_grupos, sigla_mat))
	res.sort()
	res.reverse()
	for t in res:
	    sigla = t[1]
	    self.agregar_materia_sel2(sigla)
	
	    
	
    def obtener_anterior_materia(self):
	try:
	    self.__index = self.__index - 1
	    return self.__materias_temp[self.__index]
	except:
	    return []
    
    def lista_dict_materias_to_str(self, list_dict_materias):
	s = ''
	for materia in list_dict_materias:
	    s = s + 'sigla: %s - grupo: %s - turno : %s\r\n' % (materia['sigla'], materia['grupo'], materia['turno'])
	    horario = materia['horario']
	    for dia in horario.keys():
		s = s + '%s : %s\r\n' % (dias[dia], self.__periodos_to_str(horario[dia]))
	    s = s + '\r\n'
	return s
	
    def materias_asignadas_to_str(self):
	return self.lista_dict_materias_to_str(self.__materias_res)
    
    def ch_materias_to_str(self):
	return self.lista_dict_materias_to_str(self.__carga_horaria)
    
    def __periodos_to_str(self, list_periodos):
	if isinstance(list_periodos, list):
	    s = '\r\n------------\r\n'
	    for periodo in list_periodos:
		s = s + '%s\r\n' % periodos[periodo]
	    s = s + '------------\r\n'
	    return s
	
    def intentar_asignacion(self, sigla, grupo):
	materia = self.__buscar_materia(sigla, grupo) # Retorna la el diccionario 'materia'
	if materia:
	    if not self.__materia_en_result(sigla):
		horario = materia['horario']
		if not self.__hay_choque(horario):
		    self.__asignar(horario)
		    self.__materias_res.append(materia)
		    self.__grupos_marcados = []
		    return True
	self.__grupos_marcados.append(grupo)
	return False
    
    def hay_mas_grupos(self, sigla, turno):
	cgmt = self.__contar_grupos_materia_turno(sigla, turno)
	cgm = len(self.__grupos_marcados) 
	result = (cgm < cgmt)
	if result:
	    self.__grupos_marcados = []
	return result
    
    def __contar_grupos_materia_turno(self, sigla, turno):
	i = 0
	for materia in self.__carga_horaria:
	    sigla_ = materia['sigla']
	    turno_ = materia['turno']
	    if sigla == sigla_ and turno == turno_:
		i = i + 1
	return i
    
    def materia_asignada(self, sigla):
	for materia in self.__materias_res:
	    if materia['sigla'] == sigla:
		return True
	return False
    
    def hay_grupos_materia_en_turno(self, sigla, turno):
	cgmt = self.__contar_grupos_materia_turno(sigla, turno)
	print 'Cantidad de grupos por la materia %s en el turno %s : %s' % (sigla, turno, cgmt)
	result = (cgmt > 0)
	print 'hay_grupos_materia_en_turno : %s\r\n' % result
	return result
    
    def __materia_en_result(self, sigla):
	for dic in self.__materias_res:
	    if dic['sigla'] == sigla:
		return True
	return False
	    
    def __hay_choque(self, horario):
	if isinstance(horario, dict):
	    for dia in horario.keys():
		periodos_dia = horario[dia] #devuelve una lista con los periodos de ese dia
		if self.__esta_en_horario_res(dia, periodos_dia):
		    return True
	return False
    
    def __esta_en_horario_res(self, dia, periodos_):
	"""
	dia: int
	periodos: Lista de int
	"""
	if isinstance(periodos_, list):
	    periodos_dia = self.__horario_res[dia] #retorna la lista de periodos de ese dia
	    for periodo in periodos_:
		if periodo in periodos_dia:
		    return True
	return False
	
    
    def __asignar(self, horario):
	if isinstance(horario, dict):
	    for dia in horario.keys():
		periodos_ = horario[dia] #retorna la lista de periodos de ese dia
		self.__asignar_dia(dia, periodos_)
    
    def __asignar_dia(self, dia, periodos_):
	if isinstance(periodos_, list):
	    self.__horario_res[dia].extend(periodos_)
    
    def obtener_matriz_horario_res(self):
	data = []
	for f in periodos.keys():
	    tupla = self.__obtener_tupla(f)
	    data.append(tupla)
	return data
    
    def __obtener_tupla(self, f):
	list_tupla = [periodos[f]]
	for c in dias.keys():
	    if f in self.__horario_res[c]: #Si el periodo (representado por la fila) esta asignada en el dia 'c' 
		str_info_mat = self.__obtener_info_materia_res(c, f)
		list_tupla.append(str_info_mat)
	    else:
		list_tupla.append('')
	return tuple(list_tupla)
    
    def __obtener_info_materia_res(self, dia, periodo):
	for materia in self.__materias_res:
	    horario = materia['horario']
	    if horario:
		if horario.has_key(dia):
		    if periodo in horario[dia]:
			return '%s - Gr. %s' % (materia['sigla'], materia['grupo'])
	
	    
	    
class CCargaFrame:
    
    def __init__(self):
	pass
    
    def cargar_materia_pnombre(self, nombre_materia):
	"""
	Tiene que cargar una materia de la Base de Datos y ponerlo en un frame
	y guardarlo en un archivo de frames instancia.
	
	CMateria.buscar_materia(nombre_materia)
	"""
	
	pass
    