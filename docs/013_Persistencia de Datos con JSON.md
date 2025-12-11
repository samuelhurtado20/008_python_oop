🧩Persistencia de Datos con JSON en Python

🎯 1. Concepto esencial: ¿qué es la persistencia?

La persistencia permite que tu aplicación recuerde su estado cada vez que se ejecuta.

🔸 Qué implica:

Transformar objetos de Python → JSON
Guardar ese JSON en un archivo
Cargarlo luego para reconstruir el estado previo
Validar y manejar errores para evitar datos corruptos
📌 Idea resumen: 👉 "Serializa, guarda, valida y luego reconstruye."

🧱 2. Clase principal: Persistencia

📌 Propósito:

Un único punto central para leer y guardar la información de tu sistema.

🔧 Estructura base:

class Persistencia:

    def __init__(self, archivo="biblioteca.json"):

        self.archivo = archivo

🎒 Lo que aporta:

Archivo por defecto: biblioteca.json
Organización limpia
Acceso controlado al almacenamiento
📤 3. Guardar datos de forma segura

🧰 Herramienta clave: with open

Garantiza:

Cierre automático del archivo
Escritura segura
Menos errores
with open(self.archivo, "w", encoding="utf-8") as f:

    json.dump(datos, f, indent=2, ensure_ascii=False)

🔍 Parámetros importantes:

"w" → escribir desde cero
utf-8 → soporta tildes y ñ
indent=2 → JSON legible
ensure_ascii=False → no escapa caracteres españoles
📚 4. ¿Qué información guardar?

🎒 Elementos recomendados:

nombre de la biblioteca
lista de usuarios
lista de libros
fecha de guardado (opcional pero muy útil)
🔄 Conversión de objetos → diccionarios

📌 JSON solo acepta tipos básicos, así que debes convertir objetos:

datos = {

    "nombre": biblioteca.nombre,

    "usuarios": [dict(usuario) for usuario in biblioteca.usuarios],

    "libros": [dict(libro) for libro in biblioteca.libros],

}

🧩 Visualízalo así: Objeto → dict → JSON → archivo

🕒 5. Añadir fecha de guardado (sello temporal)

🎯 ¿Por qué incluirlo?

Auditoría
Control de cambios
Registro histórico del sistema
Ejemplo conceptual:

# datos["fecha_guardado"] = DateTime.now().ISOFormat()

📌 Sencillo, pero poderoso para seguir la evolución del estado.