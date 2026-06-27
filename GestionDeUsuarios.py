from interfaz import GestorBase
from Usuario import Usuario
class GestorDeUsuario(GestorBase):
    def __init__(self):
        self.usuarios = []
    
    def alta(self,nombre,apellido,dni):
        usuario = Usuario(nombre,apellido,dni)
        self.usuarios.append(usuario)
    
    def baja(self, identificador): 
        for usuario in self.usuarios:
            if usuario.dni == identificador:
                self.usuarios.remove(usuario)
                

    def modificacion (self, libro, campo, nuevo_valor):
        if campo == "nombre":
            libro.nombre = nuevo_valor
        elif campo == "apellido":
            libro.apellido = nuevo_valor
    
    
    def listar(self):
        print("lista de usuarios")
        for usuario in self.usuarios:
            print(usuario)
    
gestor  = GestorDeUsuario()
gestor.alta("tito", "pepe", 44)
gestor.alta("jose", "perez",1800)
gestor.listar()
gestor.baja(44)
gestor.listar()




