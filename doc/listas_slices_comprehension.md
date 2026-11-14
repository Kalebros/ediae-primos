# Listas, slices y comprehensions en Python

Una lista es una estructura de datos muy útil para guardar varios elementos en una sola variable. En Python, las listas son una de las formas más comunes de representar colecciones de datos.

## 1. ¿Qué es una lista?

Una lista es una secuencia ordenada de elementos. Puede contener números, cadenas, booleanos, objetos e incluso otras listas.

```python
frutas = ["manzana", "banana", "cereza"]
nums = [1, 2, 3, 4, 5]
mezcla = ["hola", 42, True, [1, 2, 3]]
```

Las listas se escriben entre corchetes `[]` y cada elemento va separado por comas.

### Características principales

- Son ordenadas: el primer elemento ocupa la posición 0.
- Pueden cambiarse después de crearlas.
- Pueden contener elementos repetidos.
- Se usan mucho para almacenar colecciones dinámicas.

## 2. Acceso a elementos

Cada elemento de una lista tiene una posición llamada índice.

```python
frutas = ["manzana", "banana", "cereza"]

print(frutas[0])  # manzana
print(frutas[1])  # banana
print(frutas[2])  # cereza
```

Si intentamos acceder a un índice que no existe, Python lanza un error:

```python
print(frutas[99])
# IndexError: list index out of range
```

También puedes leer desde el final usando índices negativos:

```python
frutas = ["manzana", "banana", "cereza"]

print(frutas[-1])  # cereza
print(frutas[-2])  # banana
```

## 3. Slices o rebanadas

Los slices permiten obtener una porción de la lista.

La sintaxis es:

```python
lista[inicio:fin:paso]
```

- `inicio`: índice donde empieza.
- `fin`: índice donde termina (sin incluirlo).
- `paso`: cuántos elementos avanzar.

### Ejemplos:

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:6])   # [2, 3, 4, 5]
print(numeros[:4])    # [0, 1, 2, 3]
print(numeros[4:])    # [4, 5, 6, 7, 8, 9]
print(numeros[::2])   # [0, 2, 4, 6, 8]
print(numeros[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### Importante

El slice no modifica la lista original; devuelve una nueva lista.

```python
nums = [10, 20, 30, 40, 50]
sublista = nums[1:4]

print(nums)      # [10, 20, 30, 40, 50]
print(sublista)   # [20, 30, 40]
```

### Slice con paso negativo

Podemos recorrer la lista al revés:

```python
letras = ["a", "b", "c", "d", "e"]
print(letras[::-1])  # ['e', 'd', 'c', 'b', 'a']
```

Esto es útil cuando quieres invertir una lista sin cambiarla directamente.

## 4. Modificar listas

Las listas son mutables, es decir, pueden cambiar después de crearse.

### Cambiar un valor

```python
colores = ["rojo", "azul", "verde"]
colores[1] = "amarillo"
print(colores)  # ['rojo', 'amarillo', 'verde']
```

### Añadir elementos

```python
colores = ["rojo", "azul"]
colores.append("verde")
print(colores)  # ['rojo', 'azul', 'verde']
```

`append()` añade un elemento al final.

```python
colores = ["rojo", "verde"]
colores.insert(1, "azul")
print(colores)  # ['rojo', 'azul', 'verde']
```

`insert(posicion, elemento)` inserta en una posición concreta.

```python
colores = ["rojo", "verde"]
colores.extend(["azul", "amarillo"])
print(colores)  # ['rojo', 'verde', 'azul', 'amarillo']
```

`extend()` añade varios elementos a la vez.

### Eliminar elementos

```python
colores = ["rojo", "azul", "verde"]
colores.remove("azul")
print(colores)  # ['rojo', 'verde']
```

`remove()` elimina la primera coincidencia.

```python
colores = ["rojo", "azul", "verde"]
valor = colores.pop()
print(valor)    # verde
print(colores)  # ['rojo', 'azul']
```

`pop()` elimina y devuelve el último elemento si no se indica índice.

```python
colores = ["rojo", "azul", "verde"]
print(colores.pop(1))  # azul
print(colores)         # ['rojo', 'verde']
```

También puedes hacer:

```python
colores = ["rojo", "azul", "verde"]
del colores[1]
print(colores)  # ['rojo', 'verde']
```

## 5. Métodos más utilizados de listas

Estos son algunos de los métodos más comunes:

```python
numeros = [5, 2, 8, 2, 1]
```

### `len(lista)`

Devuelve cuántos elementos hay en la lista.

```python
print(len(numeros))  # 5
```

### `lista.count(valor)`

Cuenta cuántas veces aparece un valor.

```python
print(numeros.count(2))  # 2
```

### `lista.index(valor)`

Devuelve la posición de la primera coincidencia.

```python
print(numeros.index(8))  # 2
```

### `lista.sort()`

Ordena la lista in-place.

```python
numeros.sort()
print(numeros)  # [1, 2, 2, 5, 8]
```

### `lista.reverse()`

Invierte el orden de la lista.

```python
numeros.reverse()
print(numeros)  # [8, 5, 2, 2, 1]
```

### `lista.copy()`

Crea una copia de la lista.

```python
copia = numeros.copy()
print(copia)
```

### `lista.clear()`

Elimina todos los elementos.

```python
numeros.clear()
print(numeros)  # []
```

## 6. List comprehensions

Las list comprehensions son una forma breve y clara de crear listas a partir de otras secuencias.

### Sintaxis

```python
[nueva_expresion for elemento in iterable if condicion]
```

### Ejemplo básico

```python
cuadrados = [x * x for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]
```

Esto equivale a:

```python
cuadrados = []
for x in range(1, 6):
    cuadrados.append(x * x)
```

### Con condición

```python
pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]
```

### Con transformación

```python
nombres = ["ana", "juan", "pedro"]
mayusculas = [nombre.upper() for nombre in nombres]
print(mayusculas)  # ['ANA', 'JUAN', 'PEDRO']
```

### Comprehension anidada

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
planar = [valor for fila in matriz for valor in fila]
print(planar)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Ventajas

- Código más corto.
- Más legible en muchos casos.
- Muy útil para transformar datos.

### Cuándo evitarlas

Cuando la lógica se vuelve muy compleja, un `for` normal puede ser más claro.

Ejemplo:

```python
# Esto se puede volver difícil de leer
result = [funcion(complicada(x)) for x in datos if condicion(x)]
```

En ese caso, es mejor usar un bucle normal para facilitar mantenimiento.

## 7. Iterar sobre una lista

Puedes recorrer una lista con `for`:

```python
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
```

También puedes recorrerla con índice:

```python
for i, fruta in enumerate(frutas):
    print(i, fruta)
```

`enumerate()` devuelve tanto el índice como el valor.

## 8. Lista vs tupla

Python tiene dos estructuras muy parecidas: listas y tuplas.

### Lista

```python
numeros = [1, 2, 3]
numeros.append(4)
print(numeros)  # [1, 2, 3, 4]
```

Las listas son mutables: puedes cambiar, añadir o eliminar elementos.

### Tupla

```python
numeros = (1, 2, 3)
# numeros.append(4)  # Error
```

Las tuplas son inmutables. Eso significa que no puedes cambiar sus elementos después de crearlas.

```python
punto = (10, 20)
# punto[0] = 15  # TypeError: 'tuple' object does not support item assignment
```

### Diferencias clave

| Estructura | Mutable | Sintaxis | Uso típico |
|---|---|---|---|
| Lista | Sí | `[1, 2, 3]` | Datos que cambian |
| Tupla | No | `(1, 2, 3)` | Datos fijos, seguros |

### Por qué usar tuplas

Las tuplas son útiles cuando quieres representar datos que no deben cambiar durante el programa, por ejemplo:

```python
coordenadas = (40.7128, -74.0060)
```

O cuando quieres proteger datos de cambios accidentales.

### Inmutabilidad

La inmutabilidad significa que una vez creada la tupla, su contenido no puede modificarse. Esto puede ayudarte a evitar errores y hacer más seguro el código.

Por ejemplo:

```python
dias = ("lunes", "martes", "miércoles")
```

Aquí no se puede hacer:

```python
dias[0] = "domingo"
```

Porque Python impide esa modificación.

## 9. Cuando elegir cada una

### Usa una lista si:

- necesitas añadir o quitar elementos,
- quieres ordenar o filtrar dinámicamente,
- vas a modificar los datos durante la ejecución.

### Usa una tupla si:

- los datos son fijos,
- quieres evitar cambios accidentales,
- quieres representar valores que forman una unidad, por ejemplo coordenadas, fechas o configuraciones estáticas.

## 10. Resumen

- Las listas son secuencias mutables.
- Se crean con `[]`.
- Se accede a sus elementos con índices.
- Los slices permiten obtener sublistas.
- Las list comprehensions sirven para crear listas de forma compacta.
- Los métodos `append`, `extend`, `insert`, `pop` y `remove` son muy útiles.
- Las tuplas son similares, pero inmutables.

### Ejemplo final

```python
# Lista mutable
notas = [8, 6, 9, 10]
notas.append(7)
print(notas)  # [8, 6, 9, 10, 7]

# Tupla inmutable
puntuacion = (8, 6, 9)
# puntuacion.append(7)  # Error
```

## 11. Consejo final

Cuando empieces a programar, practica mucho con listas: crear, recorrer, ordenar, filtrar y modificar elementos. Eso te ayudará a entender mejor cómo funcionan los datos en Python y te preparará para estructuras más avanzadas como diccionarios, conjuntos y clases.

Recuerda: una lista te sirve para cambiar datos; una tupla te sirve para proteger datos.
