from interfaz import GestorBase
from Libro import Libro

class GestorLibros(GestorBase):
    def __init__(self):
        self.libros = []
    
    def alta(self,titulo,autor,isbn,cantdepaginas,aniopubli):
        libro = Libro(titulo,autor,isbn,cantdepaginas,aniopubli)
        self.libros.append(libro)
    
    
    def baja(self, identificador): 
        for libro in self.libros:
            if libro.isbn == identificador:
                self.libros.remove(libro)
                

    def modificacion (self, libro, campo, nuevo_valor):
        if campo == "titulo":
            libro.titulo = nuevo_valor
        elif campo == "autor":
            libro.autor = nuevo_valor
        elif campo == "anio":
            libro.anio = nuevo_valor
        elif campo == "paginas":
            libro.paginas = nuevo_valor
    
    def listar(self):
        print("lista de Libros")
        for libro in self.libros:
            print(libro)
    
Libreria=GestorLibros()
Libreria.alta("Pepe","José",11,900,1990)
Libreria.alta("Principe de P","JP",8,150,1990)
Libreria.alta("Lolo","Herrera",15,1200,1690)
Libreria.listar()
Libreria.baja(11)
print("----------------------------------------------------------------------")
Libreria.modificacion()
Libreria.listar()