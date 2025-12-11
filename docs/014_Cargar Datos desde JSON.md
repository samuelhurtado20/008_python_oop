🎯Cargar y Reconstruir Datos desde JSON en Python

🟦 1. META PRINCIPAL

🔍 "Leer un JSON, convertirlo en objetos y restaurar toda la app."

Reconstruyes:

🏛 Biblioteca
📚 Libros físicos
👩‍🎓 Estudiantes
👨‍🏫 Profesores
¿Para qué? ➡ Para que la app recupere su estado exacto cada vez que se ejecuta.

🟧 2. EL CAMINO COMPLETO

🚀 JSON → diccionario → instancias → Biblioteca lista

Pasos clave:

📥 Leer archivo (with open)
🔄 Convertir a diccionario (json.load)
🧱 Construir objetos según sus claves
🔁 Cargar libros y usuarios
🎁 Devolver la biblioteca reconstruida
🟩 3. EL MÉTODO cargar_datos

🧩 ¿Qué hace exactamente?

❗ Solo recibe self
📂 Abre archivo en "r" con encoding consistente
📦 Carga todo en un diccionario datos
🏗 Construye Biblioteca + Libros + Usuarios
🔙 Retorna una biblioteca completamente funcional
🟪 4. LECTURA DEL ARCHIVO JSON

📚 Cómo hacerlo bien

🧠 Reglas de oro:

Usa with open → evita errores y cierra solo
Mantén el mismo encoding de guardado
Usa json.load → convierte a diccionario lista para usar
🧰 Esquema mental:

📂 abrir archivo  

⬇  

📦 cargar como diccionario  

⬇  

🏗 reconstruir objetos  

🟫 5. RECONSTRUCCIÓN DEL MUNDO (Biblioteca)

🟫🟦 5.1 Crear la Biblioteca

🔹 Dato clave: "nombre"

Ejemplo mental: ➡ biblioteca.nombre = datos["nombre"]

🟫🟧 5.2 Crear libros

📚 Cada libro necesita:

título
autor
isbn
disponible
🔁 Proceso visual:

🔄 recorrer datos["libros"]

      ↳ crear LibroFisico(...)

      ↳ biblioteca.libros.append(libro)

⭐ La disponibilidad se conserva tal como estaba.

🟫🟩 5.3 Crear usuarios

🔍 Cómo reconocerlos:

Si tiene "carrera" → 🎓 Estudiante
Si NO la tiene → 👨‍🏫 Profesor
🔁 Flujo:

🔄 recorrer datos["usuarios"]

      ↳ detectar tipo

      ↳ crear instancia

      ↳ biblioteca.usuarios.append(usuario)

💡 Mejora futura: guardar "tipo": "estudiante" o "tipo": "profesor" en el JSON.

🟦 6. INTEGRAR TODO EN main.py

🧭 Ruta recomendada:

🛠 Importar Persistencia
⚡ Cargar biblioteca
▶ Ejecutar la app
💾 Guardar cambios al final