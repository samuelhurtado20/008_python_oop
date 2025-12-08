🧠POLIMORFISMO Y PROTOCOL EN PYTHON

🚀 Idea Central

El polimorfismo permite que distintos objetos respondan al mismo mensaje de forma diferente. En Python, su poder crece al combinarlo con typing.Protocol:

💡 Protocol = contrato flexible + verificación estática

 ➡️ No exige herencia.

 ➡️ Cualquier objeto que tenga los métodos necesarios puede participar.

 ➡️ Se mantiene la esencia del duck typing, pero con seguridad de tipos.

🧩 Cómo Protocol potencia el polimorfismo

🔸 Mismo mensaje → resultados distintos

🔸 Sin herencia: solo hay que cumplir el contrato

🔸 Ayuda del editor: valida si falta algún método

📘 Ejemplo mental: solicitar_libro() funciona distinto para un Estudiante y un Profesor.

🦆 Duck Typing + Protocol

“Si camina como un pato y hace cuac como un pato, es un pato.”

🐤 En Python, no importa la clase, solo que tenga los métodos esperados.

🧱 Protocol convierte ese principio flexible en algo formal y comprobable:

Define contratos claros.
Permite validación por herramientas de tipos.
Mantiene la flexibilidad del lenguaje.
⚙️ Definir un contrato con typing.Protocol

📥 Importa y declara el protocolo:

from typing import Protocol

class SolicitanteProtocol(Protocol):

    def solicitar_libro(self, titulo: str) -> str:

        """Retorna el resultado de la solicitud de préstamo."""

        ...

🎯 Claves del ejemplo:

Hereda de Protocol.
Firma del método: titulo: str → retorna str.
Usa ... para indicar que no hay implementación.
Cualquier clase que tenga ese método cumple el contrato.
🚫 Cómo el editor detecta errores

Si tipas una lista con SolicitanteProtocol, el editor revisa cada elemento.

class Libro:

    def __init__(self, titulo, autor, isbn):

        self.titulo = titulo

        self.autor = autor

        self.isbn = isbn

usuarios: list[SolicitanteProtocol] = []

usuarios.append(Libro("Título", "Autor", "ISBN"))  

# ❌ Error: no implementa solicitar_libro

⚠️ Beneficio: detectas fallos antes de ejecutar el programa.

🔁 Listas tipadas + polimorfismo en acción

class Estudiante:

    def solicitar_libro(self, titulo):

        return f"Préstamo autorizado para estudiante: {titulo}"

class Profesor:

    def solicitar_libro(self, titulo):

        return f"Préstamo autorizado para profesor: {titulo}"

usuarios: list[SolicitanteProtocol] = [Estudiante(), Profesor()]

for usuario in usuarios:

    print(usuario.solicitar_libro("Título de prueba"))

🔹 Qué ocurre:

Cada objeto ejecuta su propia versión de solicitar_libro.
El mismo mensaje → distintos resultados.
Si un objeto no cumple el contrato, el editor lo marca como error.