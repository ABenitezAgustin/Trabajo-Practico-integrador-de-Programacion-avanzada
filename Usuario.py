class Usuario():
    def __init__(self,nombre,apellido,dni,correo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo
    
    def __str__(self):
        return f"Usuario: {self.nombre}, {self.apellido}"