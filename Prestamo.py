from datetime import datetime

class Prestamo:

    def __init__(self, libro, usuario):

        self.libro = libro
        self.usuario = usuario

        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None

        self.activo = True

    def devolver(self):

        self.fecha_devolucion = datetime.now()
        self.activo = False

    def __str__(self):

        estado = "Activo" if self.activo else "Devuelto"

        return (
            f"Libro: {self.libro.titulo} | "
            f"Usuario: {self.usuario.nombre} {self.usuario.apellido} | "
            f"Fecha préstamo: {self.fecha_prestamo} | "
            f"Estado: {estado}"
        )