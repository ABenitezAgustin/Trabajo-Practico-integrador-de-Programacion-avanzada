class BibliotecaMenu:

    def __init__(self, g_libros, g_usuarios, g_prestamos):

        self.g_libros = g_libros
        self.g_usuarios = g_usuarios
        self.g_prestamos = g_prestamos

    
    # FUNCIÓN AUXILIAR
    
    def pedir_int(self, mensaje):

        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Debe ingresar un número válido.")


    # MENÚ PRINCIPAL
    
    def menu(self):

        while True:

            opcion = self.pedir_int("""
=== SISTEMA BIBLIOTECA DIGITAL ===

(1) Gestionar libros
(2) Gestionar usuarios
(3) Gestionar préstamos
(4) Salir

Digame su opción: """)

            if opcion == 1:
                self.menu_libros()

            elif opcion == 2:
                self.menu_usuarios()

            elif opcion == 3:
                self.menu_prestamos()

            elif opcion == 4:
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")


    # MENÚ LIBROS
    
    def menu_libros(self):

        while True:

            opcion = self.pedir_int("""
--- GESTIÓN DE LIBROS ---

(1) Alta libro
(2) Baja libro
(3) Modificar libro
(4) Listar libros
(5) Volver

Digame su opción: """)

            if opcion == 1:

                titulo = input("Digame el Título: ").strip()
                autor = input("Digame el Autor: ").strip()
                isbn = input("Digame el ISBN: ").strip()

                if not titulo or not autor or not isbn:
                    print("No puede haber campos vacíos.")
                    continue

                paginas = self.pedir_int("Digame la cantidad de páginas: ")
                anio = self.pedir_int("Digame el año de publicación: ")

                if paginas <= 0 or anio <= 0:
                    print("Valores numéricos inválidos.")
                    continue

                self.g_libros.alta(titulo, autor, isbn, paginas, anio)

            elif opcion == 2:

                isbn = input("Digame el ISBN del libro: ").strip()

                if not isbn:
                    print("ISBN vacío.")
                    continue

                self.g_libros.baja(isbn)

            elif opcion == 3:

                isbn = input("Digame el ISBN del libro a modificar: ").strip()

                if not isbn:
                    print("ISBN vacío.")
                    continue

                opcion_campo = self.pedir_int("""
¿Qué campo querés modificar?

(1) Título
(2) Autor
(3) ISBN
(4) Año
(5) Páginas

Digame su opción: """)

                nuevo_valor = input("Digame el nuevo valor: ").strip()

                if not nuevo_valor:
                    print("Valor vacío.")
                    continue

                self.g_libros.modificacion(isbn, opcion_campo, nuevo_valor)

            elif opcion == 4:
                self.g_libros.listar()

            elif opcion == 5:
                break

            else:
                print("Opción inválida.")

    
    # MENÚ USUARIOS
    
    def menu_usuarios(self):

        while True:

            opcion = self.pedir_int("""
--- GESTIÓN DE USUARIOS ---

(1) Alta usuario
(2) Baja usuario
(3) Modificar usuario
(4) Listar usuarios
(5) Volver

Digame su opción: """)

            if opcion == 1:

                nombre = input("Digame el Nombre: ").strip()
                apellido = input("Digame el Apellido: ").strip()
                dni = input("Digame el DNI: ").strip()
                correo = input("Digame el Correo: ").strip()

                if not nombre or not apellido or not dni or not correo:
                    print("No puede haber campos vacíos.")
                    continue

                if not dni.isdigit():
                    print("DNI inválido.")
                    continue

                self.g_usuarios.alta(nombre, apellido, dni, correo)

            elif opcion == 2:

                dni = input("Digame el DNI del usuario: ").strip()

                if not dni.isdigit():
                    print("DNI inválido.")
                    continue

                self.g_usuarios.baja(dni)

            elif opcion == 3:

                dni = input("Digame el DNI del usuario a modificar: ").strip()

                if not dni.isdigit():
                    print("DNI inválido.")
                    continue

                opcion_campo = self.pedir_int("""
¿Qué campo querés modificar?

(1) Nombre
(2) Apellido
(3) DNI
(4) Correo

Digame su opción: """)

                nuevo_valor = input("Digame el nuevo valor: ").strip()

                if not nuevo_valor:
                    print("Valor vacío.")
                    continue

                self.g_usuarios.modificacion(dni, opcion_campo, nuevo_valor)

            elif opcion == 4:
                self.g_usuarios.listar()

            elif opcion == 5:
                break

            else:
                print("Opción inválida.")

    
    # MENÚ PRÉSTAMOS

    def menu_prestamos(self):

        while True:

            opcion = self.pedir_int("""
--- GESTIÓN DE PRÉSTAMOS ---

(1) Prestar libro
(2) Devolver libro
(3) Listar préstamos
(4) Volver

Digame su opción: """)

            if opcion == 1:

                isbn = input("Digame el ISBN del libro: ").strip()
                dni = input("Digame el DNI del usuario: ").strip()

                if not isbn or not dni:
                    print("Campos vacíos.")
                    continue

                if not dni.isdigit():
                    print("DNI inválido.")
                    continue

                self.g_prestamos.alta(isbn, dni)

            elif opcion == 2:

                isbn = input("Digame el ISBN del libro: ").strip()

                if not isbn:
                    print("ISBN vacío.")
                    continue

                self.g_prestamos.baja(isbn)

            elif opcion == 3:
                self.g_prestamos.listar()

            elif opcion == 4:
                break

            else:
                print("Opción inválida.")