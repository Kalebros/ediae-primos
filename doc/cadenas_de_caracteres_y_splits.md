# Cadenas de caracteres en Python

Las cadenas de caracteres, o `strings`, son secuencias de texto. En Python, se escriben entre comillas simples o dobles:

```python
nombre = "Ana"
frase = 'Estoy aprendiendo Python'
```

Las cadenas se usan constantemente para mostrar mensajes, leer nombres, procesar textos y trabajar con datos de usuarios.

## 1. ¿Qué es una cadena de caracteres?

Una cadena es una colección ordenada de caracteres. Cada carácter ocupa una posición, como en una lista.

```python
mensaje = "Python"
print(mensaje[0])  # P
print(mensaje[1])  # y
print(mensaje[2])  # t
```

En Python, los índices empiezan en `0`.

## 2. Longitud de una cadena

Para saber cuántos caracteres tiene una cadena, usamos `len()`.

```python
texto = "Hola mundo"
print(len(texto))  # 10
```

`len()` devuelve la cantidad total de caracteres, incluyendo espacios.

## 3. Concatenación

Podemos unir cadenas con `+`.

```python
nombre = "Lucía"
apellido = "Pérez"
print(nombre + " " + apellido)  # Lucía Pérez
```

También podemos repetir una cadena con `*`:

```python
print("ha" * 3)  # hahaha
```

## 4. Acceso a caracteres

Puedes acceder a un carácter concreto usando índices:

```python
palabra = "Python"
print(palabra[0])  # P
print(palabra[-1])  # n
```

Los índices negativos cuentan desde el final:

```python
print(palabra[-2])  # o
```

## 5. Slicing (rebanado de cadenas)

Las cadenas también soportan slices, al igual que las listas.

```python
frase = "Aprendiendo Python"
print(frase[0:10])   # Aprendiendo
print(frase[:10])    # Aprendiendo
print(frase[11:])    # Python
print(frase[::-1])   # nohtyP oinednerpA
```

### Sintaxis

```python
cadena[inicio:fin:paso]
```

- `inicio`: posición inicial
- `fin`: posición final, sin incluirla
- `paso`: cada cuántos caracteres se avanza

Ejemplo:

```python
texto = "abcdefghij"
print(texto[1:8:2])  # bdfh
```

## 6. Métodos más útiles de cadenas

Python trae muchos métodos incorporados para trabajar con texto. Aquí tienes los más comunes.

### 6.1 `lower()`

Convierte todos los caracteres a minúsculas.

```python
mensaje = "HOLA MUNDO"
print(mensaje.lower())  # hola mundo
```

### 6.2 `upper()`

Convierte todos los caracteres a mayúsculas.

```python
mensaje = "hola mundo"
print(mensaje.upper())  # HOLA MUNDO
```

### 6.3 `capitalize()`

Pone en mayúscula la primera letra y el resto en minúsculas.

```python
texto = "hola mundo"
print(texto.capitalize())  # Hola mundo
```

### 6.4 `strip()`

Elimina espacios al principio y al final de la cadena.

```python
texto = "   hola   "
print(texto.strip())  # hola
```

### 6.5 `find()`

Busca una subcadena dentro de otra y devuelve su posición.

```python
frase = "Aprendiendo Python"
print(frase.find("Python"))  # 12
```

Si no la encuentra, devuelve `-1`.

```python
print(frase.find("Java"))  # -1
```

### 6.6 `replace()`

Reemplaza un texto por otro.

```python
frase = "Me gusta el cafe"
print(frase.replace("cafe", "té"))  # Me gusta el té
```

También puedes reemplazar varias veces:

```python
texto = "manzana manzana manzana"
print(texto.replace("manzana", "pera"))  # pera pera pera
```

### 6.7 `split()`

Divide una cadena en una lista de subcadenas según un separador.

```python
frase = "uno dos tres"
print(frase.split())  # ['uno', 'dos', 'tres']
```

Si pasamos un carácter específico:

```python
correo = "ana@example.com"
print(correo.split("@"))  # ['ana', 'example.com']
```

Otro ejemplo:

```python
fecha = "2025-11-14"
print(fecha.split("-"))  # ['2025', '11', '14']
```

### 6.8 `join()`

Une una lista de cadenas usando un separador.

```python
palabras = ["Python", "es", "genial"]
print(" ".join(palabras))  # Python es genial
```

También podemos unir con comas:

```python
print(", ".join(palabras))  # Python, es, genial
```

### 6.9 `startswith()` y `endswith()`

Comprueban si una cadena empieza o termina con un valor concreto.

```python
frase = "Hola mundo"
print(frase.startswith("Hola"))  # True
print(frase.endswith("mundo"))  # True
```

## 7. Comparación de cadenas

Puedes comparar cadenas con operadores:

```python
print("hola" == "hola")  # True
print("hola" != "adios")  # True
print("a" < "b")  # True
```

Python compara cadenas según el orden alfabético.

## 8. Formateo de cadenas

A menudo necesitas construir frases con valores variables.

### Con f-strings

Las f-strings son la forma más moderna y clara de hacerlo.

```python
nombre = "Sofía"
edad = 20
print(f"Me llamo {nombre} y tengo {edad} años")
```

Salida:

```python
Me llamo Sofía y tengo 20 años
```

### Con concatenación

También puedes hacerlo así:

```python
nombre = "Sofía"
print("Me llamo " + nombre)
```

Pero las f-strings son más legibles.

## 9. Ejemplo práctico completo

```python
frase = "  Aprendiendo Python desde cero  "
print(frase.strip())

frase_limpia = frase.strip()
print(frase_limpia.lower())
print(frase_limpia.upper())
print(frase_limpia.find("Python"))
print(frase_limpia.replace("Python", "JavaScript"))

palabras = frase_limpia.split()
print(palabras)
print("-".join(palabras))
```

Salida esperada:

```python
Aprendiendo Python desde cero
aprendiendo python desde cero
APRENDIENDO PYTHON DESDE CERO
1
Aprendiendo JavaScript desde cero
['Aprendiendo', 'Python', 'desde', 'cero']
Aprendiendo-Python-desde-cero
```

## 10. Errores comunes

### 1. Mezclar tipos

```python
edad = 25
print("Mi edad es " + edad)
```

Esto da error porque `edad` es un número, no una cadena. Debes convertirlo:

```python
print("Mi edad es " + str(edad))
```

### 2. Usar `find()` y esperar un booleano

`find()` devuelve la posición, no `True` o `False`.

```python
texto = "hola"
print(texto.find("h"))  # 0
```

Si quieres saber si existe, puedes combinarlo con `!= -1`:

```python
print(texto.find("x") != -1)  # False
```

## 11. Resumen

Las cadenas de caracteres son una de las estructuras más importantes en Python. Con ellas puedes:

- almacenar texto,
- transformar mayúsculas/minúsculas,
- buscar palabras,
- reemplazar texto,
- separar frases en palabras,
- unir listas de palabras.

### Métodos más usados

- `lower()`: convierte a minúsculas
- `upper()`: convierte a mayúsculas
- `find()`: busca una subcadena
- `replace()`: reemplaza texto
- `split()`: divide la cadena
- `join()`: une elementos de una lista
- `strip()`: elimina espacios

## 12. Consejo final

Cuando empiezas a programar, practicar con cadenas es imprescindible. Muchas tareas reales implican leer texto, procesar formularios, validar emails o manipular nombres de archivos. Cuanto más practiques con `split()`, `join()` y `replace()`, más fácil te resultará trabajar con datos de texto.

Recuerda: el texto no es solo información, también es entrada y salida del programa.
