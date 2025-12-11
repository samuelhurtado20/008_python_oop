🎓✨@property en Python

🏁 Concepto esencial

@property = acceder a un método como si fuera un atributo. Limpio, natural, controlado y 100% pythónico.

🧱 1. ¿Por qué usar @property?

🌟 Beneficios inmediatos

🔹 Acceso sin paréntesis

🔹 Encapsulación real sin cambiar cómo se usa

🔹 Validación automática de valores

🔹 Cálculo interno invisible para el usuario

🔹 Interfaces más limpias y mantenibles

💡 Te permite:

✔ Crear atributos de solo lectura

✔ Controlar la escritura con un setter

✔ Generar valores derivados sin métodos extras

🛠 2. Cómo crear una propiedad

🔄 Transformar un getter clásico

Antes: método get_... Después: propiedad accesible con punto.

🧩 Ejemplo rápido

class Libro:

    def __init__(self, titulo, autor, ISBN):

        self.titulo = titulo

        self.autor = autor

        self.ISBN = ISBN

        self._veces_prestado = 0

    @property

    def veces_prestado(self):

        return self._veces_prestado

▶ Uso

for libro in libros_disponibles():

    print(libro.titulo, libro.veces_prestado)

📌 Nota visual: sin paréntesis → como un atributo.

🔐 3. Controlar la escritura: el setter

🎛 ¿Por qué un setter?

Porque te permite validar, rechazar y controlar lo que entra a tu objeto.

🧰 Ejemplo

@veces_prestado.setter

def veces_prestado(self, valor):

    if valor > 0:

        self._veces_prestado = valor

    else:

        raise ValueError("El valor debe ser mayor a cero")

🚨 Qué ocurre

Valor correcto → ✔ se asigna
Valor no válido → ❌ ValueError
Resultado → Estado interno siempre coherente
🔢 4. Propiedades calculadas (sin setter)

🧠 ¿Qué son?

Propiedades que no guardan datos, sino que calculan algo en el momento.

🎨 Ejemplo visual

@property

def descripcion_completa(self):

    return f"{self.titulo} por {self.autor} {self.ISBN}"

▶ Uso

print(libro.descripcion_completa)

💎 Beneficio: información compuesta sin métodos ruidosos.

🧭 5. Integración en main y en la biblioteca

🔗 Reglas visuales

📘 Devuelve objetos, no cadenas 👆 Accede a los datos así:

libro.titulo
libro.veces_prestado
libro.descripcion_completa
▶ Prueba todo ejecutando: python main.py