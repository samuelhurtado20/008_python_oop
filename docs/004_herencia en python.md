🧠HERENCIA SIMPLE EN PYTHON

🎯 Objetivo General

Aprender cómo la herencia simple permite reutilizar código en Python. 📚 Ejemplo práctico: un sistema de usuarios (Estudiante y Profesor) que heredan de una clase base llamada Usuario.

🧩 Concepto Clave

🔹 La herencia simple permite que una clase hija copie atributos y métodos de una clase padre.

👉 En este caso:

Usuario ➜ Clase base
Estudiante y Profesor ➜ Clases hijas
💡 ¿Por qué usar herencia?

✨ Beneficios principales:

🚫 Elimina código duplicado
🧭 Centraliza atributos y comportamientos comunes
🔧 Facilita extender con funciones nuevas
📏 Mantiene mensajes y respuestas consistentes
⚙️ Estructura General del Ejemplo

📁 Archivo: <u>usuarios.py</u>

📜 Estrategia: usar super() para acceder al constructor del padre sin mencionarlo directamente.

🧱 Diagrama Conceptual:

Usuario

 ├── Estudiante

 └── Profesor

👤 Clase Base: Usuario

🧩 Contiene los atributos y métodos comunes a todos los usuarios.

class Usuario:

    def __init__(self, nombre, cedula):

        self.nombre = nombre

        self.cedula = cedula

        self.libros_prestados = []

    def solicitar_libro(self, titulo):

        return f"Solicitud de libro '{titulo}' realizada."

🧠 Qué hace:

Guarda nombre y cédula.
Lleva el registro de libros prestados.
Define el método básico de solicitud.
🎓 Clase Hija: Estudiante

👨‍🎓 Añade el atributo carrera y un límite de 3 libros.

class Estudiante(Usuario):

    def __init__(self, nombre, cedula, carrera):

        super().__init__(nombre, cedula)

        self.carrera = carrera

        self.limite_libros = 3

📌 Diferencia clave: El estudiante solo puede prestar 3 libros.

🧑‍🏫 Clase Hija: Profesor

👩‍🏫 Hereda de Usuario, pero sin límite de libros.

class Profesor(Usuario):

    def __init__(self, nombre, cedula):

        super().__init__(nombre, cedula)

        self.limite_libros = None

📌 Diferencia clave: El profesor puede prestar todos los libros que desee.

🔁 Sobrescritura del Método solicitar_libro

Cada clase redefine (sobrescribe) el método según sus reglas:

🧱 Usuario

Mensaje genérico de solicitud.

def solicitar_libro(self, titulo):

    return f"Solicitud de libro '{titulo}' realizada."

🎓 Estudiante

Controla el número de préstamos.

def solicitar_libro(self, titulo):

    if len(self.libros_prestados) < self.limite_libros:

        self.libros_prestados.append(titulo)

        return f"Préstamo del libro '{titulo}' autorizado."

    else:

        return f"No puedes prestar más libros. Límite alcanzado: {self.limite_libros}."

🔍 Validación incluida:

✔️ Si hay espacio disponible → agrega el libro
❌ Si ya alcanzó el límite → muestra mensaje de advertencia
🧑‍🏫 Profesor

No valida el límite.

def solicitar_libro(self, titulo):

    self.libros_prestados.append(titulo)

    return f"Préstamo del libro '{titulo}' autorizado."

📘 Resultado: Todos los préstamos son aprobados.