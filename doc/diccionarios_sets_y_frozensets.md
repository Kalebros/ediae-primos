# Diccionarios, sets y frozensets en Python

Cuando empiezas a programar, pronto te das cuenta de que no todo se guarda mejor en listas. A veces necesitas estructuras que te permitan:

- guardar datos con una clave y un valor,
- eliminar duplicados,
- comprobar si un elemento existe rápidamente,
- recorrer colecciones de forma eficiente.

Para eso existen los diccionarios y los sets.

## 1. ¿Qué es un diccionario?

Un diccionario en Python es una estructura de datos que guarda pares `clave: valor`.

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
```

Aquí:

- `"nombre"` es la clave
- `"Ana"` es el valor
- `"edad"` es otra clave
- `25` es su valor

### ¿Para qué sirven?

Los diccionarios son ideales cuando quieres asociar información:

```python
alumno = {
    "nombre": "Luis",
    "curso": "Python",
    "nota": 9.5
}
```

Se usan mucho para guardar información de usuarios, productos, configuraciones, resultados, etc.

## 2. Crear un diccionario

```python
vacio = {}
persona = {"nombre": "Ana", "edad": 25}
```

También puedes construirlo con `dict()`:

```python
persona = dict(nombre="Ana", edad=25)
print(persona)  # {'nombre': 'Ana', 'edad': 25}
```

## 3. Acceder a valores

Para acceder a un valor se usa la clave:

```python
persona = {"nombre": "Ana", "edad": 25}

print(persona["nombre"])  # Ana
print(persona["edad"])   # 25
```

Si intentas acceder a una clave que no existe, Python lanza un error:

```python
print(persona["apellidos"])
# KeyError: 'apellidos'
```

### Usa `.get()` para un acceso más seguro

```python
print(persona.get("apellidos", "No existe"))
```

`.get()` devuelve un valor por defecto si la clave no existe.

## 4. Modificar y añadir elementos

### Añadir un nuevo par clave-valor

```python
persona = {"nombre": "Ana"}
persona["edad"] = 25
print(persona)  # {'nombre': 'Ana', 'edad': 25}
```

### Modificar un valor existente

```python
persona["edad"] = 26
print(persona)  # {'nombre': 'Ana', 'edad': 26}
```

### Eliminar elementos

```python
persona.pop("edad")
print(persona)  # {'nombre': 'Ana'}
```

También puedes usar `del`:

```python
del persona["nombre"]
```

## 5. Recorrer un diccionario

### Recorriendo claves

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

for clave in persona:
    print(clave)
```

Esto recorre solo las claves.

### Recorriendo claves y valores

```python
for clave, valor in persona.items():
    print(clave, valor)
```

`items()` devuelve pares `(clave, valor)`.

### Recorriendo solo los valores

```python
for valor in persona.values():
    print(valor)
```

## 6. Métodos más utilizados de diccionarios

### `keys()`

Devuelve una vista con todas las claves.

```python
persona = {"nombre": "Ana", "edad": 25}
print(persona.keys())  # dict_keys(['nombre', 'edad'])
```

### `values()`

Devuelve una vista con todos los valores.

```python
print(persona.values())  # dict_values(['Ana', 25])
```

### `items()`

Devuelve pares clave-valor.

```python
print(persona.items())  # dict_items([('nombre', 'Ana'), ('edad', 25)])
```

### `update()`

Combina otro diccionario con el actual.

```python
persona = {"nombre": "Ana", "edad": 25}
persona.update({"ciudad": "Madrid"})
print(persona)
```

### `copy()`

Crea una copia del diccionario.

```python
copia = persona.copy()
```

### `clear()`

Elimina todos los elementos.

```python
persona.clear()
print(persona)  # {}
```

### `pop()`

Elimina y devuelve el valor de una clave.

```python
persona = {"nombre": "Ana", "edad": 25}
print(persona.pop("edad"))  # 25
```

## 7. Diccionarios y comprehension

La comprehension también funciona con diccionarios.

### Ejemplo básico

```python
cuadrados = {x: x * x for x in range(1, 6)}
print(cuadrados)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Esto crea un diccionario donde cada número tiene como valor su cuadrado.

### Con condición

```python
pares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print(pares)
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

### A partir de una lista de tuplas

```python
pares = [("nombre", "Ana"), ("edad", 25)]
diccionario = dict(pares)
print(diccionario)
```

Las comprehensions son útiles si quieres crear estructuras complejas de manera breve y legible.

## 8. ¿Qué es un set?

Un `set` es una colección de elementos únicos, sin orden fijo.

```python
numeros = {1, 2, 3, 4, 4, 5}
print(numeros)  # {1, 2, 3, 4, 5}
```

Los sets no permiten duplicados. Si introduces varios iguales, se eliminan.

### Características principales

- No tienen orden
- No admiten elementos duplicados
- Son útiles para hacer comprobaciones rápidas
- Se crean con llaves `{}`

```python
colores = {"rojo", "azul", "verde", "rojo"}
print(colores)
```

Salida:

```python
{'rojo', 'azul', 'verde'}
```

## 9. Operaciones con sets

### Añadir elementos

```python
numeros = {1, 2, 3}
numeros.add(4)
print(numeros)  # {1, 2, 3, 4}
```

### Eliminar elementos

```python
numeros.remove(2)
print(numeros)  # {1, 3, 4}
```

También se puede usar `discard()`:

```python
numeros.discard(99)
```

`discard()` no falla si el elemento no existe, mientras que `remove()` sí falla.

### Comprobar si un elemento está en el set

```python
numeros = {1, 2, 3}
print(2 in numeros)  # True
```

Esto es muy eficiente en sets.

## 10. Operaciones entre sets

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### Unión

```python
print(A | B)  # {1, 2, 3, 4, 5, 6}
```

### Intersección

```python
print(A & B)  # {3, 4}
```

### Diferencia

```python
print(A - B)  # {1, 2}
```

### Diferencia simétrica

```python
print(A ^ B)  # {1, 2, 5, 6}
```

## 11. Set comprehension

También puedes crear sets con comprehension.

```python
cuadrados = {x * x for x in range(1, 6)}
print(cuadrados)  # {1, 4, 9, 16, 25}
```

### Con filtro

```python
pares = {x for x in range(1, 11) if x % 2 == 0}
print(pares)  # {2, 4, 6, 8, 10}
```

Los sets son ideales cuando quieres trabajar con colecciones sin duplicados.

## 12. ¿Qué es un frozenset?

Un `frozenset` es como un `set`, pero inmutable.

```python
s = frozenset({1, 2, 3})
print(s)
```

### Diferencia principal

- `set`: mutable, puedes añadir o quitar elementos.
- `frozenset`: inmutable, no puedes modificarlo.

```python
s = frozenset({1, 2, 3})
# s.add(4)  # Error: 'frozenset' object has no attribute 'add'
```

### ¿Cuándo se usa?

Se usa cuando quieres una colección de elementos únicos que no deba alterarse.

```python
configuracion = frozenset({"modo", "debug", "prod"})
```

## 13. Diferencia entre lista, diccionario, set y frozenset

| Estructura | Se usa para | Permite duplicados | Es mutable |
|---|---|---|---|
| Lista | guardar elementos secuenciales | Sí | Sí |
| Diccionario | guardar pares clave-valor | Claves únicas | Sí |
| Set | guardar elementos únicos | No | Sí |
| Frozenset | guardar elementos únicos inmutables | No | No |

## 14. ¿Qué es un iterable?

Un iterable es cualquier objeto que se puede recorrer elemento a elemento.

En Python, muchos tipos son iterables, por ejemplo:

- listas
- cadenas
- diccionarios
- sets
- tuplas

```python
for letra in "Python":
    print(letra)
```

```python
for numero in [1, 2, 3, 4]:
    print(numero)
```

```python
for clave, valor in {"a": 1, "b": 2}.items():
    print(clave, valor)
```

### Importante

Un iterable no siempre es una lista. Puede ser una cadena, un diccionario o cualquier objeto que soporte la iteración.

La palabra clave es: “puede recorrerse”.

## 15. Iterables y loops

Los bucles `for` trabajan con iterables.

```python
for elemento in [10, 20, 30]:
    print(elemento)
```

Saber esto te ayuda a entender por qué muchas funciones de Python aceptan listas, tuplas, strings y sets:

```python
sum([1, 2, 3])
len("hola")
" ".join(["a", "b", "c"])
```

## 16. Ejemplo práctico con diccionario

```python
productos = {
    "manzana": 2.5,
    "pera": 3.0,
    "uva": 2.0
}

for fruta, precio in productos.items():
    print(f"La {fruta} cuesta {precio} euros")
```

## 17. Ejemplo práctico con set

```python
usuarios = {"Ana", "Luis", "Ana", "Marta"}
print(usuarios)
# {'Ana', 'Luis', 'Marta'}
```

En un set, no hay duplicados.

## 18. Resumen

### Diccionario

- Guarda pares `clave: valor`
- Las claves son únicas
- Muy útil para asociar información
- Se recorre con `items()`, `keys()` y `values()`

### Set

- Guarda elementos únicos
- No tiene orden fijo
- Muy útil para eliminar duplicados y comprobar pertenencia

### Frozenset

- Igual que un set, pero inmutable
- Útil cuando quieres una colección “fija”

### Iterable

- Cualquier estructura que se puede recorrer elemento a elemento
- Es una idea clave en Python

## 19. Consejo final

Cuando empieces a programar, te darás cuenta de que estas estructuras aparecen casi siempre:

- listas para secuencias ordenadas,
- diccionarios para datos con clave-valor,
- sets para elementos únicos,
- frozensets para colecciones inmutables.

La clave está en elegir la estructura correcta según el problema que quieres resolver.

Si usas la estructura adecuada, el código suele ser más claro, más rápido y menos propenso a errores.
