from abc import ABC, abstractmethod

class GestorBase:
    @abstractmethod
    def alta(self):
        pass 
    
    @abstractmethod
    def baja(self, identificador):
        pass
    
    @abstractmethod
    def modificacion(self,identificador, campo, nuevo_valor):
        pass
    
    @abstractmethod
    def listar(self):
        pass
        