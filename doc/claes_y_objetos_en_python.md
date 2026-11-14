# Clases y objetos en Python

Cuando programas, a menudo necesitas representar cosas del mundo real o del problema que estás resolviendo. Por ejemplo:

- una persona,
- un coche,
- un libro,
- un producto,
- un usuario,
- una cuenta bancaria.

Para modelar estas entidades, Python usa clases y objetos.

## 1. ¿Qué es una clase?

Una clase es un molde o plantilla que define cómo debe ser un tipo de objeto.

Por ejemplo, una clase `Persona` puede describir que una persona tiene:

- un nombre,
- una edad,
- una ciudad.

Y también puede definir comportamientos, como saludar o mostrar su edad.

```python
class Persona:
    pass
```

La palabra reservada `class` sirve para crear una clase.

## 2. ¿Qué es un objeto?

Un objeto es una instancia concreta de una clase.

```python
persona1 = Persona()
persona2 = Persona()
```

Aunque ambas son objetos de la misma clase, cada uno puede tener su propio estado.

## 3. Atributos

Los atributos son las características del objeto.

Por ejemplo, una persona puede tener:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Aquí:

- `self` hace referencia al propio objeto
- `self.nombre` y `self.edad` son atributos del objeto

### Ejemplo:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)

print(p1.nombre)  # Ana
print(p2.edad)    # 30
```

## 4. Métodos

Los métodos son funciones que pertenecen a la clase y describen comportamientos del objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

p1 = Persona("Ana", 25)
p1.saludar()
```

Salida:

```python
Hola, soy Ana y tengo 25 años
```

## 5. El constructor `__init__`

El método `__init__` se ejecuta cuando se crea un objeto.

Se usa para inicializar los atributos del objeto.

```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

c1 = Coche("Toyota", "Corolla")
print(c1.marca)   # Toyota
print(c1.modelo)  # Corolla
```

Es el punto de entrada principal para preparar un objeto con datos iniciales.

## 6. Encapsulación básica

Python no fuerza tanto la encapsulación como otros lenguajes, pero sí se usa una convención: los atributos con un guion bajo bajo indican que no deben usarse directamente fuera de la clase.

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    def obtener_saldo(self):
        return self._saldo
```

Esto ayuda a crear código más ordenado y menos propenso a errores.

## 7. Objetos y estado

Cada objeto tiene su propio estado.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)

print(p1.edad)  # 25
print(p2.edad)  # 30
```

Aunque ambos son de la misma clase, no comparten el mismo valor para sus atributos.

## 8. ¿Por qué usar clases?

Las clases ayudan a organizar mejor el código cuando el programa crece.

### Ventajas:

- agrupan datos y comportamiento,
- hacen el código más claro,
- permiten crear muchos objetos similares,
- evitan duplicar lógica,
- facilitan el mantenimiento.

## 9. Ejemplo más completo

```python
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def info(self):
        return f"{self.titulo} escrito por {self.autor}, {self.paginas} páginas"

libro1 = Libro("El Quijote", "Cervantes", 600)
print(libro1.info())
```

Salida:

```python
El Quijote escrito por Cervantes, 600 páginas
```

## 10. `self` en Python

`self` es una referencia al objeto actual.

Es necesario para diferenciar:

- atributos del objeto,
- variables locales o parámetros del método.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombre)
```

Aquí `self.nombre` hace referencia al atributo del objeto, no a una variable independiente.

## 11. ¿Qué son las dataclasses?

Las `dataclass` son una forma más rápida y limpia de crear clases cuya función principal es almacenar datos.

En lugar de escribir manualmente `__init__`, `__repr__` y otros métodos repetitivos, Python lo hace por ti.

### Ejemplo sin dataclass

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
```

### Ejemplo con dataclass

```python
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

p = Persona("Ana", 25)
print(p)  # Persona(nombre='Ana', edad=25)
```

Esto genera automáticamente un constructor y una representación legible.

## 12. Ventajas de las dataclasses

Las dataclasses son muy útiles cuando una clase solo sirve para contener información.

### Ventajas:

- menos código repetitivo,
- más legible,
- más fácil de mantener,
- ayudan a modelar objetos de datos,
- se usan mucho en proyectos reales.

### Ejemplo práctico

```python
from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int

p1 = Producto("Laptop", 1200.50, 7)
print(p1)
```

Salida:

```python
Producto(nombre='Laptop', precio=1200.5, stock=7)
```

## 13. Cuando usar dataclasses

Las dataclasses son ideales para:

- usuarios,
- productos,
- pedidos,
- libros,
- configuraciones simples,
- cualquier objeto que principalmente almacene datos.

No son necesariamente la mejor opción para clases con lógica muy compleja o con muchos métodos de negocio.

## 14. Ejemplo con dataclass y métodos

```python
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

p = Persona("Marta", 28)
p.saludar()
```

Salida:

```python
Hola, soy Marta y tengo 28 años
```

## 15. Diferencia entre clase normal y dataclass

### Clase normal

```python
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
```

### Dataclass

```python
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    email: str
```

La dataclass hace todo mucho más corto y ordenado cuando tu objetivo es guardar datos.

## 16. Casos de uso recomendados

### Usa clases cuando:

- necesitas encapsular lógica más compleja,
- el objeto realiza acciones o decisiones,
- se necesita una estructura más rica que solo datos.

### Usa dataclasses cuando:

- el objeto se usa principalmente para guardar información,
- deseas escribir menos código,
- quieres que la representación sea automática y clara.

## 17. Resumen

Las clases nos permiten modelar entidades del programa como objetos con:

- atributos: datos del objeto,
- métodos: acciones que puede hacer,
- estado: valores concretos que tiene cada instancia.

Las dataclasses son una forma más elegante y práctica de crear clases con datos.

### En resumen:

- `class` se usa para definir molde de objetos.
- un `object` es una instancia de esa clase.
- `__init__` prepara un objeto al crearlo.
- `self` hace referencia al objeto actual.
- `dataclass` reduce mucho código cuando la clase solo representa datos.

## 18. Consejo final

Cuando empiezas a programar, lo más útil es practicar con clases pequeñas y sencillas:

- `Persona`
- `Coche`
- `Producto`
- `Libro`
- `Cuenta`

Eso te ayudará a entender cómo los objetos almacenan información y cómo la lógica del programa puede organizarse mejor.

Las clases son una de las bases fundamentales de la programación orientada a objetos, y las dataclasses te permiten empezar de forma más limpia y clara.
