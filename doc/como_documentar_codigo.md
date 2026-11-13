# Guía Completa: Cómo Documentar Código Python para Principiantes

Una guía paso a paso para aprender a documentar correctamente el código Python usando el estilo Google. La documentación es tan importante como el código mismo porque permite que otros programadores (¡y tu yo del futuro!) entiendan qué hace tu código y por qué lo hace de esa manera.

## 📚 Contenidos

- [¿Por qué documentar código?](#por-qué-documentar-código)
- [Docstrings de módulo](#docstrings-de-módulo)
- [Docstrings de función](#docstrings-de-función---estilo-google)
- [Docstrings de clase](#docstrings-de-clase---estilo-google)
- [Comentarios en línea](#comentarios-en-línea)
- [Buenas prácticas](#buenas-prácticas-de-documentación)
- [Ejemplo completo](#ejemplo-completo)
- [Resumen de estilos](#comparación-estilos-de-docstring)
- [Ejercicio práctico](#ejercicio-práctico)

---

## ¿Por qué documentar código?

Piensa en esto: **pasarás el 90% del tiempo LEYENDO código y el 10% escribiéndolo.**

La documentación clara significa:

✅ Tú mismo entiendes tu código después de 6 meses  
✅ Otros programadores saben cómo usar tu código  
✅ Es más fácil encontrar y arreglar errores  
✅ Se mantiene el proyecto de manera sostenible  
✅ Te vuelves más valioso como programador  

> **La documentación es un acto de amor hacia tu yo del futuro.**

---

## Docstrings de Módulo

Un **docstring de módulo** es un comentario especial al **INICIO** de un archivo `.py`

### Propósito

- Explicar qué hace el módulo
- Listar los conceptos principales
- Proporcionar información de contacto o licencia

### Sintaxis

```python
"""
Descripción breve de qué hace este módulo.

Descripción más detallada si es necesario. Puede ocupar varias líneas
para explicar los conceptos principales del módulo.

Contenidos:
    - Concepto 1
    - Concepto 2
    - Concepto 3

Autor: Tu nombre
Fecha: 2026-11-13
"""

# El resto del código va aquí
import sys
# ...
```

### Regla importante

> El docstring de módulo debe estar **ANTES** que cualquier otra cosa (excepto comments)

### Ejemplo real

```python
"""
Módulo para calcular números primos.

Este módulo proporciona funciones para identificar números primos
y generar listas de primos hasta un valor máximo.

Contenidos:
    - es_primo(): Verifica si un número es primo
    - generar_primos(): Genera lista de primos

Autor: Aprendiendo Python
Versión: 1.0
"""

from typing import List

def es_primo(numero: int) -> bool:
    # ...
```

---

## Docstrings de Función - Estilo Google

### ¿Qué NO hacer?

```python
def calcular_promedio(calificaciones):
    """Calcula el promedio de las calificaciones"""
    pass
```

**¿Qué le falta?**
- No indica qué tipo de datos entra
- No explica qué retorna
- No menciona casos especiales

### Anatomía correcta (Estilo Google)

```python
def calcular_promedio_correcto(calificaciones: list[float]) -> float:
    """
    Resumen breve en una línea.
    
    Descripción detallada de qué hace la función. Puedes usar
    varias líneas para explicar el comportamiento en detalle.
    
    Args:
        nombre_parametro: Descripción del parámetro, incluyendo
            qué tipo de dato es y qué valores espera.
        otro_parametro: Descripción adicional.
    
    Returns:
        tipo: Descripción de qué retorna la función.
    
    Raises:
        TipoError: Cuándo se lanza esta excepción.
        OtroError: Cuándo se lanza este otro error.
    
    Example:
        >>> calcular_promedio_correcto([80, 90, 100])
        90.0
    """
    pass
```

### Las 7 secciones

| Sección | Obligatoria | Descripción |
|---------|------------|-------------|
| **Resumen** | ✅ | Una línea que resume qué hace (imperativamente) |
| **Descripción** | ❌ | Explicación detallada (opcional pero recomendado) |
| **Args** | ✅ | Parámetros, tipos y descripciones |
| **Returns** | ✅ | Qué retorna y su tipo |
| **Raises** | ❌ | Excepciones que puede lanzar |
| **Example** | ❌ | Ejemplos de uso (recomendado para funciones complejas) |
| **Note** | ❌ | Notas especiales si es necesario |

### Ejemplos prácticos

#### Ejemplo 1: Función simple

```python
def validar_edad(edad: int) -> bool:
    """
    Verifica si la edad es válida (entre 0 y 150 años).
    
    Args:
        edad: La edad en años que se va a validar.
    
    Returns:
        True si la edad es válida, False en caso contrario.
    
    Example:
        >>> validar_edad(25)
        True
        >>> validar_edad(-5)
        False
    """
    return 0 <= edad <= 150
```

#### Ejemplo 2: Función con excepciones

```python
def dividir_numeros(dividendo: float, divisor: float) -> float:
    """
    Divide un número por otro.
    
    Args:
        dividendo: El número a ser dividido.
        divisor: El número por el cual se divide (no puede ser 0).
    
    Returns:
        float: El resultado de la división.
    
    Raises:
        ZeroDivisionError: Si divisor es 0.
        TypeError: Si los argumentos no son números.
    
    Example:
        >>> dividir_numeros(10, 2)
        5.0
        >>> dividir_numeros(15, 3)
        5.0
    """
    if divisor == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return dividendo / divisor
```

#### Ejemplo 3: Función con lista

```python
def calcular_promedio(calificaciones: list[float]) -> float:
    """
    Calcula el promedio aritmético de un conjunto de calificaciones.
    
    Args:
        calificaciones: Lista de números flotantes que representan las
            calificaciones. Cada calificación debe estar entre 0 y 100.
    
    Returns:
        float: El promedio de todas las calificaciones. Por ejemplo,
            si calificaciones = [80, 90, 100], retorna 90.0
    
    Raises:
        ValueError: Si la lista está vacía.
        TypeError: Si algún elemento no es un número.
    
    Example:
        >>> calcular_promedio([80, 90, 100])
        90.0
        >>> calcular_promedio([70, 70])
        70.0
    """
    if not calificaciones:
        raise ValueError("La lista de calificaciones no puede estar vacía")
    
    return sum(calificaciones) / len(calificaciones)
```

---

## Docstrings de Clase - Estilo Google

### Estructura básica

```python
class MiClase:
    """
    Resumen breve en una línea.
    
    Descripción detallada de qué representa esta clase,
    cuál es su propósito y cómo se usa.
    
    Attributes:
        atributo1: Descripción del atributo 1 (tipo).
        atributo2: Descripción del atributo 2 (tipo).
    
    Example:
        >>> obj = MiClase(arg1, arg2)
        >>> obj.metodo()
        resultado
    """
    pass
```

### Ejemplo 1: Clase simple

```python
class Persona:
    """
    Representa una persona con información básica.
    
    Esta clase almacena información sobre una persona como su nombre,
    edad y correo electrónico. Es un ejemplo educativo simple.
    
    Attributes:
        nombre: El nombre completo de la persona (str).
        edad: La edad en años de la persona (int).
        email: El correo electrónico de la persona (str).
    
    Example:
        >>> persona = Persona("Juan", 25, "juan@example.com")
        >>> print(persona.nombre)
        Juan
        >>> persona.saludar()
        Hola, me llamo Juan y tengo 25 años
    """
    
    def __init__(self, nombre: str, edad: int, email: str):
        """
        Inicializa una nueva instancia de Persona.
        
        Args:
            nombre: El nombre completo de la persona.
            edad: La edad en años (debe estar entre 0 y 150).
            email: El correo electrónico de contacto.
        
        Raises:
            ValueError: Si la edad no está en el rango válido.
        """
        if not validar_edad(edad):
            raise ValueError(f"La edad {edad} no es válida")
        
        self.nombre = nombre
        self.edad = edad
        self.email = email
    
    def saludar(self) -> str:
        """
        Retorna un saludo personalizado.
        
        Returns:
            str: Un mensaje de saludo con el nombre y edad de la persona.
        
        Example:
            >>> persona = Persona("Ana", 30, "ana@example.com")
            >>> persona.saludar()
            'Hola, me llamo Ana y tengo 30 años'
        """
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"
```

### Ejemplo 2: Clase con herencia

```python
class Estudiante(Persona):
    """
    Representa un estudiante que hereda de Persona.
    
    NOTA: Cuando una clase hereda de otra, también hereda sus docstrings.
    Documenta solo lo nuevo que agregues.
    
    Attributes:
        nombre: El nombre del estudiante (heredado de Persona).
        edad: La edad del estudiante (heredado de Persona).
        email: El email del estudiante (heredado de Persona).
        matricula: El número único de matrícula del estudiante (str).
        calificaciones: Lista de calificaciones numéricas (list[float]).
    
    Example:
        >>> est = Estudiante("Carlos", 20, "carlos@uni.edu", "2024001")
        >>> est.agregar_calificacion(95)
        >>> est.obtener_promedio()
        95.0
    """
    
    def __init__(
        self,
        nombre: str,
        edad: int,
        email: str,
        matricula: str
    ):
        """
        Inicializa un nuevo estudiante.
        
        Args:
            nombre: El nombre del estudiante.
            edad: La edad del estudiante.
            email: El email del estudiante.
            matricula: El número de matrícula (ej: "2024001").
        """
        super().__init__(nombre, edad, email)
        self.matricula = matricula
        self.calificaciones: list[float] = []
    
    def agregar_calificacion(self, calificacion: float) -> None:
        """
        Agrega una calificación al registro del estudiante.
        
        Args:
            calificacion: Un número entre 0 y 100 que representa la
                calificación.
        
        Raises:
            ValueError: Si la calificación está fuera del rango 0-100.
        """
        if not 0 <= calificacion <= 100:
            raise ValueError(
                f"La calificación {calificacion} debe estar entre 0 y 100"
            )
        self.calificaciones.append(calificacion)
    
    def obtener_promedio(self) -> float:
        """
        Calcula el promedio de todas las calificaciones del estudiante.
        
        Returns:
            float: El promedio de las calificaciones.
        
        Raises:
            ValueError: Si el estudiante no tiene calificaciones registradas.
        
        Example:
            >>> est = Estudiante("María", 19, "maria@uni.edu", "2024002")
            >>> est.agregar_calificacion(85)
            >>> est.agregar_calificacion(90)
            >>> est.obtener_promedio()
            87.5
        """
        if not self.calificaciones:
            raise ValueError("El estudiante no tiene calificaciones")
        
        return sum(self.calificaciones) / len(self.calificaciones)
```

---

## Comentarios en Línea

Los comentarios en línea son notas DENTRO del código que explican la lógica.

### ¿Cuándo usarlos?

✅ **SÍ usarlos cuando:**
- La lógica es compleja o no obvia
- Explicas por QUÉ haces algo (no QUÉ hace el código)
- Adviertes sobre trampas o casos especiales

❌ **NO usarlos cuando:**
- El código es obvio
- Solo repites lo que el código dice
- Usas nombres claros de variables

### Ejemplos correctos

```python
def procesar_datos(datos: list[int]) -> list[int]:
    """
    Procesa una lista de números aplicando varias transformaciones.
    
    Args:
        datos: Lista de números enteros para procesar.
    
    Returns:
        Lista de números procesados.
    """
    resultado = []
    
    # Itera sobre cada número en la lista de datos
    for numero in datos:
        # Salta números negativos o cero (no nos interesan)
        if numero <= 0:
            continue
        
        # Multiplica por 2 si el número es par (optimización de rendimiento)
        if numero % 2 == 0:
            numero = numero * 2
        # Suma 1 si el número es impar
        else:
            numero = numero + 1
        
        resultado.append(numero)
    
    return resultado
```

### ¿Qué NO hacer?

```python
# ❌ MAL: Comentario innecesario
def sumar(x, y):
    return x + y  # Retorna la suma de x y y

# ✅ BIEN: El código es autoexplicativo
def sumar(x, y):
    return x + y
```

---

## Buenas Prácticas de Documentación

### 1. Docstrings para TODO

```
✅ Cada módulo debe tener un docstring
✅ Cada función debe tener un docstring
✅ Cada clase debe tener un docstring
✅ Métodos públicos deben tener un docstring
❌ Métodos privados (comienzan con _) solo si son complejos
```

### 2. Sé específico

```
❌ MALO: "Esta función hace algo"
✅ BUENO: "Calcula el promedio de calificaciones entre 0 y 100"

❌ MALO: "Procesa datos"
✅ BUENO: "Filtra números pares de una lista y los multiplica por 2"
```

### 3. Usa ejemplos

```
Los ejemplos muestran exactamente cómo usar la función.
Especialmente importante para funciones complicadas.
```

### 4. Documenta excepciones

```
✅ Si tu función puede lanzar excepciones, documéntalas
✅ Explica cuándo y por qué se lanzan
✅ Ayuda al programador a saber qué esperar
```

### 5. Mantén actualizado

```
✅ Si cambias el código, actualiza la documentación
❌ La documentación obsoleta es peor que sin documentación
```

### 6. Usa palabras simples

```
✅ "retorna" en lugar de "devuelve el resultado de"
✅ "verifica" en lugar de "determina la veracidad de"
✅ "lista" en lugar de "colección de elementos de tipo iterable"
```

### 7. Tipo de datos

```
✅ Siempre indica el tipo de dato en Args y Returns
✅ En Python 3.5+, usa type hints: list[float], dict[str, int]
✅ Sé específico: list[str] no solo list
```

### 8. Usa Markdown simple

```
✅ Puedes usar **negritas** para énfasis
✅ Puedes usar `código` entre backticks
✅ Puedes usar listas con - o *
✅ Mantén el formato simple y legible
```

---

## Ejemplo Completo

Aquí te mostramos una clase completamente documentada:

```python
class Calculadora:
    """
    Una calculadora simple para operaciones aritméticas básicas.
    
    Esta clase proporciona métodos para realizar operaciones matemáticas
    simples como suma, resta, multiplicación y división. Es un ejemplo
    educativo de cómo documentar una clase completa.
    
    Attributes:
        historial: Lista que mantiene un registro de todas las
            operaciones realizadas.
    
    Example:
        >>> calc = Calculadora()
        >>> calc.sumar(5, 3)
        8
        >>> calc.multiplicar(4, 7)
        28
        >>> len(calc.historial)
        2
    """
    
    def __init__(self):
        """Inicializa una nueva calculadora con un historial vacío."""
        self.historial: list[str] = []
    
    def sumar(self, a: float, b: float) -> float:
        """
        Suma dos números.
        
        Args:
            a: El primer número.
            b: El segundo número.
        
        Returns:
            La suma de a + b.
        
        Example:
            >>> calc = Calculadora()
            >>> calc.sumar(10, 5)
            15
        """
        resultado = a + b
        self._registrar_operacion(f"{a} + {b} = {resultado}")
        return resultado
    
    def dividir(self, a: float, b: float) -> float:
        """
        Divide dos números.
        
        Args:
            a: El dividendo (número a dividir).
            b: El divisor (número por el cual dividir).
        
        Returns:
            float: El cociente a / b.
        
        Raises:
            ZeroDivisionError: Si b es 0.
        
        Example:
            >>> calc = Calculadora()
            >>> calc.dividir(15, 3)
            5.0
        """
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        
        resultado = a / b
        self._registrar_operacion(f"{a} / {b} = {resultado}")
        return resultado
    
    def _registrar_operacion(self, operacion: str) -> None:
        """
        Registra una operación en el historial (método privado).
        
        NOTA: El prefijo _ indica que es un método privado.
        
        Args:
            operacion: Descripción de la operación a registrar.
        """
        self.historial.append(operacion)
```

---

## Comparación: Estilos de Docstring

Existen varios estilos en Python. Te mostramos los principales:

### Estilo Google ✅ (Recomendado)

```python
def mi_funcion(x: int, y: int) -> int:
    """Resumen de una línea.
    
    Descripción más detallada.
    
    Args:
        x: Descripción de x.
        y: Descripción de y.
    
    Returns:
        Descripción del retorno.
    """
    pass
```

**Ventajas:** Muy legible, moderno, fácil de mantener

### Estilo NumPy

```python
def mi_funcion(x: int, y: int) -> int:
    """Resumen de una línea.
    
    Parameters
    ----------
    x : int
        Descripción de x.
    y : int
        Descripción de y.
    
    Returns
    -------
    int
        Descripción del retorno.
    """
    pass
```

**Ventajas:** Bueno para proyectos científicos

### Estilo reStructuredText (RST)

```python
def mi_funcion(x: int, y: int) -> int:
    """Resumen de una línea.
    
    :param x: Descripción de x.
    :param y: Descripción de y.
    :return: Descripción del retorno.
    """
    pass
```

**Ventajas:** Compatible con Sphinx

> **Conclusión:** Usamos **Google** porque es más legible y moderno. ✅

---

## Ejercicio Práctico

Intenta documentar estas funciones tú mismo usando el estilo Google:

### Función 1

```python
def calcular_area_rectangulo(largo: float, ancho: float) -> float:
    """[AGREGA EL DOCSTRING AQUÍ]"""
    return largo * ancho
```

### Función 2

```python
def es_numero_par(numero: int) -> bool:
    """[AGREGA EL DOCSTRING AQUÍ]"""
    return numero % 2 == 0
```

### Función 3 (más complicada)

```python
def filtrar_numeros_pares(numeros: list[int]) -> list[int]:
    """[AGREGA EL DOCSTRING AQUÍ]"""
    return [n for n in numeros if n % 2 == 0]
```

### Soluciones

**Solución 1:**

```python
def calcular_area_rectangulo(largo: float, ancho: float) -> float:
    """
    Calcula el área de un rectángulo.
    
    Args:
        largo: La longitud del rectángulo en unidades.
        ancho: El ancho del rectángulo en unidades.
    
    Returns:
        float: El área del rectángulo (largo × ancho).
    
    Example:
        >>> calcular_area_rectangulo(5, 3)
        15
    """
    return largo * ancho
```

**Solución 2:**

```python
def es_numero_par(numero: int) -> bool:
    """
    Verifica si un número es par.
    
    Args:
        numero: El número a verificar.
    
    Returns:
        True si el número es par, False si es impar.
    
    Example:
        >>> es_numero_par(4)
        True
        >>> es_numero_par(7)
        False
    """
    return numero % 2 == 0
```

**Solución 3:**

```python
def filtrar_numeros_pares(numeros: list[int]) -> list[int]:
    """
    Filtra y retorna solo los números pares de una lista.
    
    Args:
        numeros: Lista de números enteros a filtrar.
    
    Returns:
        list[int]: Una nueva lista con solo los números pares.
    
    Raises:
        TypeError: Si algún elemento no es un número entero.
    
    Example:
        >>> filtrar_numeros_pares([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> filtrar_numeros_pares([1, 3, 5])
        []
    """
    return [n for n in numeros if n % 2 == 0]
```

---

## Resumen y Conclusión

### Checklist de documentación

- ✅ ¿Tiene docstring de módulo?
- ✅ ¿Tiene docstring cada función?
- ✅ ¿Tiene docstring cada clase?
- ✅ ¿Los Args incluyen tipos?
- ✅ ¿Los Returns incluyen tipos?
- ✅ ¿Está documentado en estilo Google?
- ✅ ¿Hay ejemplos para funciones complejas?

### Recuerda

1. 📝 **Documenta MIENTRAS escribes el código**, no después
2. 🎯 **Sé claro y conciso** - evita jerga innecesaria
3. 📚 **Incluye ejemplos** para funciones complicadas
4. 🔄 **Mantén actualizado** - la documentación debe cambiar con el código
5. 📖 **Lee documentación de otros** como inspiración

### Próximos pasos

- 🎯 Practica documentando tus propios proyectos
- 📚 Lee ejemplos de código bien documentado en GitHub
- 🛠️ Usa herramientas como **Sphinx** para generar documentación automática
- 🔍 Revisa la documentación oficial: [PEP 257](https://www.python.org/dev/peps/pep-0257/)

---

## Conclusión Final

La documentación es una habilidad que mejora con la práctica. 

> **¡La documentación es un regalo para otros programadores y para ti mismo!**

¡Felicidades por aprender esto! 🎉

