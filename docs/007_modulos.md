🧩Organización modular de un proyecto en Python

🎯 Objetivo principal

Transformar el desorden del “código espagueti” en una estructura clara y modular. 🧠 Claves:

Separar responsabilidades.
Seguir la guía PEP 8.
Usar imports ordenados y útiles.
🚨 Problemas del código espagueti

❌ Todo en un solo archivo (<u>main.py</u>).

❌ Dificultad para ubicar clases o funciones.

❌ Código duplicado o mal organizado.

❌ Mantenimiento lento y propenso a errores.

📉 Resultado: deuda técnica y una arquitectura confusa.

✅ Ventajas de modularizar

🌱 Claridad estructural.

⚙️ Mantenimiento más simple.

🔁 Reutilización de clases.

🔍 Búsqueda más rápida.

🧩 Código escalable y limpio.

🧱 Pilares de una buena modularización

🔹 Una responsabilidad por archivo.

🔹 Clases separadas del código ejecutable.

🔹 Imports precisos para conectar los módulos.

🔹 Nada de código que se ejecute dentro de los módulos.

🔹 Lógica principal centralizada en main.py.

🗂️ Estructura recomendada del proyecto

📘 <u>Libros.py</u>

 → Define Libro y LibroFisico.

 → Todo lo relacionado con los libros.

🏛️ <u>Biblioteca.py</u>

 → Contiene la clase Biblioteca.

 → Gestiona préstamos y operaciones de biblioteca.

👩‍🎓 <u>Usuarios.py</u>

 → Define Estudiante, Profesor y el protocolo Solicitante.

 → Se encarga de los usuarios.

⚙️ <u>main.py</u>

 → Punto de entrada del sistema.

 → Crea objetos, conecta clases y ejecuta el flujo.

🔗 Cómo usar los imports

📍 Reglas clave:

Importa solo lo que necesites.
Agrupa varias clases del mismo módulo.
Coloca todos los imports al inicio del archivo.
Repetir imports está bien si se usan en varios lugares.
Usa nombres de archivo en plural si contienen varias clases.
Ejemplo (main.py):

from Usuarios import Estudiante, Profesor

from Libros import Libro, LibroFisico

from Biblioteca import Biblioteca

town_library = Biblioteca()

est1 = Estudiante("Ana")

prof1 = Profesor("Luis")

lib1 = Libro("Python 101")

lib2 = LibroFisico("Estructuras de Datos")

print(town_library.libros)

🧾 Orden de imports según PEP 8

📚 1. Biblioteca estándar: import os import sys

🌍 2. Librerías de terceros: import requests

🏗️ 3. Módulos propios del proyecto: from Usuarios import Estudiante, Profesor from Libros import Libro, LibroFisico from Biblioteca import Biblioteca

🔤 Dentro de cada grupo → orden alfabético.

⬜ Deja una línea en blanco entre grupos.

⚙️ Herramientas recomendadas

🧰 Ruff (en Visual Studio Code):

Organiza los imports automáticamente al guardar.
Ahorra tiempo y evita errores de formato.
💡 Tip adicional: Proyectos con archivos cortos y modulares ayudan a los modelos de lenguaje (LLMs) a analizar el código con menos costo y mejor contexto.