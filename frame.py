class Frame:
    """
    Estructura: Frame(nombre, [Slot(nombre, [Facet(nombre, []), ..., Facet(nombre, [])]), ..., Slot(nombre, [Facet(nombre, []), ..., Facet(nombre, [])])])
    __nombre : Cadena
    __slots : Lista de <Slot>
    """
    def __init__(self, nombre = '', slots_ = None):
        self.__nombre = nombre
        self.__slots = ((slots_ == None) and [[]] or [slots_])[0]
        self.__set_myname_slots()
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_slots(self, slots):
        self.__set_myname_slots()
        self.__slots = slots
        
    def agregar_slot(self, slot):
        """Agrega un objeto tipo 'Slot' al frame"""
        if isinstance(slot, Slot):
            slot.set_nombre_frame(self.__nombre)
            self.__slots.append(slot)
        
    def get_nombre(self):
        return self.__nombre
    
    def get_slots(self):
        return self.__slots
    
    def get_slot(self, nombre_slot):
        """Retorna el 'Slot' con nombre 'nombre_slot'"""
        for slot in self.__slots:
            if nombre_slot == slot.nombre:
                return slot
            
    def get_valor_facet(self, nombre_slot, nombre_facet):
        slot_ = self.get_slot(nombre_slot)
        if slot_ is not None:
            facet_ = slot_.get_facet(nombre_facet)
            if facet_ is not None:
                return facet_.valores
        return None
    
    def get_valor(self, nombre_slot):
        slot_ = self.get_slot(nombre_slot)
        if slot_ is not None:
            facet_ = slot_.get_facet('valor')
            if facet_ is not None:
                return facet_.valores[0] # Obtiene el primer valor de la lista del Facet "valor"
        return None
        
    def existe_slot(self, nombre_slot):
        return self.get_slot(nombre_slot) is not None
    
    def __set_myname_slots(self):
        for slot in self.__slots:
            slot.set_nombre_frame(self.__nombre)
        
    def to_str(self):
        s = self.nombre + ' : \r\n'
        for slot in self.slots:
            s = s + slot.to_str() + '\r\n'
        return s
    
    nombre = property(get_nombre, set_nombre)
    slots = property(get_slots, set_slots)

"""
T: Texto
N: Numerico
L: Lista
B: Booleano
F: Fecha
H: Hora
"""
(T, N, L, B ,F, H, D) = range(7)

"""Tipo de metodo asociado a un slot"""
(WHEN_CHANGED, WHEN_NEEDED) = range(7,9)

class Slot:
    """
    Estructura Generica: Slot(nombre, [Facet(nombre, []), ..., Facet(nombre, [])])
    Estructura especifica: Slot(nombre, [Facet('rango', []), Facet('valores', []), Facet('default', []))
    __nombre_frame : str, Solo para saber a que frame pertenece este Slot
    __nombre : str
    __tipo : int
    __metodo: int
    __facets : Lista de <Facet>
    """
    def __init__(self, nombre_, tipo_, metodo_ = None, facets_ = None):
        if isinstance(nombre_, str):
            self.__nombre_frame = ''
            self.__nombre = nombre_
            self.__tipo = tipo_
            self.__metodo = metodo_
            self.__facets = ((facets_ == None) and [[]] or [facets_])[0]
        
    def set_nombre_frame(self, nom_frame):
        if isinstance(nom_frame, str):
            self.__nombre_frame = nom_frame
        
    def set_nombre(self, nombre_):
        if isinstance(nombre_, str):
            self.__nombre = nombre_
        
    def get_nombre_frame(self):
        return self.__nombre_frame
            
    def get_nombre(self):
        return self.__nombre
    
    def set_tipo(self, tipo_):
        if tipo_ in range(7):
            self.__tipo = tipo_
            
    def get_tipo(self):
        return self.__tipo
    
    def set_metodo(self, metod):
        if metod is None or metod in range(7,9):
            self.__metodo = metod
            
    def get_metodo(self):
        return self.__metodo
    
    def set_facets(self, facets):
        self.__facets = facets
            
    def get_facets(self):
        return self.__facets
    
    def get_facet(self, nombre_facet):
        for facet in self.__facets:
            if facet.nombre == nombre_facet:
                return facet
        return None
    
    def agregar_facet(self, facet):
        if isinstance(facet, Facet):
            self.__facets.append(facet)
                
    def set_facet(self, facet):
        if isinstance(facet, Facet):
            fac = self.buscar_facet(facet.nombre)
            if fac is None:
                self.agregar_facet(facet)
            else:
                fac = facet.valores
                
    
    def buscar_facet(self, nombre_fac):
        if isinstance(nombre_fac, str):
            for fac in self.facets:
                if fac.nombre == nombre_fac:
                    return fac
        return None
    
            
    #Getters y Setters de Facets especificas para este proyecto: Inicio
    def set_rango(self, rango_):
        """
        Procedimiento que establece el rango de valores al facet 'rango' de este slot
        param rango: Lista que contiene el rango de valores que puede tomar este slot
        """
        if isinstance(rango_, list):
            self.set_facet(Facet('rango', rango_))
            
    def set_valor(self, valor):
        """
        Procedimiento que establece el valor o valores al facet 'valor' de este slot
        param valor: Si es una lista lo asigna a la propiedad 'valores' del facet 'valor' de este slot,
        caso contrario se lo introduce como un item a la propiedad 'valores' del facet 'valor' de este slot
        (Esta operacion es validad por el constructor del Facet).
        """
        self.set_facet(Facet('valor', valor))
        
    def set_default(self, valor_def):
        """
        Procedimiento similar a set_valor, con la particularidad que este establece un valor por defecto
        al facet 'default' de este slot.
        """
        self.set_facet(Facet('default', valor_def))
        
    def get_rango(self):
        """
        Devuelve una lista con los valores validos que pueden tomar los facets 'valor' y 'default' de este slot.
        """
        return self.get_facet('rango').valores
    
    def get_valor(self):
        """
        Devuelve el valor del facet 'valor' de este slot
        """
        return self.get_facet('valor').valores
    
    def get_default(self):
        """
        Devuelve el valor del facet 'default' de este slot
        """
        return self.get_facet('default').valores
    
    #Facets especificas para este proyecto: Fin
    
    def to_str(self):
        s = ''
        for facet in self.facets:
            s = s + facet.to_str() + '\r\n'
        return '%s : %s' % (self.nombre, s)
    
    nombre_frame = property(get_nombre_frame, set_nombre_frame)
    nombre = property(get_nombre, set_nombre)
    tipo = property(get_tipo, set_tipo)
    metodo = property(get_metodo, set_metodo)
    facets = property(get_facets, set_facets)
        
class Facet:
    """
    Estructura: Facet(nombre, [])
    __nombre : Cadena
    __valores : Lista de 'Object'
    """
    def __init__(self, nombre = '', valores = None):
        if isinstance(nombre, str):
            self.__nombre = nombre
            self.__valores = valores
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_valores(self, valores):
        self.__valores = valores
        
    def set_valor(self, valor):
        if isinstance(valor, list):
            self.__valores = valores
        else:
            self.agregar_valor(valor)
        
    def get_valores(self):
        return self.__valores
        
    def agregar_valor(self, valor):
        self.__valores.append(valor)
        
    def get_valor(self, i):
        return self.__valores[i]
    
    def to_str(self):
        return 'F[%s : %s]' % (self.nombre, self.valores)
    
    nombre = property(get_nombre, set_nombre)
    valores = property(get_valores, set_valores)
    
    