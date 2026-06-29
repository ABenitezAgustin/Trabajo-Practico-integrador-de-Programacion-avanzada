from abc import ABC, abstractmethod

class GestorBase(ABC):
    @abstractmethod
    def alta(self, *args):
        pass 
    
    @abstractmethod
    def baja(self, identificador):
        pass
    
    @abstractmethod
    def modificacion(self, *args):
        pass
    
    @abstractmethod
    def listar(self):
        pass
        
        