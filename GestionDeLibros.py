from interfaz import GestorBase
from Libro import Libro

class GestorLibros(GestorBase):
    def __init__(self):
        self.libros = []
    
    def alta(self, titulo, autor, isbn, cantdepaginas, aniopubli):

      for l in self.libros:
          if l.isbn == isbn:
              print("Ya existe un libro con ese ISBN.")
              return

      nuevo_libro = Libro(titulo, autor, isbn, cantdepaginas, aniopubli)
      self.libros.append(nuevo_libro)
    
    
    def baja(self, identificador): 
        for libro in self.libros:
            if libro.isbn == identificador:
                self.libros.remove(libro)
                print("Se ha borrado con exito")
                return
            print("No se encontró el libro.")

    def modificacion (self, isbn, campo, nuevo_valor):
        for libro in self.libros:
            if libro.isbn() == isbn:
                if campo == 1:
                    libro.titulo = nuevo_valor
                elif campo == 2:
                    libro.autor = nuevo_valor
                elif campo == 4:
                    libro.aniopubli = nuevo_valor
                elif campo == 5:
                    libro.cantpaginas = nuevo_valor
                elif campo == 3:
                    libro.isbn = nuevo_valor    
                return
        print(f"No se encontro el libro: {isbn}")
    
    def listar(self):
        print("lista de Libros")
        for libro in self.libros:
            print(libro)
    
