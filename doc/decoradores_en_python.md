# Decoradores en Python

Los decoradores son una técnica muy útil en Python para modificar o ampliar el comportamiento de una función o método sin cambiar directamente su código principal.

Piensa en ellos como una especie de envoltorio: una función original recibe una capa adicional que puede:

- validar argumentos,
- ejecutar algo antes o después,
- registrar información,
- comprobar permisos,
- medir tiempos,
- reutilizar lógica común.

## 1. ¿Qué es un decorador?

Un decorador es una función que recibe otra función y devuelve una nueva función con comportamiento añadido.

La sintaxis es esta:

```python
def decorador(funcion):
    def envoltorio():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return envoltorio
```

Y se usa con `@`:

```python
@decorador
def saludar():
    print("Hola")

saludar()
```

Resultado:

```python
Antes de ejecutar la función
Hola
Después de ejecutar la función
```

## 2. ¿Por qué son útiles?

Los decoradores permiten:

- evitar duplicar código,
- añadir lógica común a varias funciones,
- hacer programas más ordenados,
- reutilizar funcionalidades en varias partes del proyecto,
- aplicar validaciones o reglas a funciones concretas.

## 3. Cómo funciona realmente un decorador

Cuando escribes esto:

```python
@decorador
def saludar():
    print("Hola")
```

Python hace algo parecido a esto:

```python
saludar = decorador(saludar)
```

Es decir, reemplaza la función original por la nueva función devuelta por el decorador.

## 4. Decorador con argumentos

A veces quieres que el decorador reciba parámetros.

```python
def repetir(numero):
    def decorador(funcion):
        def envoltorio():
            for _ in range(numero):
                funcion()
        return envoltorio
    return decorador

@repetir(3)
def saludar():
    print("Hola")

saludar()
```

Salida:

```python
Hola
Hola
Hola
```

## 5. Decorador para funciones con parámetros

Muchas funciones reciben argumentos. Hay que escribir el envoltorio para aceptar cualquier número de parámetros.

```python
def log(funcion):
    def envoltorio(*args, **kwargs):
        print(f"Llamando a {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return envoltorio

@log
def sumar(a, b):
    return a + b

print(sumar(2, 3))
```

Salida:

```python
Llamando a sumar
Resultado: 5
5
```

## 6. Decorador `@property`

Es uno de los decoradores más comunes en Python.

Permite tratar un método como si fuera un atributo.

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
print(p.nombre)

p.nombre = "Luis"
print(p.nombre)
```

### ¿Para qué sirve?

Es muy útil para encapsular atributos y controlar su acceso de una forma más clara.

## 7. Decorador `@staticmethod`

Un método estático no depende de la instancia ni de la clase.

```python
class Matematicas:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Matematicas.sumar(5, 3))
```

### ¿Cuándo usarlo?

Cuando la función no necesita acceder a `self` ni a `cls`.

## 8. Decorador `@classmethod`

Un método de clase recibe la clase como primer argumento.

```python
class Persona:
    total = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.total += 1

    @classmethod
    def contar(cls):
        return cls.total

p1 = Persona("Ana")
p2 = Persona("Luis")
print(Persona.contar())
```

### ¿Para qué sirve?

Se usa para comportamientos relacionados con la clase, no con una instancia concreta.

## 9. Decorador `@functools.lru_cache`

Este decorador almacena resultados de una función para reutilizarlos si se vuelve a llamar con los mismos argumentos.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
```

### ¿Para qué sirve?

Optimiza funciones costosas y repetitivas, especialmente en cálculos o consultas.

## 10. Decorador `@wraps`

`@wraps` se usa normalmente junto con decoradores personalizados para conservar metadatos de la función original, como su nombre y su documentación.

```python
from functools import wraps

def decorador(funcion):
    @wraps(funcion)
    def envoltorio(*args, **kwargs):
        print("Antes")
        resultado = funcion(*args, **kwargs)
        print("Después")
        return resultado
    return envoltorio

@decorador
def saludar():
    """Función de saludo"""
    print("Hola")

print(saludar.__name__)
print(saludar.__doc__)
```

Esto mantiene la identidad de la función original más limpia.

## 11. Decoradores en pytest

`pytest` usa muchos decoradores para declarar pruebas y configurar comportamiento.

### `@pytest.mark.parametrize`

Permite ejecutar la misma prueba con varios valores.

```python
import pytest

@pytest.mark.parametrize("numero, esperado", [(1, 2), (2, 3), (5, 6)])
def test_sumar_uno(numero, esperado):
    assert numero + 1 == esperado
```

Esto permite probar muchos casos sin duplicar funciones.

### `@pytest.mark.skip`

Salta una prueba.

```python
import pytest

@pytest.mark.skip(reason="Todavía no está implementado")
def test_no_implementado():
    assert False
```

### `@pytest.mark.xfail`

Marca una prueba como esperada a fallar.

```python
import pytest

@pytest.mark.xfail(reason="Se conoce el fallo")
def test_esperado_a_fallar():
    assert 1 == 2
```

### `@pytest.fixture`

Se usa para crear datos o configuraciones reutilizables dentro de las pruebas.

```python
import pytest

@pytest.fixture
def numero():
    return 5


def test_suma(numero):
    assert numero + 2 == 7
```

`fixture` es muy útil para evitar repetir preparación del entorno de prueba.

## 12. Decorador `@pytest.raises`

Se usa para comprobar que una excepción ocurre como se espera.

```python
import pytest


def dividir(a, b):
    return a / b


def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
```

Esto es esencial para validar que el programa maneja errores de la forma esperada.

## 13. Decoradores en Flask y frameworks web

Muchos frameworks usan decoradores para asociar rutas o permisos a funciones.

Ejemplo conceptual:

```python
# @app.route("/login")
# def login():
#     return "Pantalla de login"
```

Esto permite que una función sea ejecutada cuando se accede a una URL concreta.

## 14. Decoradores personalizados para validación

Un caso típico es validar argumentos antes de ejecutar una función.

```python
def validar_edad(funcion):
    def envoltorio(edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        return funcion(edad)
    return envoltorio

@validar_edad
def mostrar_edad(edad):
    print(f"Edad: {edad}")

mostrar_edad(25)
```

## 15. Consejos al usar decoradores

- Usa decoradores cuando varias funciones comparten la misma lógica.
- Mantén los decoradores simples y claros.
- Usa `@wraps` cuando crees decoradores personalizados.
- Si estás escribiendo pruebas, familiarízate con los decoradores de `pytest`.

## 16. Resumen

Los decoradores permiten ampliar funciones sin reescribirlas por completo.

### Decoradores comunes en Python

- `@property`
- `@staticmethod`
- `@classmethod`
- `@lru_cache`
- `@wraps`

### Decoradores comunes en pytest

- `@pytest.mark.parametrize`
- `@pytest.mark.skip`
- `@pytest.mark.xfail`
- `@pytest.fixture`
- `@pytest.raises`

## 17. Consejo final

Si estás aprendiendo a programar, empieza por entender el patrón base: una función que recibe otra función y devuelve una nueva.

Cuando comprendes esa idea, los decoradores dejan de parecer magia y se convierten en una herramienta muy poderosa para escribir código más limpio, reutilizable y fácil de mantener.
