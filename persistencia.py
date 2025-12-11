import json


class Persistencia:
		# ....
		
    def cargar_datos(self):
        with open(self.archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        # datos: {'titulo': 'Cien Años de Soledad', 'autor': 'Gabriel García Márquez', 'isbn': '9780307474728', 'disponible': True, '_Libro__veces_prestado': 0}

        biblioteca = Biblioteca(datos["nombre"])
        for dato_libro in datos["libros"]:
            libro = LibroFisico.recrear(
                titulo=dato_libro["titulo"],
                autor=dato_libro["autor"],
                isbn=dato_libro["isbn"],
                disponible=dato_libro["disponible"],
                veces_prestado=dato_libro["_Libro__veces_prestado"]
            )
            biblioteca.libros.append(libro)

        # datos: {'Profesor': {'nombre': 'Felipe', 'cedula': '123123123', 'libros_prestados': ['La Metamorfosis'], 'limite_libros': None}}
        # datos: {'Estudiante': {'nombre': 'Ana María López', 'cedula': '1001234567', 'libros_prestados': [], 'carrera': 'Ingeniería de Sistemas', 'limite_libros': 3}}
        for dato_usuario in datos["usuarios"]:
            tipo_usuario, info_usuario = list(dato_usuario.items())[0]
            
            if tipo_usuario == "Estudiante":
                usuario = Estudiante.recrear(
                    nombre=info_usuario["nombre"],
                    cedula=info_usuario["cedula"],
                    carrera=info_usuario["carrera"],
                    libros_prestados=info_usuario["libros_prestados"]
                )
            else:
                usuario = Profesor.recrear(
                    nombre=info_usuario["nombre"], 
                    cedula=info_usuario["cedula"],
                    libros_prestados=info_usuario["libros_prestados"]
                )
            biblioteca.usuarios.append(usuario)
        return biblioteca