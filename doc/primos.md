# Guía de `app/primos.py` para principiantes

En este archivo hay dos funciones:

- `es_primo(numero: int, primos_conocidos: list[int]) -> bool`
- `generar_primos(valor_maximo: int) -> list[int]`

Su objetivo es **calcular números primos**.

---

## 1. ¿Qué es una función?

Una función es un bloque de código con un nombre que realiza una tarea concreta.  
Sirve para reutilizar código y organizar mejor un programa.

En Python se declara con `def`:

```python
def nombre_funcion(parametros):
    # instrucciones
    return resultado
```

---

## 2. Función `es_primo`

```python
def es_primo(numero: int, primos_conocidos: list[int]) -> bool:
    if numero == 2:
        return True
    for primo in primos_conocidos:
        if numero % primo == 0:
            return False
    return True
```

### ¿Qué hace?
Comprueba si `numero` es primo usando una lista de primos ya encontrados (`primos_conocidos`).

### Conceptos clave

- **Anotaciones de tipo**:
  - `numero: int` → `numero` debe ser entero.
  - `primos_conocidos: list[int]` → lista de enteros.
  - `-> bool` → la función devuelve `True` o `False`.

- **`if` (condicional)**:
  - `if numero == 2:` evalúa un caso especial.
  - Si se cumple, devuelve `True`.

- **`for` (bucle)**:
  - `for primo in primos_conocidos:` recorre la lista.
  - Si `numero % primo == 0`, entonces tiene divisor y **no** es primo (`False`).

- **`return`**:
  - Termina la función devolviendo un valor.

---

## 3. Función `generar_primos`

```python
def generar_primos(valor_maximo: int) -> list[int]:

    primos = []
    candidatos = []

    # Generar lista de candidatos del 2 al valor máximo
    for i in range(2, valor_maximo + 1):
        candidatos.append(i)

    # Filtrar los primos usando el concepto de primalidad
    for candidato in candidatos:
        if es_primo(candidato, primos):
            primos.append(candidato)
    
    return primos
```

### ¿Qué hace?
Genera todos los números primos desde `2` hasta `valor_maximo`.

### Paso a paso

1. Crea dos listas vacías:
   - `primos`: guardará los primos finales.
   - `candidatos`: números a evaluar.

2. Llena `candidatos` con un `for` y `range(2, valor_maximo + 1)`.

3. Recorre cada `candidato`:
   - Usa `if es_primo(candidato, primos):`
   - Si es primo, lo añade con `primos.append(candidato)`.

4. Devuelve la lista `primos`.

---

## 4. Estructuras de control usadas

- **`if`**: toma decisiones.
- **`for`**: repite acciones sobre secuencias.
- **`return`**: entrega resultado y finaliza la función.

---

## 5. Ejemplo rápido

Si llamas:

```python
generar_primos(10)
```

el resultado será:

```python
[2, 3, 5, 7]
```

---

## 6. Idea importante para aprender

Este archivo muestra muy bien cómo:
- dividir un problema en funciones pequeñas,
- usar tipos para que el código sea más claro,
- combinar `if` y `for` para construir lógica paso a paso.
