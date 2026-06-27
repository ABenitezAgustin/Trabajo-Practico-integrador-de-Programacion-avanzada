class Libro():
    def __init__(self,titulo,autor,isbn,cantdepaginas,aniopubli):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.cantdepaginas = cantdepaginas
        self.aniopubli = aniopubli
        estado = True
        
    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}"    
    
        
        