🧠HERENCIA EN PYTHON

🌳 1. IDEA PRINCIPAL

La herencia permite que una clase (hija) reutilice código de otra (padre). Es como un árbol familiar de clases: lo común se define una vez en la raíz y se comparte hacia abajo.

🟩 Objetivo:

Evitar duplicación
Mantener orden
Reutilizar lógica
Facilitar mantenimiento
Permitir polimorfismo
🔗 2. RELACIÓN “ES UN TIPO DE”

Imagina que cada clase responde a esta pregunta:

¿Es un tipo de...?

💡 Ejemplos:

Estudiante → es un tipo de Usuario
Profesor → es un tipo de Usuario
🧩 Resultado: Ambos heredan lo esencial, pero pueden comportarse distinto.

⚙️ 3. COMPONENTES CLAVE

🧱 Clase padre (base)

Contiene lo común.
Ejemplo: Usuario
Define atributos y métodos compartidos.
🌱 Clases hijas (derivadas)

Heredan del padre.
Añaden o modifican comportamiento.
✏️ Override (sobrescritura)

Permite cambiar un método sin alterar el original.
🎭 Polimorfismo

Mismo método → diferentes respuestas según la clase.
🧬 Herencia múltiple

Una clase combina más de un rol.
Python da prioridad al primer padre declarado.
📘 4. EJEMPLO: SISTEMA DE BIBLIOTECA

👤 Clase base → Usuario

🔹 Atributos: nombre, cedula 🔹 Método: solicitar_libro(titulo)

class Usuario:

    def __init__(self, nombre, cedula):

        self.nombre = nombre

        self.cedula = cedula

    def solicitar_libro(self, titulo):

        return f"Solicitud de '{titulo}' registrada para {self.nombre}."

🎓 Clase hija → Estudiante

🔸 Atributos nuevos: libros_prestados, carrera, limite_libros

🔸 Sobrescribe solicitar_libro() con validaciones:

✅ La carrera debe estar activa
✅ No debe exceder el límite de libros
class Estudiante(Usuario):

    def __init__(self, nombre, cedula, libros_prestados=0, carrera=None, limite_libros=3):

        super().__init__(nombre, cedula)

        self.libros_prestados = libros_prestados

        self.carrera = carrera

        self.limite_libros = limite_libros

    def solicitar_libro(self, titulo):

        if not self.carrera:

            return "No se puede prestar: carrera inactiva o no registrada."

        if self.libros_prestados >= self.limite_libros:

            return "No se puede prestar: alcanzó el límite de libros."

        return super().solicitar_libro(titulo)

👨‍🏫 Clase hija → Profesor

🔸 Atributo nuevo: departamento 🔸 Sobrescribe solicitar_libro() para validar el departamento.

class Profesor(Usuario):

    def __init__(self, nombre, cedula, departamento=None):

        super().__init__(nombre, cedula)

        self.departamento = departamento

    def solicitar_libro(self, titulo):

        if not self.departamento:

            return "No se puede prestar: departamento no asignado."

        return super().solicitar_libro(titulo)

🧑‍🏫🎓 Clase combinada → ProfesorEstudiante

🔹 Hereda de Profesor y Estudiante 🔹 Prioriza el comportamiento del Profesor

class ProfesorEstudiante(Profesor, Estudiante):

    pass

🪜 5. JERARQUÍA VISUAL

Usuario

├── Estudiante

│    ├── libros_prestados

│    ├── carrera

│    └── limite_libros

├── Profesor

│    └── departamento

└── ProfesorEstudiante (Profesor + Estudiante)