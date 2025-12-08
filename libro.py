from typing import Protocol

class LibroProtocol(Protocol):
  def prestar_libro(self) -> str:
    """
    Método que debe implementar cualquier clase que quiera prestar un libro
    Returns:
        str: Un mensaje indicando que el libro ha sido prestado
    """

  def duracion_prestamo(self) -> int:
    """
    Método que debe implementar cualquier clase que quiera calcular la duración de un préstamo de un libro
    Returns:
        int: La duración del préstamo en días
    """


# Clase Libro
class Libro:

  # Método constructor
  def __init__(self, titulo, autor, isbn, disponible = True):
    self.titulo = titulo
    self.autor = autor
    self.isbn = isbn
    self.disponible = disponible
    #Atributo privado
    self.__prestamos = 0  # Lista para guardar los préstamos del libro

  # Método para imprimir la representación escrita del libro
  def __str__(self):
    return f"Titulo: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Disponible: {self.disponible}"

  # Método para cambiar la disponibilidad del libro
  def prestar_libro(self):
    if self.disponible:
      self.disponible = False
      self.__prestamos += 1  # Registrar el préstamo en la lista
      return f"El libro *{self.titulo} ha sido prestado"
    return f"El libro *{self.titulo} no está disponible"

  def devolver_libro(self):
    if not self.disponible:
      self.disponible = True
      return f"El libro *{self.titulo} ha sido devuelto"

  def es_popular(self):
    # Retorna True si el libro ha sido prestado más de 5 veces
    if self.__prestamos > 5:
      return f"El libro *{self.titulo} es popular, ha sido prestado {self.__prestamos} veces"
    return f"El libro *{self.titulo} no es popular, ha sido prestado {self.__prestamos} veces"

  #Método para acceder al atributo privado
  def get_prestamos(self):
    return self.__prestamos

  #Método para cambiar el atributo privado
  def set_prestamos(self, prestamos):
    self.__prestamos = prestamos

class LibroFisico(Libro):
  def __init__(self, titulo, autor, isbn, disponible = True, dias_en_prestamo: int = 0):
    super().__init__(titulo, autor, isbn, disponible)
    self.dias_en_prestamo = dias_en_prestamo

  def prestar_libro(self):
    if self.disponible:
      self.disponible = False
      self.set_prestamos(self.get_prestamos() + 1) # Incrementa el número de préstamos
      return f"El libro físico *{self.titulo} ha sido prestado"
    return f"El libro físico *{self.titulo} no está disponible"

  def duracion_prestamo(self) -> int:
    return f"La duración del préstamo del libro físico *{self.titulo} es de {self.dias_en_prestamo} días"

class LibroDigital(Libro):
  def __init__(self, titulo, autor, isbn, disponible = True, dias_en_prestamo: int = 0):
    super().__init__(titulo, autor, isbn, disponible)
    self.dias_en_prestamo = dias_en_prestamo

  def prestar_libro(self):
    if self.disponible:
      self.disponible = False
      self.set_prestamos(self.get_prestamos() + 1) # Incrementa el número de préstamos
      return f"El libro digital *{self.titulo} ha sido prestado"
    return f"El libro digital *{self.titulo} no está disponible"

  def duracion_prestamo(self) -> int:
    return f"La duración del préstamo del libro digital *{self.titulo} es de {self.dias_en_prestamo} días"


class Biblioteca:
  def __init__(self, nombre):
    self.nombre = nombre
    self.libros = []
    self.usuarios = []

  def libros_disponibles(self):
    return [
      libro.titulo
      for libro in self.libros
      if libro.disponible
    ]


class Autor:
  def __init__(self, nombre, nacionalidad):
    self.nombre = nombre
    self.nacionalidad = nacionalidad
    self.libros = []  # Composición: lista de libros del autor

  def agregar_libro(self, libro):
    """Agrega un libro a la lista de libros del autor"""
    self.libros.append(libro)

  def listar_libros(self):
    return [libro.titulo for libro in self.libros]

  def total_libros(self):
    return len(self.libros)


# Instancia de la clase Libro
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "1234567890", True)
libro2 = Libro("1984", "George Orwell", "1234567890", True)
libro3 = LibroFisico("El principe de Persia", "Antoine de Saint-Exupéry", "1234567890", True, 10)
libro4 = LibroDigital("La ciudad de las sombras", "George Orwell", "1234567890", True, 10)

# Instancia de la clase Autor
autor1 = Autor("Antoine de Saint-Exupéry", "Francia")
autor2 = Autor("George Orwell", "Reino Unido")

# Agregar libros a cada autor según su autoría (composición)
autor1.agregar_libro(libro1)  # El principito
autor1.agregar_libro(libro3)  # El principe de Persia
autor2.agregar_libro(libro2)  # 1984
autor2.agregar_libro(libro4)  # La ciudad de las sombras

# Instancia de la clase Biblioteca
biblioteca = Biblioteca("Platzi Biblioteca")
biblioteca.libros = [libro1, libro2, libro3, libro4]
biblioteca.autores = [autor1, autor2]

# Lista de libros
listaCatalogo = [libro1, libro2, libro3, libro4]

# Imprimir el catálogo de libros
print("Catálogo de libros:")
for libro in listaCatalogo:
  print(libro)

print("================================================")
print(biblioteca.libros_disponibles())
print("================================================")
#print(libro1.__prestamos) # No se puede acceder al atributo privado
libro2.set_prestamos(100) # Cambia el valor del atributo privado
print(libro2.get_prestamos()) # Accede al atributo privado
print("================================================")
print(libro1.prestar_libro())
print(libro1.devolver_libro())
print(libro1.prestar_libro())
print(libro1.devolver_libro())
print(libro1.prestar_libro())
print(libro1.devolver_libro())
print(libro1.prestar_libro())
print(libro1.devolver_libro())
print(libro1.prestar_libro())
print(libro1.devolver_libro())
print(libro1.prestar_libro())
print(libro1.es_popular())
print(libro2.es_popular())
print("================================================")
libro3.dias_en_prestamo = 15
print(libro3.prestar_libro())
print(libro3.duracion_prestamo())
libro4.dias_en_prestamo = 8
print(libro4.prestar_libro())
print(libro4.duracion_prestamo())
print("================================================")
print(biblioteca.libros_disponibles())
print("================================================")
print(f"Libros de {autor1.nombre}: {autor1.listar_libros()}")
print(f"Total: {autor1.total_libros()} libros")
print(f"Libros de {autor2.nombre}: {autor2.listar_libros()}")
print(f"Total: {autor2.total_libros()} libros")