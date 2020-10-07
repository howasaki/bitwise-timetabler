import bc
import bh
from bc import BC
from bc import Regla
from bc import Cuadrupla
from bh import BH
#from bh import Objeto
from bh import Hecho
from frame import *
import umetodos

class CMotorInferencia:
    def __init__(self, _bc, _bh = BH()):
        self.set_bc(_bc)
        self.set_bh(_bh)
        self.__slot_marcados = []
        self.__reglas_marcadas = []
        
    def set_bc(self, _bc):
        if isinstance(_bc, BC): self.__bc = _bc
        
    def set_bh(self, _bh):
        if isinstance(_bh, BH): self.__bh = _bh
        
    def get_bh(self):
        return self.__bh
        
    def fwc_meta(self, nombre_meta):
        """ Forward Chaining - Encadenamiento hacia adelante. Forzado a encontrar una meta 
        Retorna El valor si unifica la meta, caso contrario None """
        meta = self.__bc.get_objeto(nombre_meta)
        if meta is not None:
            self.desmarcar_reglas()
            l = self.__bh.longitud()
            while l in range(self.__bh.longitud()) and self.hay_regla_no_marcada() and not self.meta_en_bh(meta):
                while i in range(len(self.__bc.reglas)) and not self.meta_en_bh(meta):
                    regla = self.__bc.reglas[i]
                    conclusion = self.dispara_conclusion(regla)
                    if not self.regla_marcada(regla) and conclusion is not None:
                        self.__bh.agregar(conclusion)
                        self.marcar(regla)
                l = self.__bh.longitud()
            return self.meta_en_bh(meta) and meta.get_nombre() or None
        return None
    
    def fwc(self):
        """ Forward Chaining - Encadenamiento hacia adelante.
        Retorna una lista de valores unificados """
        conclusiones = []
        self.desmarcar_reglas()
        l = self.__bh.longitud()
        i = 0
        horario_alcanzado = False
        #while i in range(l) and self.hay_regla_no_marcada():
        while not horario_alcanzado:
            for regla in self.__bc.reglas:
                if not self.regla_marcada(regla) and self.dispara_conclusion(regla):
                    conclusion = regla.get_conclusion()
                    #print "Regla %s -> Conclusion = %s" % (regla.get_nombre(), conclusion.to_str())
                    slot_ = conclusion.get_slot()
                    if slot_:
                        if slot_.get_metodo() == WHEN_CHANGED:
                            umetodos.regla = regla
                            str_llamada = '%s_%s_when_changed(regla, "%s")' % (slot_.get_nombre_frame(), slot_.get_nombre(), conclusion.get_valor())
                            #print 'ejecutando la funcion umetodos.%s' % str_llamada
                            if not umetodos.ejecutar(str_llamada):
                                horario_alcanzado = True
                                #print 'HORARIO ALCANZADO IGUAL A TRUE, JEJE YO ME LARGOOOOOOOOOOOOO'
                                return True
                    if regla.es_metarregla():
                        self.__bh.reemplazar_hecho(conclusion)
                    else:
                        self.__bh.agregar(conclusion)
                    conclusiones.append(conclusion)
                    #self.marcar(regla)
                    i = 0
            #print 'BASE DE HEEECHOSSSS %s' % self.get_bh().to_str()
            l = self.__bh.longitud()
            i = i + 1
        return conclusiones
                         
    def desmarcar_reglas(self):
        self.__reglas_marcadas = []
    
    def hay_regla_no_marcada(self):
        return not (len(self.__reglas_marcadas) == len(self.__bc.reglas))
    
    def meta_en_bh(self, meta):
        pass
    
    def regla_marcada(self, regla):
        for reg in self.__reglas_marcadas:
            if reg.get_nombre() == regla.get_nombre():
                return True
        return False
    
    def dispara_conclusion(self, regla):
        for cuadrupla in regla.get_premisa():
            hecho = self.__bh.get_hecho(cuadrupla.slot)
            if hecho is None or not self.eval_satisfactoria(cuadrupla, hecho):
                return False
        return True
    
    def marcar(self, regla):
        if isinstance(regla, Regla):
            self.__reglas_marcadas.append(regla)
    
    def eval_satisfactoria(self, cuadrupla, hecho):
        b = False
        oprel = cuadrupla.get_oprel()
        valc = cuadrupla.get_valor()
        valh = hecho.get_valor()
        tipo = cuadrupla.slot.tipo
        if tipo == N:
            if oprel == bc.IGUAL:
                b = (valh == valc)
            if oprel == bc.DIS:
                b = (valh != valc)
            elif oprel == bc.MAI:
                b = (valh >= valc)
            elif oprel == bc.MAY:
                b = (valh > valc)
            elif oprel == bc.MEI:
                b = (valh <= valc)
            elif oprel == bc.MEN:
                b = (valh < valc)
        elif tipo == T:
            if oprel == bc.IGUAL:
                b = (valh == valc)
            if oprel == bc.DIS:
                b = (valh != valc)
        res = b and not cuadrupla.get_no()
        return res
    
    def agregar_hecho(self, hecho_):
        if not self.__buscar_hecho(hecho_):
            self.__bh.agregar(hecho_)
            
    def agregar_hecho2(self, nombre_f, nombre_s, valor):
        slot_ = self.__bc.get_slot(nombre_f, nombre_s)
        if slot_:
            self.agregar_hecho(Hecho(slot_, valor))
    
    def __buscar_hecho(self, hecho_):
        if isinstance(hecho_, Hecho):
            hecho_e = self.__bh.buscar_slot(hecho_.get_slot())
            return hecho_e
                