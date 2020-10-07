import types
import pickle
from frame import *
from bc import *

PATH_LFRAMES = 'archivos/frames.t'

class Singleton(type):
 
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)
 
    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args,**kw)
        return cls.__instance

    
class UADMDB:
    
    __metaclass__ = Singleton
    
    def __init__(self):
        pass
    
    def obtener(self, path_file):
        #try:
            return pickle.load(open(path_file))
        #except:
        #    print 'No se pudo cargar el archivo %s' % path_file
        #   return None
    
    def guardar(self, obj, path_file):
        pickle.dump(obj, open(path_file, 'w'))   
        

admdb = UADMDB()
    
class UArchivoBC:
    
    __metaclass__ = Singleton
    
    def __init__(self):
        pass
    
    def guardar_frames(self, list_frames, path_frame):
        admdb.guardar(list_frames, path_frame)
    
    def obtener_frames(self, path_frames):
        return admdb.obtener(path_frames)
    
    def guardar_bc(self, bc, path_bc):
        if isinstance(bc, BC):
            admdb.guardar(bc, path_bc)
            
    def obtener_bc(self, path_bc):
        return admdb.obtener(path_bc)

