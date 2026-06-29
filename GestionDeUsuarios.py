from interfaz import GestorBase
from Usuario import Usuario
class GestorDeUsuario(GestorBase):
    def __init__(self):
        self.usuarios = []
    
    def alta(self,nombre,apellido,dni,correo):
        usuario = Usuario(nombre,apellido,dni,correo)
        for u in self.usuarios:
            if u.dni == dni:
                print("Ya existe un usuario con ese DNI.")
                return
    
        self.usuarios.append(usuario)
    
    def baja(self, identificador): 
        for usuario in self.usuarios:
            if int(usuario.dni) == int(identificador):
                self.usuarios.remove(usuario)
                return
                

    def modificacion (self, dni, campo, nuevo_valor):
        for u in self.usuarios:
            if int(u.dni) == int(dni):
                if campo == 1:
                    u.nombre = nuevo_valor
                elif campo == 2:
                    u.apellido = nuevo_valor
                elif campo == 3:
                    u.dni = nuevo_valor
                elif campo == 4:
                    u.correo = nuevo_valor    
                return
        print(f"No se ha encontrado el usuario: {dni}")
    
    def listar(self):
        print("lista de usuarios")
        for usuario in self.usuarios:
            print(usuario)



