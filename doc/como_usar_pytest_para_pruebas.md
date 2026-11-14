# Guía de Pytest para Principiantes

Una guía paso a paso para aprender a hacer pruebas unitarias en Python usando `pytest` y `uv`.

---

## 📚 Índice

1. [¿Qué son las pruebas unitarias?](#qué-son-las-pruebas-unitarias)
2. [¿Qué es pytest?](#qué-es-pytest)
3. [¿Qué es uv?](#qué-es-uv)
4. [Instalación y configuración](#instalación-y-configuración)
5. [Nuestro ejemplo: Números primos](#nuestro-ejemplo-números-primos)
6. [Anatomía de una prueba](#anatomía-de-una-prueba)
7. [Ejecutando pruebas](#ejecutando-pruebas)
8. [Casos de prueba útiles](#casos-de-prueba-útiles)
9. [Consejos finales](#consejos-finales)

---

## ¿Qué son las pruebas unitarias?

Las **pruebas unitarias** son pequeños programas que verifican que nuestro código funciona correctamente.

### Analogía con la vida real

Imagina que eres un fabricante de piezas LEGO:
- **Tu código** = fabricar piezas LEGO
- **Prueba unitaria** = verificar que cada pieza sea del tamaño correcto, color correcto y se encaje bien

Si una pieza falla, lo sabes inmediatamente, en lugar de descubrirlo cuando alguien intenta construir un castillo completo.

### ¿Por qué son importantes?

✅ Encuentras errores rápidamente  
✅ Ganas confianza en tu código  
✅ Facilita cambios futuros sin miedo a romper algo  
✅ Documentan cómo debería usarse el código  

---

## ¿Qué es pytest?

**pytest** es una herramienta que hace que escribir y ejecutar pruebas sea muy fácil.

### Ventajas de pytest

- ✨ **Sintaxis simple**: Solo usas `assert` (afirmaciones)
- 🚀 **Rápido**: Descubre y ejecuta pruebas automáticamente
- 📊 **Informativo**: Te muestra exactamente qué falló y por qué
- 🎯 **Flexible**: Puedes ejecutar pruebas individuales o todas juntas

---

## ¿Qué es uv?

**uv** es un gestor de proyectos Python muy rápido y moderno que reemplaza herramientas antiguas como `pip` y `virtualenv`.

### Características clave de uv

- ⚡ **Muy rápido**: 10-100 veces más rápido que pip
- 📦 **Gestión de dependencias**: Controla qué librerías necesita tu proyecto
- 🔐 **Reproducible**: Los proyectos funcionan igual en cualquier computadora
- 🛠️ **Todo en uno**: Instala, ejecuta scripts y gestiona entornos

---

## Instalación y configuración

### Paso 1: Verificar que uv está instalado

```bash
uv --version
```

Si ves un número de versión (ejemplo: `uv 0.4.0`), ¡está listo!

### Paso 2: Crear un proyecto con uv

```bash
uv init mi-proyecto
cd mi-proyecto
```

### Paso 3: Agregar pytest como dependencia

En tu archivo `pyproject.toml`, asegúrate de que tengas:

```toml
[project]
name = "mi-proyecto"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "pytest",
]
```

### Paso 4: Instalar dependencias

```bash
uv sync
```

¡Listo! Ahora tienes todo lo necesario.

---

## Nuestro ejemplo: Números primos

### El código que queremos probar

Tenemos un módulo `app/primos.py` que contiene dos funciones:

```python
def es_primo(numero: int, primos_conocidos: list[int]) -> bool:
    """
    Verifica si un número es primo.
    
    Argumentos:
        numero: El número a verificar
        primos_conocidos: Lista de números primos ya conocidos
    
    Retorna:
        True si el número es primo, False en caso contrario
    """
    if numero == 2:
        return True
    for primo in primos_conocidos:
        if numero % primo == 0:
            return False
    return True


def generar_primos(valor_maximo: int) -> list[int]:
    """
    Genera todos los números primos hasta un valor máximo.
    
    Argumentos:
        valor_maximo: El número más alto a considerar
    
    Retorna:
        Una lista de todos los números primos encontrados
    """
    primos = []
    candidatos = []

    # Generar lista de candidatos del 2 al valor máximo
    for i in range(2, valor_maximo + 1):
        candidatos.append(i)

    # Filtrar los primos
    for candidato in candidatos:
        if es_primo(candidato, primos):
            primos.append(candidato)
    
    return primos
```

**¿Qué hacen estas funciones?**

- `es_primo()`: Pregunta "¿es este número primo?" y responde Sí o No
- `generar_primos()`: Crea una lista de todos los números primos hasta cierto número

---

## Anatomía de una prueba

### Estructura básica

```python
def test_nombre_descriptivo():
    """Descripción de qué estamos probando."""
    # Paso 1: Preparar los datos (opcional)
    numero = 5
    
    # Paso 2: Ejecutar el código
    resultado = es_primo(numero, [2, 3])
    
    # Paso 3: Verificar que el resultado es correcto
    assert resultado is True
```

### Las tres partes de una prueba

| Parte | Qué hace | Ejemplo |
|-------|----------|---------|
| **Preparar** | Crear datos para probar | `numero = 5` |
| **Ejecutar** | Llamar la función | `resultado = es_primo(numero, [2, 3])` |
| **Verificar** | Comprobar que funciona | `assert resultado is True` |

### El comando `assert`

`assert` significa "afirmo que esto es verdad". Si no es verdad, pytest nos lo dice.

```python
# Ejemplos de asserts

assert 2 + 2 == 4          # ✅ Verdadero
assert 5 > 3               # ✅ Verdadero
assert resultado == [2, 3] # ✅ Verdadero si resultado es [2, 3]
assert lista != []         # ✅ Verdadero si lista no está vacía

# Si escribimos algo falso, pytest lo marca como error:
assert 2 + 2 == 5          # ❌ Falso - ¡error!
assert resultado == [1, 2] # ❌ Falso - ¡error!
```

---

## Ejecutando pruebas

### Estructura del proyecto

```
mi-proyecto/
├── app/
│   ├── __init__.py
│   └── primos.py           ← El código que probamos
├── tests/
│   ├── __init__.py
│   └── test_primos.py      ← Nuestras pruebas
├── pyproject.toml
└── pytest.ini              ← Configuración de pytest
```

### Ejecutar todas las pruebas

```bash
pytest
```

**Resultado esperado:**
```
============================= 12 passed in 0.03s ==============================
```

### Ejecutar pruebas con más información (verbose)

```bash
pytest -v
```

Esto te muestra el nombre de cada prueba:

```
tests/test_primos.py::TestEsPrimo::test_dos_es_primo PASSED
tests/test_primos.py::TestEsPrimo::test_numero_no_primo_con_divisor PASSED
tests/test_primos.py::TestEsPrimo::test_numero_primo_sin_divisores PASSED
...
```

### Ejecutar solo un archivo de pruebas

```bash
pytest tests/test_primos.py -v
```

### Ejecutar solo una clase de pruebas

```bash
pytest tests/test_primos.py::TestEsPrimo -v
```

### Ejecutar solo una prueba específica

```bash
pytest tests/test_primos.py::TestEsPrimo::test_dos_es_primo -v
```

### Ver qué pasa cuando una prueba falla

```bash
pytest -v --tb=short
```

El `--tb=short` te muestra un resumen conciso del error.

---

## Casos de prueba útiles

### 1. Pruebas de casos normales

Pruebas que verifican que el código funciona como se espera en situaciones típicas.

```python
def test_generar_primos_hasta_10(self):
    """Los primos hasta 10 son: 2, 3, 5, 7."""
    resultado = generar_primos(10)
    esperado = [2, 3, 5, 7]
    assert resultado == esperado
```

✅ **¿Qué probamos?** Que cuando pedimos primos hasta 10, obtenemos la lista correcta

### 2. Pruebas de casos límite

Pruebas que verifican situaciones extremas o especiales.

```python
def test_generar_primos_hasta_1_lista_vacia(self):
    """No hay primos entre 2 y 1."""
    resultado = generar_primos(1)
    assert resultado == []

def test_dos_es_primo(self):
    """El número 2 debe ser identificado como primo."""
    assert es_primo(2, []) is True
```

✅ **¿Qué probamos?** Que el código funciona correctamente en los "bordes" (números muy pequeños, listas vacías, etc.)

### 3. Pruebas de propiedades

Pruebas que verifican características generales del resultado.

```python
def test_generar_primos_100(self):
    """Verificar que se generan 25 primos hasta 100."""
    resultado = generar_primos(100)
    assert len(resultado) == 25
    assert resultado[0] == 2
    assert resultado[-1] == 97
```

✅ **¿Qué probamos?** Que el resultado tiene las características esperadas (número correcto de primos, primer elemento, último elemento)

### 4. Pruebas de tipo de dato

Pruebas que verifican que el resultado es del tipo correcto.

```python
def test_generar_primos_retorna_lista(self):
    """La función debe retornar una lista."""
    resultado = generar_primos(10)
    assert isinstance(resultado, list)
```

✅ **¿Qué probamos?** Que `generar_primos` siempre retorna una lista, no otra cosa

### 5. Pruebas lógicas

Pruebas que verifican la lógica interna del código.

```python
def test_todos_los_resultados_son_primos(self):
    """Todos los números retornados deben ser primos."""
    resultado = generar_primos(50)
    for primo in resultado[1:]:
        assert primo % 2 != 0  # Ninguno es divisible por 2 (excepto 2)
```

✅ **¿Qué probamos?** Que todos los números en la lista cumplan la propiedad de ser primos

---

## Estructura de pruebas con clases

### Por qué usar clases

Cuando tenemos muchas pruebas, agruparlas en clases las hace más organizadas.

```python
class TestEsPrimo:
    """Pruebas para la función es_primo."""
    
    def test_dos_es_primo(self):
        assert es_primo(2, []) is True
    
    def test_numero_no_primo_con_divisor(self):
        assert es_primo(4, [2]) is False


class TestGenerarPrimos:
    """Pruebas para la función generar_primos."""
    
    def test_generar_primos_hasta_10(self):
        resultado = generar_primos(10)
        assert resultado == [2, 3, 5, 7]
    
    def test_generar_primos_hasta_20(self):
        resultado = generar_primos(20)
        assert resultado == [2, 3, 5, 7, 11, 13, 17, 19]
```

### Ventajas

- 📁 **Organización**: Todas las pruebas relacionadas juntas
- 📖 **Claridad**: Es fácil ver qué se prueba
- 🔍 **Ejecución selectiva**: Puedes ejecutar solo las pruebas de una función

---

## Consejos finales

### ✅ Buenas prácticas

1. **Nombres descriptivos**: 
   - ❌ `def test_1():`
   - ✅ `def test_generar_primos_hasta_10():`

2. **Una cosa por prueba**: Cada prueba debe verificar una sola cosa
   - ❌ Probar si genera primos, verifica la cantidad Y verifica el primer elemento
   - ✅ Una prueba por cada aspecto

3. **Documentar con docstrings**:
   ```python
   def test_dos_es_primo(self):
       """El número 2 debe ser identificado como primo."""
       assert es_primo(2, []) is True
   ```

4. **Usar assert con mensajes (opcional)**:
   ```python
   assert resultado == [2, 3, 5], f"Se esperaba [2, 3, 5] pero se obtuvo {resultado}"
   ```

5. **Prueba los casos normales Y los casos límite**:
   - Casos normales: Número regular en el medio
   - Casos límite: Número muy pequeño, muy grande, vacío, etc.

### 📊 Cuántas pruebas escribir

- **Mínimo**: Una prueba por función
- **Recomendado**: 3-5 pruebas por función (casos normales + límite)
- **Ideal**: Cubrir el 70-80% del código

### 🐛 Si una prueba falla

1. Lee el mensaje de error de pytest
2. Verifica que tu prueba es correcta (el error podría estar en la prueba, no en el código)
3. Prueba el código manualmente en Python
4. Ajusta o el código o la prueba

---

## Ejemplo práctico paso a paso

### Paso 1: Escribe la función

En `app/primos.py`:
```python
def es_primo(numero: int, primos_conocidos: list[int]) -> bool:
    if numero == 2:
        return True
    for primo in primos_conocidos:
        if numero % primo == 0:
            return False
    return True
```

### Paso 2: Piensa en casos para probar

- ¿Qué pasa con el número 2?
- ¿Qué pasa con un número divisible por un primo?
- ¿Qué pasa con un número que no es divisible?

### Paso 3: Escribe pruebas

En `tests/test_primos.py`:
```python
class TestEsPrimo:
    def test_dos_es_primo(self):
        assert es_primo(2, []) is True
    
    def test_numero_no_primo_con_divisor(self):
        assert es_primo(4, [2]) is False
    
    def test_numero_primo_sin_divisores(self):
        assert es_primo(3, [2]) is True
```

### Paso 4: Ejecuta las pruebas

```bash
pytest tests/test_primos.py -v
```

### Paso 5: Ajusta si es necesario

Si una prueba falla, revisa si:
- El código tiene un bug
- La prueba está mal escrita
- Tus suposiciones sobre el comportamiento fueron incorrectas

---

## Resumen

| Concepto | Definición |
|----------|-----------|
| **Prueba unitaria** | Pequeño programa que verifica que una función funciona correctamente |
| **pytest** | Herramienta para escribir y ejecutar pruebas |
| **uv** | Gestor de proyectos Python moderno y rápido |
| **assert** | Comando que verifica que algo es verdadero |
| **Caso límite** | Situación extrema o especial (número muy pequeño, lista vacía, etc.) |
| **Clase de prueba** | Grupo de pruebas relacionadas |

---

## Próximos pasos

Ahora que conoces los conceptos básicos:

1. 🎯 **Practica**: Escribe más pruebas para otras funciones
2. 📚 **Lee la documentación oficial**: [pytest.org](https://pytest.org)
3. 🧪 **Experimenta**: Prueba diferentes tipos de asserts
4. 🔄 **Itera**: Escribe código → Pruébalo → Ajusta

¡La práctica es la clave para mejorar! 🚀
