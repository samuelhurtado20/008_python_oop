🎨Manejo Profesional de Errores en Python

────────────────────────────────────────

🎯 PROPÓSITO

Construir programas seguros, claros y a prueba de fallos usando:

 👉 try

 👉 except

 👉 raise

 👉 excepciones personalizadas

────────────────────────────────────────

🧱 1. Evitar que el programa se detenga

🔍 Problema

Entradas incorrectas → el programa se cae.

🛠 Solución

🟦 try: intenta ejecutar la acción.
🟧 except: reacciona solo a los errores esperados.
🔴 Evitar: except: genérico (oculta problemas reales).
⚠️ Errores frecuentes

📌 Título vacío
📌 None como entrada
📌 Datos corruptos
────────────────────────────────────────

📝 2. Validación de entradas

✔ Principio clave

Antes de continuar → verifica la validez.

💡 Si algo no es válido:

Lanza un raise con un mensaje claro.

⚙️ Ejemplo ilustrativo

if not titulo:

    raise ValueError("El título no es válido.")

────────────────────────────────────────

🧰 3. Buen uso de try y except

✔ Cómo hacerlo bien

✨ Maneja los errores en la capa superior (por ejemplo, en main).
✨ Informa al usuario con mensajes comprensibles.
✨ Captura solo lo necesario.
❌ Cómo NO hacerlo

No ocultes errores con except: vacío.
Ejemplo visual:

try:

    estudiante.solicitar_libro(None)

except Exception:

    print("Error: no se pudo solicitar el libro.")

────────────────────────────────────────

🚨 4. Qué es raise

💥 Idea clave

Interrumpe inmediatamente el flujo. Después del raise → nada más se ejecuta.

🧭 Cuándo usarlo

Condición inválida detectada
La operación no puede continuar
Otro módulo debe decidir cómo resolverlo
────────────────────────────────────────

🧱 5. Excepciones personalizadas

🎨 ¿Por qué usarlas?

Más expresividad
Código profesional
Jerarquías claras
Capturas específicas sin silenciar otros errores
🧬 Ejemplo de jerarquía

class BibliotecaError(Exception): pass

class TituloInvalidoError(BibliotecaError): pass

⭐ Ventajas visuales

🎯 Captura solo el dominio que te interesa
🧩 type(e) permite diagnóstico rápido
🔍 Nombres que explican claramente qué falló
────────────────────────────────────────

🔗 6. Ejemplo integrado

🧠 En la lógica de negocio

if not titulo:

    raise TituloInvalidoError("El título no es válido.")

🖥 En el programa principal

try:

    estudiante.solicitar_libro(None)

except BibliotecaError as e:

    print("Error:", e)