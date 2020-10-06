from bh import Hecho
from frame import *

(IGUAL, DIS, MAY, MEN, MAI, MEI) = range(6)

class Cuadrupla:
    """
    __no : bool
    __slot : <Slot>
    __oprel : (IGUAL, DIS, MAY, MEN, MAI, MEI)
    __val : 'Object'
    """
    def __init__(self, no_, slot_, oprel_, val):
        self.__no = no_
        self.__slot = slot_
        self.__oprel = oprel_
        self.__valor = val
        
    def set_no(self, no_):
        if isinstance(no_, bool):
            self.__no = no_
                
    def set_slot(self, slot_):
        if isinstance(slot_, Slot):
            self.__slot = slot_
            
    def set_oprel(self, oprel_):
        if isinstance(oprel_, int) and oprel_ in range(6):
            self.__oprel = oprel_
        
    def set_valor(self, val):
        if val is not None:
            self.__valor = val
        
    def get_no(self):
        return self.__no
    
    def get_slot(self):
        return self.__slot
    
    def get_oprel(self):
        return self.__oprel
    
    def get_valor(self):
        return self.__valor

    @property
    def nombre_frame(self):
        return self.__slot.get_nombre_frame()
    
    @property
    def nombre_slot(self):
        return self.__slot.get_nombre()
    
    def oprel_to_str(self):
        if self.__oprel == IGUAL:
            return '=='
        elif self.__oprel == DIS:
            return '<>'
        elif self.__oprel == MAY:
            return '>'
        elif self.__oprel == MEN:
            return '<'
        elif self.__oprel == MAI:
            return '>='
        elif self.__oprel == MEI:
            return '<='
    
    def to_str(self):
        return '%s %s.%s %s %s' % (self.__no and 'NOT' or '', self.__slot.nombre_frame, self.__slot.get_nombre(), self.oprel_to_str(), self.__valor)
    
    no = property(get_no, set_no)
    slot = property(get_slot, set_slot)
    oprel = property(get_oprel, set_oprel)
    valor = property(get_valor, set_valor)

class Regla:
    """
    __nombre : str
    __premisa : Lista de objetos tipo <Cuadrupla>
    __conclusion : <Hecho>
    __metarregla: Boolean (True si es metarregla, False si es simplemente una regla)
    """
    def __init__(self, es_metarregla = False):
        self.__nombre = ''
        self.__premisa = []
        self.__conclusion = None
        self.__metarregla = es_metarregla
        
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        
    def set_premisa(self, premisa):
        if isinstance(premisa, list):
            self.__premisa = premisa
        
    def set_conclusion(self, conclusion):
        if isinstance(conclusion, Hecho):
            self.__conclusion = conclusion
            
    def get_nombre(self):
        return self.__nombre
    
    def get_premisa(self):
        return self.__premisa

    def get_conclusion(self):
        return self.__conclusion

    def get_literal(self, index):
        return self.__premisa[index]
    
    def es_metarregla(self):
        return self.__metarregla
    
    def set_metarregla(self, es_mr):
        self.__metarregla = es_mr

    def insertar_literal(self, cuadrupla):
        if isinstance(cuadrupla, Cuadrupla):
            if (not self.__metarregla) and self.en_conclusion(cuadrupla.slot):
                raise Exception('Hay contradiccion')
            self.__premisa.append(cuadrupla)
            
    def modificar_literal(self, i, cuadrupla):
        if isinstance(cuadrupla, Cuadrupla):
            if (not self.__metarregla) and self.en_conclusion(cuadrupla.slot):
                raise Exception('Hay contradiccion')
            self.__premisa[i] = cuadrupla
            
    def eliminar_literal(self, index):
        if index in range(len(self.__premisa)):
            self.__premisa.remove(index)
            
    def hay_slot(self, slot_):
        return en_conclusion(slot_) or en_premisa(slot_)
    
    def hay_valor(self, val):
        if val == self.__conclusion.valor: return True
        for cuadrupla in self.__premisa:
            if cuadrupla.valor == val: return True            
        return False
    
    def en_conclusion(self, slot_):
        if isinstance(slot_, Slot):
            if self.__conclusion:
                return self.__slot_iguales(self.__conclusion.get_slot(), slot_)
        return False
    
    def en_premisa(self, slot_):
        for cuadrupla in self.__premisa:
            if self.__slot_iguales(cuadrupla.slot, slot_): return True
        return False
    
    def __slot_iguales(self, slot1, slot2):
        if slot1.nombre_frame == slot2.nombre_frame:
                if slot1.nombre == slot2.nombre:
                    return True
        return False
    
    @property
    def cant_literales(self):
        return len(self.__premisa)
    
    def to_str(self):
        return 'IF %s \r\n  THEN %s' % (' AND'.join(['%s' % (cuadr.to_str()) for cuadr in self.__premisa]), (self.__conclusion and self.__conclusion.to_str() or '=' ))
    
    #def premisa_to_str(self):
        
    
    nombre = property(get_nombre, set_nombre)
    premisa = property(get_premisa, set_premisa)
    conclusion = property(get_conclusion, set_conclusion)
    
class BC:
    """
    __slots : Lista de objetos tipo <Slot>
    __reglas : Lista de objetos tipo <Regla>
    """
    def __init__(self):
        self.__slots = []
        self.__reglas = []
        
    def get_objeto(self, nombre):
        for objeto in self.__objetos:
            if objeto.get_nombre() == nombre:
                return objeto
        return None
    
    def get_slot(self, nombre_frame, nombre_slot):
        for slot_ in self.__slots:
            if slot_.get_nombre_frame() == nombre_frame and slot_.get_nombre() == nombre_slot:
                return slot_
        return None
    
    def get_slots(self):
        return self.__slots
    
    def get_reglas(self):
        return self.__reglas
    
    def set_slots(self, slots_):
        if isinstance(slots_, list):
            self.__slots = slots_
        
    def set_reglas(self, reglas):
        if isinstance(reglas, list):
            self.__reglas = reglas
    
    def get_regla(self, index):
        try:
            return self.__reglas[index]
        except:
            return None
            
    slots = property(get_slots, set_slots)
    reglas = property(get_reglas, set_reglas)