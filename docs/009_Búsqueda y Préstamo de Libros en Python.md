🌟Sistema de Búsqueda y Préstamo de Libros en Python

🔵 1. Propósito del sistema

📚 Buscar libros por título

 🔐 Validar disponibilidad antes del préstamo

 ⚠️ Gestionar errores con excepciones

 🗂️ Utilizar datos externos desde el módulo Data

 🧑‍🏫 Interactuar con el usuario desde consola

🗂️ 2. Componentes del Proyecto

🧱 Módulo Data

⭐ 10 libros
👩‍🎓 10 estudiantes
🏛️ Clases involucradas

Biblioteca
Usuario
Estudiante → hereda de Usuario
🖥️ main.py

Importa datos de Data
Limpia listas locales antiguas
Conserva el profesor
Ejecuta el flujo completo
🔌 3. Integrando Data en main.py

Pasos esenciales

🔹 Importar listas desde Data

🔹 Borrar listas de libros/estudiantes previas en <u>main.py</u>

🔹 Asignar las importadas a las variables centrales

🔹 Ejecutar:

python main.py

🧑‍💻 4. Entradas que pide el programa

🔸 Cédula del usuario → identifica al estudiante

 🔸 Título del libro → mediante:

 input("Digite el título del libro: ")

🔍 5. Búsqueda del Libro en Biblioteca

🎯 Objetivo del método buscarolibro

Recorrer libros
Comparar títulos
Verificar si está disponible
Retornar libro si coincide
Lanzar LibroNoDisponibleError si no existe o está prestado
🧩 Implementación (visual)

class Biblioteca:

    def buscarolibro(self, titulo):

        for libro in self.libros:

            if libro.titulo == titulo and libro.disponible:

                return libro

        raise LibroNoDisponibleError(

            f"El libro {titulo} no está disponible o no existe"

        )

🛡️ 6. Manejo de Errores (try/except)

🎯 Uso recomendado:

try → lo que puede fallar
except → manejar error con claridad
titulo = input("Digite el título del libro: ")

try:

    libro = biblioteca.buscarolibro(titulo)

    print(f"El libro que seleccionaste es {libro.titulo} por {libro.autor}")

except LibroNoDisponibleError as e:

    print(f"Error: {e}")

⭐ Formato claro de error: Error: mensaje

📚 7. Flujo completo de Solicitud + Préstamo

1️⃣ Autorización del estudiante

usuario.solicitar_libro(titulo)
Retorna mensaje (autorizado o no)
2️⃣ Préstamo ejecutado desde Libro

El método prestar():

Verifica disponibilidad
Cambia disponible a False
Aumenta contador de préstamos
Puede lanzar LibroNoDisponibleError
🔧 Ejemplo visual

resultado = usuario.solicitar_libro(titulo)

print("\n" + resultado)

try:

    resultado_prestar = libro.prestar()

    print(resultado_prestar)

except LibroNoDisponibleError as e:

    print(f"Error: {e}")