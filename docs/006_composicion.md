🧠Composición en Python (POO)

🎯 Idea central

🔸 La composición permite construir sistemas más flexibles y fáciles de mantener al combinar objetos existentes, en lugar de crear jerarquías rígidas con herencia.

🧩 En vez de “es un”, se usa “tiene un”.

⚙️ ¿Qué resuelve la composición?

✨ Combina objetos dentro de otros para ampliar funcionalidades.

 🔁 Reutiliza comportamientos ya creados.

 🧱 Evita construir todo desde cero.

 🚫 Rompe dependencias rígidas de la herencia.

 🏗️ Modela relaciones reales del dominio (ejemplo: la biblioteca tiene usuarios y libros).

🔍 Composición vs Herencia

📗 Herencia — “Es un”

Crea jerarquías (por ejemplo: el usuario es un profesor).
Buena para especializaciones directas.
📘 Composición — “Tiene un”

Combina instancias (por ejemplo: la biblioteca tiene libros).
Más flexible y adaptable.
✅ Regla práctica: Usa herencia para especializar. Usa composición para integrar.

📚 Ejemplo práctico: LibroFísico y LibroDigital

Protocolo base: LibroProtocol Métodos:

prestar()
devolver()
calcular_duración()
Clases concretas:

📖 LibroFísico → préstamo de 7 días.
💻 LibroDigital → préstamo de 14 días.
🔐 Cada clase mantiene el mismo contrato, pero define su propia lógica interna.

🏛️ Clase Biblioteca — Estructura general

Objetivo: Centralizar datos y acciones del dominio.

Constructor (__init__):

Guarda un nombre.
Crea dos listas vacías:
libros
usuarios
🧩 Ejemplo:

PlaziBiblioteca = Biblioteca("PlaziBiblioteca")

Colección inicial:

“MiLibro”
“MiLibroNoDisponible” (no disponible)
“OtroLibro”
📘 Cada libro tiene un atributo disponible (True o False).

Beneficios:

La biblioteca controla su catálogo.
Los estados de los libros son claros y fáciles de modificar.
🧱 Componentes clave de Biblioteca

🔹 Atributos

nombre → identifica la biblioteca.
libros → lista de libros gestionados.
usuarios → lista de usuarios registrados.
🔹 Control del estado

Cada libro tiene disponible = True/False.
🔹 Punto de acceso

Todos los métodos (como libros_disponibles) operan sobre estos atributos.
🔎 Método: libros_disponibles()

📜 Propósito: Devolver una lista con los títulos de libros disponibles.

Implementación:

class Biblioteca:

    def __init__(self, nombre):

        self.nombre = nombre

        self.libros = []

        self.usuarios = []

    def libros_disponibles(self):

        return [libro.titulo for libro in self.libros if libro.disponible]

📖 Cómo funciona:

Recorre la lista self.libros.
Filtra los que tienen disponible = True.
Devuelve una lista con sus títulos.
🧪 Ejemplo de uso:

print(PlaziBiblioteca.libros_disponibles())

💡 Resultado:

Si un libro está disponible → aparece en la lista.
Si no → se omite automáticamente.