from interfaz import GestorBase
from Prestamo import Prestamo


class GestorPrestamos(GestorBase):

    def __init__(self, g_libros, g_usuarios):

        self.g_libros = g_libros
        self.g_usuarios = g_usuarios

        self.prestamos = [] 

   
    def alta(self, isbn, dni): #Prestamo del libro

        libro = None
        usuario = None

        
        for l in self.g_libros.libros:
            if l.isbn.lower() == isbn.lower():
                libro = l
                break

        
        for u in self.g_usuarios.usuarios:
            if int(u.dni) == int(dni):
                usuario = u
                break

        
        if not libro:
            print(f"No se encontró el isbn '{isbn}'")
            return

        if not usuario:
            print(f"No se encontró el usuario con DNI {dni}")
            return

        if not libro.estado:
            print(f"El libro '{libro.titulo}' ya está prestado")
            return

        
        prestamo = Prestamo(libro, usuario)
        self.prestamos.append(prestamo)

        libro.estado = False

        print(f"Préstamo exitoso: {usuario.nombre} {usuario.apellido} -> '{libro.titulo}'")

    
    def baja(self, isbn): #devoluciondellibro

        for p in self.prestamos:

            if p.libro.isbn == isbn and p.activo:

                p.devolver()
                p.libro.estado = True

                print(f"Devolución exitosa: '{p.libro.titulo}'")

                return

        print(f"No se encontró préstamo activo del libro '{isbn}'")

   
    def modificacion(self, *args):

        print("Los préstamos no se pueden modificar.")

  
    def listar(self):

        print("\n--- PRÉSTAMOS ACTIVOS ---")

        hay = False

        for p in self.prestamos:

            if p.activo:

                print(p)  # usa __str__ de Prestamo
                hay = True

        if not hay:
            print("No hay préstamos activos.")