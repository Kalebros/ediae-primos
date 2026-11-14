# Herencia y polimorfismo en Python

Cuando programas, a menudo te encontrarás con situaciones en las que varias clases comparten características parecidas. Por ejemplo:

- `Coche`, `Moto` y `Camión` son todos vehículos,
- `Perro`, `Gato` y `Pájaro` son todos animales,
- `CuentaBancaria` y `CuentaJoven` comparten comportamiento financiero.

En esos casos, la herencia ayuda a reutilizar código y a organizar mejor el programa.

Además, el polimorfismo permite que distintas clases respondan de forma distinta al mismo mensaje.

En esta guía también veremos:

- `abstract base classes` (ABC),
- decoradores comunes como `@property`, `@staticmethod` y `@classmethod`.

## 1. ¿Qué es la herencia?

La herencia permite crear una nueva clase a partir de otra existente.

La clase nueva se llama clase hija o subclase, y la clase de la que hereda se llama clase padre o superclase.

```python
class Animal:
    def hablar(self):
        print("Hace un sonido")

class Perro(Animal):
    pass
```

Aquí `Perro` hereda de `Animal`.

### Ejemplo:

```python
class Animal:
    def hablar(self):
        print("Hace un sonido")

class Perro(Animal):
    pass

p = Perro()
p.hablar()  # Hace un sonido
```

## 2. ¿Para qué sirve la herencia?

La herencia es útil cuando varias clases comparten comportamiento similar.

### Ejemplo:

```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        print(f"El vehículo {self.marca} está arrancando")

class Coche(Vehiculo):
    pass

class Moto(Vehiculo):
    pass

c = Coche("Toyota")
m = Moto("Kawasaki")

c.arrancar()
m.arrancar()
```

El código de `arrancar()` se define solo una vez en la clase base.

## 3. Sobrescribir métodos

Una clase hija puede modificar el comportamiento heredado.

```python
class Animal:
    def hablar(self):
        print("Hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("Miau")

perro = Perro()
gato = Gato()

perro.hablar()  # Guau
gato.hablar()   # Miau
```

Esto se conoce como sobrescritura de métodos.

## 4. ¿Qué es el polimorfismo?

El polimorfismo significa que distintas clases pueden responder al mismo mensaje de formas diferentes.

Aunque los objetos son distintos, todos comparten una interfaz o un nombre de método.

```python
class Perro:
    def hablar(self):
        print("Guau")

class Gato:
    def hablar(self):
        print("Miau")

class Pato:
    def hablar(self):
        print("Cuac")

animales = [Perro(), Gato(), Pato()]

for animal in animales:
    animal.hablar()
```

Salida:

```python
Guau
Miau
Cuac
```

Aunque cada clase tiene su propio `hablar()`, todas se usan igual desde el exterior.

## 5. Herencia y polimorfismo juntos

```python
class Animal:
    def hablar(self):
        print("Hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("Miau")

animales = [Perro(), Gato()]

for animal in animales:
    animal.hablar()
```

Esto es muy útil porque puedes trabajar con colecciones de objetos diferentes, pero todos comparten un comportamiento común.

## 6. `super()`

La función `super()` se usa para llamar al método de la clase padre desde la clase hija.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, puesto):
        super().__init__(nombre)
        self.puesto = puesto

empleado = Empleado("Ana", "Programadora")
print(empleado.nombre)  # Ana
print(empleado.puesto)  # Programadora
```

`super()` ayuda a reutilizar código de la clase padre.

## 7. Abstract Base Classes (ABC)

Las `abstract base classes` son clases diseñadas para ser usadas como plantillas.

No se espera que se creen instancias directamente de ellas, sino que sirvan como base para otras clases.

### ¿Para qué sirven?

Sirven para definir una interfaz común que las clases hijas deben implementar.

### Ejemplo con `ABC`

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("Miau")
```

### ¿Qué pasa si intentamos instanciar `Animal`?

```python
animal = Animal()
```

Esto da un error, porque `Animal` es abstracta.

### Beneficio de las ABC

Aseguran que todas las clases hijas implementen ciertos métodos obligatorios.

Esto reduce errores y vuelve el diseño más claro.

## 8. Decoradores en Python

Los decoradores son una forma de modificar o extender el comportamiento de una función o método sin cambiar su código principal.

Se escriben con `@`.

## 9. Decorador `@property`

`@property` permite tratar un método como si fuera un atributo.

```python
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

p = Persona("Ana")
print(p.nombre)  # Ana

p.nombre = "Luis"
print(p.nombre)  # Luis
```

### ¿Para qué sirve?

Hace que el acceso a atributos sea más controlado y claro.

## 10. Decorador `@staticmethod`

Un método estático no necesita acceso a `self` ni a ninguna instancia concreta.

```python
class Matematicas:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Matematicas.sumar(3, 4))  # 7
```

### ¿Cuándo usarlo?

Cuando la función no depende del estado de un objeto, sino que realiza una tarea útil de forma general.

## 11. Decorador `@classmethod`

Un método de clase recibe la clase como primer argumento, normalmente llamado `cls`.

```python
class Persona:
    total = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.total += 1

    @classmethod
    def contar_personas(cls):
        return cls.total

p1 = Persona("Ana")
p2 = Persona("Luis")

print(Persona.contar_personas())  # 2
```

### ¿Para qué sirve?

Se usa para comportamientos relacionados con la clase, no con una instancia concreta.

## 12. Decorador `@functools.lru_cache`

Este decorador sirve para guardar resultados de funciones costosas y reutilizarlos.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
```

Esto evita volver a calcular lo mismo muchas veces.

## 13. Decorador `@login_required` (ejemplo común en frameworks)

En frameworks web, `@login_required` se usa para restringir acceso a ciertas páginas o funciones.

```python
# Ejemplo conceptual
# @login_required
# def perfil():
#     return "Perfil del usuario"
```

Esto se usa para añadir comprobaciones antes de ejecutar la función.

## 14. Decoradores personalizados

También puedes crear tus propios decoradores.

```python
def saludo_decorador(funcion):
    def wrapper():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return wrapper

@saludo_decorador
def hola():
    print("Hola")

hola()
```

Salida:

```python
Antes de ejecutar la función
Hola
Después de ejecutar la función
```

## 15. Herencia con ABC y polimorfismo

Una estructura muy ordenada es combinar ABC con polimorfismo.

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

figuras = [Cuadrado(3), Circulo(2)]

for figura in figuras:
    print(figura.area())
```

Todos los objetos tienen un método `area()`, aunque cada clase lo calcula de una forma distinta.

## 16. Cuándo usar herencia

La herencia es útil cuando:

- varias clases tienen el mismo comportamiento base,
- quieres evitar duplicación de código,
- quieres representar relaciones del tipo “es un”.

Ejemplo:

- `Perro` es un `Animal`
- `Coche` es un `Vehiculo`
- `CuentaJoven` es una `CuentaBancaria`

## 17. Cuándo usar ABC

Usa ABC cuando quieres imponer una estructura común y asegurarte de que las clases hijas no olviden ciertos métodos.

## 18. Cuándo usar polimorfismo

Usa polimorfismo cuando distintas clases deben responder al mismo método, pero cada una lo implementa a su manera.

## 19. Resumen

### Herencia

Permite reutilizar código y crear clases especializadas a partir de otras.

### Polimorfismo

Permite que objetos distintos respondan al mismo método de forma distinta.

### ABC

Garantizan que las clases hijas implementen métodos obligatorios.

### Decoradores

Permiten cambiar o añadir comportamiento sin tocar la función original.

Los más útiles para empezar son:

- `@property`
- `@staticmethod`
- `@classmethod`

## 20. Consejo final

Cuando empieces a programar, intenta trabajar con ejemplos pequeños y claros:

- `Animal`, `Perro`, `Gato`
- `Vehiculo`, `Coche`, `Moto`
- `Figura`, `Cuadrado`, `Circulo`

Esto te ayudará a ver cómo herencia y polimorfismo permiten organizar mejor el código y evitar lógica duplicada.

Las ABC y los decoradores son herramientas más avanzadas, pero cuando se entienden bien, hacen que el código sea mucho más limpio y más fácil de mantener.
