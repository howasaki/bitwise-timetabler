from frame import *

(NUMERICO, ESCALAR) = range(2)
# NOTA : La clase Objeto esta en desuso
"""
class Objeto:
    def __init__(self, nombre, tipo, valores = None):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__valores = ((valores == None) and [[]] or [[valores]])[0]
	
    def set_nombre(self, nombre):
	self.__nombre = nombre
	
    def set_tipo(self, tipo):
	self.__tipo = tipo
	
    def set_valores(self, vals):
	self.__valores = vals
	
    def get_nombre(self):
	return self.__nombre
    
    def get_tipo(self):
	return self.__tipo
    
    def get_valores(self):
	return self.__valores
    	
    def ins_valor(self, valor):
	if (self.__tipo == ESCALAR and valor not in self.__valores):
	    self.__valores.append(valor)
	    
    def modif_valor(self, valAnt, valNuevo):
	if(self.__tipo == ESCALAR):
	    if(valAnt in self.__valores):
		self.__valores[self.__valores.index(valAnt)] = valNuevo
	    
    def elim_valor(self, valor):
	if(self.__tipo == ESCALAR):
	    self.__valores.remove(valor)
	    
    def set_rango(self, min, max):
	if(self.__tipo == NUMERICO):
	    self.__valores = [min, max]
	    
    def es_valido(self, valor):
	if(self.__tipo == NUMERICO):
	    if(self.__valores.count == 2):
		return self.__valores[0] <= valor and valor <= self.__valores[1]
	else:
	    return valor in self.__valores
"""	    
	    
class Hecho:
    """
    __slot : <Slot>
    __valor : 'Object'
    """
    def __init__(self, slot_, valor_):
	self.__slot = slot_
	self.__valor = valor_
	
    def get_slot(self): return self.__slot
    
    def get_valor(self): return self.__valor
    
    def set_slot(self, slot_):
	if isinstance(slot_, Slot):
	    self.__slot = slot_
	
    def set_valor(self, val):
	if val is not None:
	    self.__valor = val
	
    def to_str(self):
	return "%s.%s = %s" % (self.__slot.nombre_frame, self.__slot.nombre, self.__valor)
    
    slot = property(get_slot, set_slot)
    valor = property(get_valor, set_valor)
	
class BH:
    """
    __hechos : Lista de tipo <Hecho>
    """
    def __init__(self):
	self.__hechos = []
    
    def set_hechos(self, hechos):
	if isinstance(hechos, list):
	    self.__hechos = hechos
	
    def agregar(self, hecho):
	if isinstance(hecho, Hecho):
	    self.__hechos.append(hecho)
	    
    def obtener(self, index):
	self.__hechos[index]
	
    def vaciar(self):
	self.__hechos = []
	
    def longitud(self):
	return len(self.__hechos)
      
    def get_hecho(self, slot_):
	if isinstance(slot_, Slot):
	    hecho = self.buscar_slot(slot_)
	    return hecho
	return None
    
    def buscar_slot(self, slot_):
	"""
	Busca el Hecho que tenga al slot 'slot_'
	"""
	for hecho in self.__hechos:
	    if hecho.slot.nombre_frame == slot_.nombre_frame and hecho.slot.nombre == slot_.nombre:
		return hecho
	return None
    
    def indice_de_nombre_hecho(self, hecho_):
	"""
	Retona el indice del hecho, en la BH, que tenga el nombre de 'hecho_'
	"""
	for index in range(len(self.__hechos)):
	    hecho = self.__hechos[index]
	    if hecho.slot.nombre_frame == hecho_.slot.nombre_frame and hecho.slot.nombre == hecho_.slot.nombre:
		return index
	return None
    
    def reemplazar_hecho(self, hecho):
	if isinstance(hecho, Hecho):
	    index = self.indice_de_nombre_hecho(hecho)
	    if index is not None:
		self.__hechos[index] = hecho
    
    def to_str(self):
	return "BH : \r\n" + ";\r\n".join(["%s" % (hecho.to_str()) for hecho in self.__hechos])