🧠Encapsulación en Python

🔒 CONCEPTO CLAVE

Encapsulación = Protección + Control de acceso

 👉 Oculta los detalles internos de una clase.

 👉 Evita que los datos se modifiquen directamente desde fuera.

 👉 Mantiene la integridad del sistema.

💡 Ejemplo: Como en un banco, tú no entras a la bóveda: hablas con el cajero. En Python, tampoco accedes al atributo, sino que usas métodos.

📚 CASO PRÁCTICO: UNA BIBLIOTECA

Cada Libro tiene:

 📘 Título

 🔢 Veces prestado

 ✅ Disponibilidad

Y solo puede modificarse a través de métodos controlados.

⚙️ CÓMO EVITAR INCONSISTENCIAS

🔹 Controla la disponibilidad

Si el libro está disponible → se presta.
Si no → muestra “No está disponible”.
🔹 Evita valores vacíos o None Siempre devuelve un mensaje claro.

🔹 Lleva un contador interno Cada vez que se presta, el contador aumenta.

🔹 Define popularidad

Método es_popular()
Retorna True si el libro fue prestado más de 5 veces.
⚠️ ERROR COMÚN

Si haces:

libro.veces_prestado = 10

❌ El sistema puede mostrar “11 préstamos” sin que haya ocurrido realmente.

➡️ Consecuencia: se rompe la integridad de los datos.

✅ Solución: Encapsular el atributo y acceder solo mediante métodos.

🔤 GUIONES BAJOS Y PROTECCIÓN

Python usa guiones para marcar el nivel de acceso.

🔸 Un guion bajo → _atributo

Ejemplo: _veces_prestado
Es una advertencia, no una barrera.
Significa: “no modifiques esto desde fuera”.
🔹 Doble guion bajo → __atributo

Ejemplo: __veces_prestado
Activa el name mangling (renombrado interno).
🚫 Impide acceder directamente desde fuera.
Si lo intentas, obtendrás un error.







👉👉Variables protegidas y privadas

👉Protegido (_): un SOLO guión bajo. Úsame con cuidado, especialmente útil en herencia
👉Privado (__): doble guión bajo. Realmente no deberías tocar esto, ni siquiera en subclases
Variables protegidas _variable

Se marcan con un solo guión bajo y sugieren: "Este atributo es interno, pero las subclases pueden usarlo si lo necesitan". La idea es que están disponibles dentro de la clase y sus herederas.