🌟 Clases Abstractas en Python (ABC)

🔹 1. Concepto esencial

📌 Una clase abstracta = un contrato. Define qué debe existir en cada subclase, no cómo debe funcionar. Imagina: planos de un edificio → siempre deben tener puertas y ventanas.

🔹 2. Elementos fundamentales

🎯 Para crear una clase abstracta necesitas:

🧩 Heredar de ABC
🏷️ Decorar métodos obligatorios con @abstractmethod
🚫 No instanciar la clase hasta que todo esté implementado
⚡ Python validará el contrato al ejecutar
🛡️ Mayor robustez que Protocol → aquí sí se revisa en runtime
🔹 3. Cómo se ve una clase abstracta

🧱 Estructura del contrato

from abc import ABC, abstractmethod

class UsuarioBase(ABC):

    @abstractmethod

    def solicitar_libro(self):

        pass

👉 Representa:

📜 Un método que todas las subclases deben crear
❗ Sin implementación en la clase base
🔹 4. Cómo luce una subclase que cumple el contrato

🛠️ Implementación obligatoria

class Usuario(UsuarioBase):

    def solicitar_libro(self):

        # Lógica específica de la subclase

        ...

✔ Permite instanciar la clase ✔ Satisface los métodos del contrato ✔ Mantiene la interfaz uniforme

🔹 5. ¿Qué valida Python al ejecutar?

⚠️ Detección automática de errores

Python revisa el contrato cuando corres:

python main.py

Si falta un método abstracto:

💥 TypeError → “No puedes instanciar esta clase, te falta implementar algo”.

🔹 6. Qué pasa al agregar un nuevo método abstracto

🔧 Actualizas el contrato en la clase base

class UsuarioBase(ABC):

    @abstractmethod

    def solicitar_libro(self):

        pass

    @abstractmethod

    def metodo_de_prueba(self):

        pass

➡️ Ahora todas las subclases deben cumplir el nuevo método.

✔ Corrección en la subclase:

class Usuario(UsuarioBase):

    def solicitar_libro(self):

        ...

    def metodo_de_prueba(self):

        return "Método de prueba para saber cómo funciona ABC"

🟢 Al implementar el nuevo método, la aplicación vuelve a funcionar.

🔹 7. Mini–guía rápida (checklist visual)

✅ Ejecuta: python <u>main.py</u> ➕ Agrega método con @abstractmethod

🔁 Ejecuta de nuevo

⚠️ Observa el TypeError

🛠️ Implementa lo que falta

🟢 Vuelve a ejecutar → ¡todo en orden!

🔹 8. Cuándo usarlas

💡 Las clases abstractas son ideales cuando quieres:

🔒 Contratos estrictos
🧭 Interfaces coherentes
🧱 Estructuras comunes en múltiples subclases
🧰 Frameworks o librerías robustas