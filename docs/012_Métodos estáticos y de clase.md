🧠✨Métodos estáticos y de clase en Python

🔹 1. @staticmethod

💡 Idea principal: Lógica independiente dentro de la clase

🧩 Características

No recibe self
No recibe cls
Funciona como una función normal, pero ubicada dentro de una clase
Útil para validaciones y operaciones auxiliares
🛠 Ejemplo: Validación de ISBN

class Biblioteca:

    @staticmethod

    def validar_isbn(isbn: str) -> bool:

        return len(isbn) >= 10

▶ Cómo se usa

Biblioteca.validar_isbn("1234567890")

🟦 Visualízalo así

📦 Clase → contiene tareas auxiliares
🧰 Método → herramienta disponible sin instanciar
🔍 Resultado → True o False
🔹 2. @classmethod

💡 Idea principal: Crear objetos usando la clase como referencia

🧩 Características

Recibe cls como primer argumento
Crea instancias alternativas
Permite reglas propias de construcción
🛠 Ejemplo: Libro no disponible

class Libro:

    @classmethod

    def crear_no_disponible(cls, titulo, autor, isbn):

        return cls(titulo, autor, isbn, disponible=False)

▶ Cómo se usa

Libro.crear_no_disponible("Título", "Autor", "1234567890")

🟩 Visualízalo así

🏭 Clase → fábrica de objetos
🎛 Método → receta alternativa
📘 Resultado → objeto con disponible=False