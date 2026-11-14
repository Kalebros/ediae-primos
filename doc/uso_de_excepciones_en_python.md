# Uso de excepciones en Python

Cuando programas, hay muchas cosas que pueden salir mal: un archivo no existe, una operación matemática es imposible, se introduce un valor incorrecto o una variable no tiene el tipo que esperamos.

Para evitar que el programa se rompa de golpe, Python usa las excepciones.

En esta guía aprenderás:

- qué es una excepción,
- cómo usar `try`, `except` y `finally`,
- qué errores comunes hay,
- cómo manejar errores de forma clara y segura.

## 1. ¿Qué es una excepción?

Una excepción es un error que ocurre durante la ejecución del programa.

Cuando Python encuentra un problema, lanza una excepción. Si no la manejamos, el programa se detiene y muestra un mensaje de error.

Ejemplo:

```python
print(10 / 0)
```

Esto lanza una excepción:

```python
ZeroDivisionError: division by zero
```

## 2. ¿Por qué usar excepciones?

Las excepciones permiten controlar errores sin que el programa termine de forma abrupta.

Esto ayuda a:

- evitar bloqueos del programa,
- informar al usuario con mensajes claros,
- seguir ejecutando el resto del código cuando algo falla,
- escribir programas más robustos.

## 3. `try` y `except`

La estructura básica es:

```python
try:
    # Código que puede fallar
except:
    # Código que se ejecuta si ocurre un error
```

### Ejemplo:

```python
try:
    numero = int("abc")
except:
    print("Ha ocurrido un error al convertir el valor")
```

Aquí el programa no se rompe: el error se captura y se responde de forma controlada.

## 4. `except` con tipos de error

En lugar de capturar cualquier error, es mejor manejar tipos específicos.

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

Esto hace el código más claro y más fácil de mantener.

### Ejemplo con varios errores

```python
try:
    numero = int("hola")
except ValueError:
    print("El valor introducido no es un número válido")
except TypeError:
    print("Se ha usado un tipo incorrecto")
```

## 5. `else`

El bloque `else` se ejecuta si el código dentro de `try` no lanza ninguna excepción.

```python
try:
    numero = int("5")
except ValueError:
    print("Eso no es un número válido")
else:
    print("La conversión fue correcta")
```

## 6. `finally`

El bloque `finally` siempre se ejecuta, haya o no haya error.

```python
try:
    archivo = open("archivo.txt", "r", encoding="utf-8")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
finally:
    print("Esto se ejecuta siempre")
```

`finally` se usa mucho para:

- cerrar archivos,
- liberar recursos,
- ejecutar limpieza final.

## 7. Ejemplo completo con `try`, `except`, `else` y `finally`

```python
try:
    numero = int(input("Introduce un número: "))
except ValueError:
    print("Debes introducir un número válido")
else:
    print(f"Has introducido el número {numero}")
finally:
    print("Proceso terminado")
```

## 8. Errores comunes en Python

Aquí tienes algunos de los más habituales:

### `ZeroDivisionError`

Se produce al dividir entre cero.

```python
print(10 / 0)
```

### `ValueError`

Se produce cuando una función recibe un valor incorrecto.

```python
int("hola")
```

### `TypeError`

Se produce cuando se usa un tipo incorrecto para una operación.

```python
"hola" + 5
```

### `FileNotFoundError`

Se produce cuando se intenta abrir un archivo que no existe.

```python
open("archivo_que_no_existe.txt", "r")
```

### `IndexError`

Se produce cuando se accede a una posición inválida en una lista.

```python
lista = [1, 2, 3]
print(lista[10])
```

### `KeyError`

Se produce cuando una clave no existe en un diccionario.

```python
persona = {"nombre": "Ana"}
print(persona["edad"])
```

## 9. Capturar errores con mensajes útiles

Es recomendable mostrar mensajes claros al usuario.

```python
try:
    edad = int(input("Introduce tu edad: "))
except ValueError:
    print("Error: debes introducir un número entero.")
else:
    print(f"Tu edad es {edad}")
```

## 10. Lanzar excepciones manualmente

Podemos crear errores con `raise`.

```python
edad = -5

if edad < 0:
    raise ValueError("La edad no puede ser negativa")
```

Esto permite controlar situaciones que no son válidas en la lógica del programa.

## 11. Excepciones personalizadas

También puedes crear tus propias excepciones.

```python
class MiError(Exception):
    pass

try:
    raise MiError("Se ha producido un error personalizado")
except MiError as e:
    print(e)
```

Las excepciones personalizadas son útiles cuando tu proyecto necesita tipos de errores específicos.

## 12. Ejemplo práctico: validación de entrada del usuario

```python
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Tu edad registrada es {edad}")
finally:
    print("Fin del programa")
```

## 13. Buenas prácticas al manejar excepciones

### 1. Captura errores específicos

Es mejor manejar errores concretos que capturar todo con un `except:` sin más.

```python
try:
    numero = int("hola")
except ValueError:
    print("Has introducido un valor incorrecto")
```

### 2. No ocultes errores sin informar

Si ocurre un error, suele ser útil mostrar un mensaje útil.

### 3. Usa `finally` para limpieza

Por ejemplo, cerrar archivos, conexiones o liberar recursos.

### 4. Haz mensajes claros

Un buen mensaje ayuda a diagnosticar el problema.

## 14. Ejemplo con archivo

```python
try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("No se encontró el archivo")
finally:
    print("Se cerró la operación de lectura")
```

## 15. Resumen

Las excepciones permiten manejar errores en Python sin que el programa termine de forma inesperada.

### Estructura básica

```python
try:
    # código que puede fallar
except TipoDeError:
    # manejar el problema
else:
    # se ejecuta si no hay error
finally:
    # se ejecuta siempre
```

### ¿Qué hace cada bloque?

- `try`: contiene el código arriesgado
- `except`: maneja el error
- `else`: se ejecuta si todo va bien
- `finally`: se ejecuta siempre

## 16. Consejo final

Cuando empieces a programar, es normal que aparezcan errores. La clave no es evitarlos siempre, sino saber cómo manejarlos con elegancia.

Aprender a usar `try`, `except` y `finally` te ayudará a crear programas más seguros, más útiles y mucho más profesionales.
