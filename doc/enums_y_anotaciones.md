# Enums y anotaciones en Python

Cuando empiezas a programar, muchas veces trabajas con valores como cadenas o números que representan estados o categorías. Por ejemplo:

```python
estado = "activo"
```

Esto parece sencillo, pero al cabo del tiempo puede dar problemas si alguien escribe algo distinto por error:

```python
estado = "activa"
```

Ese valor puede romper la lógica del programa o provocar errores difíciles de detectar.

Para evitar esto, Python ofrece dos herramientas muy útiles:

- `Enum`: para representar un conjunto finito de valores posibles.
- Anotaciones (`typing`): para documentar y verificar el tipo de datos esperados.

## 1. ¿Qué es un enum?

Un `Enum` es una colección de nombres simbólicos asociados a valores constantes.

Se usa cuando una variable solo puede tomar un número limitado de opciones válidas.

```python
from enum import Enum

class EstadoCivil(Enum):
    SOLTERO = "soltero"
    CASADO = "casado"
    DIVORCIADO = "divorciado"
    VIUDO = "viudo"
```

Ahora, en lugar de usar cadenas sueltas, trabajamos con valores específicos del enum:

```python
estado = EstadoCivil.SOLTERO
print(estado)  # EstadoCivil.SOLTERO
print(estado.value)  # soltero
```

## 2. ¿Por qué usar enums?

Los enums ayudan a reducir errores de entrada de datos.

### Ejemplo sin enum

```python
color = "rojo"

if color == "rojo":
    print("Encender luz roja")
elif color == "verde":
    print("Encender luz verde")
else:
    print("Color no válido")
```

Aquí es fácil escribir una cadena mal:

```python
color = "rojo "
```

o:

```python
color = "ROJO"
```

Y el programa puede fallar.

### Ejemplo con enum

```python
from enum import Enum

class Color(Enum):
    ROJO = "rojo"
    VERDE = "verde"
    AZUL = "azul"

color = Color.ROJO

if color == Color.ROJO:
    print("Encender luz roja")
elif color == Color.VERDE:
    print("Encender luz verde")
else:
    print("Color no válido")
```

Ahora el conjunto de valores posibles está definido claramente. No se aceptan otros valores por accidente.

## 3. Casos en los que los enums son útiles

Los enums son especialmente útiles en situaciones como estas:

### a) Estados de un proceso

```python
from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"
```

Esto evita que alguien escriba:

```python
estado = "entregao"
```

### b) Días de la semana

```python
class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
```

### c) Roles de usuario

```python
class RolUsuario(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VISITANTE = "visitante"
```

### d) Tipos de documento

```python
class TipoDocumento(Enum):
    DNI = "dni"
    NIE = "nie"
    PASAPORTE = "pasaporte"
```

## 4. Enum con valores numéricos

También puedes asociar valores numéricos:

```python
from enum import Enum

class Nivel(Enum):
    BAJO = 1
    MEDIO = 2
    ALTO = 3
```

Esto puede ser útil cuando el sistema ya usa números para representar estados.

## 5. Comparación y validación

Un enum permite comparar valores de forma más segura:

```python
if estado == EstadoCivil.CASADO:
    print("Está casado")
```

Esto es más claro y menos propenso a errores que comparar con cadenas sueltas.

## 6. ¿Qué son las anotaciones en Python?

Las anotaciones de tipo permiten indicar qué tipo de dato espera una variable, un parámetro o el valor de retorno de una función.

```python
nombre: str = "Ana"
edad: int = 25
activo: bool = True
```

### Ejemplo con función

```python
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"
```

Aquí decimos:

- `nombre` debe ser un `str`
- la función devuelve un `str`

## 7. ¿Para qué sirven las anotaciones?

Las anotaciones tienen varios usos muy importantes:

### a) Ayuda a entender el código

Cuando lees una función, puedes saber rápidamente qué datos espera y qué devuelve.

```python
def calcular_total(precio: float, cantidad: int) -> float:
    return precio * cantidad
```

Esto hace que el código sea mucho más legible.

### b) Mejoran el análisis estático

Herramientas como `mypy` o el análisis de Pylance pueden detectar errores antes de ejecutar el programa.

```python
def sumar(a: int, b: int) -> int:
    return a + b

print(sumar(3, 4))      # correcto
print(sumar("3", 4))   # el analizador avisará del error
```

Aunque Python sigue siendo un lenguaje dinámico, las anotaciones ayudan a detectar inconsistencias antes.

### c) Mejoran el mantenimiento a largo plazo

Cuando un proyecto crece, el código se vuelve más complejo. Las anotaciones ayudan a:

- entender qué esperan las funciones,
- reducir errores al cambiar código,
- facilitar la colaboración entre programadores,
- soportar refactorizaciones más seguras.

## 8. Tipos básicos en Python

Algunas anotaciones comunes son:

```python
nombre: str
edad: int
altura: float
activo: bool
notas: list[int]
```

### Lista de enteros

```python
notas: list[int] = [10, 8, 9]
```

### Diccionario

```python
datos: dict[str, int] = {"a": 1, "b": 2}
```

### Tupla

```python
coordenadas: tuple[int, int] = (3, 5)
```

### Una lista de cadenas opcional

```python
nombres: list[str] | None = None
```

En Python moderno se puede usar `|` para indicar unión de tipos.

## 9. Parámetros y valores de retorno

```python
def obtener_nombre(usuario_id: int) -> str:
    return f"usuario-{usuario_id}"
```

Esto comunica claramente:

- `usuario_id` debe ser un entero,
- la función devuelve una cadena.

## 10. Anotaciones con clases y enums

Las anotaciones también se usan con clases y enums.

```python
from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"

class Pedido:
    estado: EstadoPedido

    def __init__(self, estado: EstadoPedido) -> None:
        self.estado = estado
```

Esto deja claro que `estado` solo puede tomar valores de `EstadoPedido`.

## 11. Enum + anotaciones: una combinación muy útil

Cuando se combinan, las dos herramientas mejoran mucho la calidad del código.

```python
from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"

class Pedido:
    def __init__(self, estado: EstadoPedido) -> None:
        self.estado = estado

ped = Pedido(EstadoPedido.ENVIADO)
```

La anotación hace que el lector entienda qué tipo de dato es esperado, y el enum restringe esos valores para que no haya errores de entrada.

## 12. Caso práctico: formularios de usuario

Imagina un sistema con una variable que representa el rol del usuario:

```python
rol = "admin"
```

Si otra parte del programa escribe:

```python
rol = "admn"
```

Eso podría causar un fallo. Con enum:

```python
from enum import Enum

class RolUsuario(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    INVITADO = "invitado"
```

Y con anotaciones:

```python
def crear_usuario(rol: RolUsuario) -> None:
    print(f"Creando usuario con rol: {rol.value}")
```

Así se evita mucha ambigüedad y se reduce el riesgo de errores.

## 13. ¿Cuándo conviene usar enum y cuándo no?

### Usa `Enum` cuando:

- hay un conjunto fijo de opciones,
- quieres evitar entradas inválidas,
- los valores representan estados o categorías,
- quieres que el código sea más expresivo y legible,
- necesitas un valor constante y bien definido.

### No lo uses cuando:

- hay muchos valores posibles y cambian con frecuencia,
- necesitas almacenar datos dinámicos como nombres, textos o listas,
- no hay una categoría clara ni un conjunto limitado.

### Usa anotaciones cuando:

- quieres documentar funciones y variables,
- quieres mejor mantenimiento del código,
- trabajas en proyectos grandes,
- quieres usar herramientas de análisis estático.

## 14. Ventajas reales de los enums

Los enums ayudan a:

- reducir errores de entrada,
- evitar cadenas mágicas,
- hacer el código más legible,
- documentar mejor los estados del sistema,
- favorecer la consistencia en proyectos medianos y grandes.

Por ejemplo, en lugar de tener muchas cadenas dispersas por el programa:

```python
if estado == "pendiente":
    ...
if estado == "enviado":
    ...
```

Puedes centralizar todo en un enum:

```python
if estado == EstadoPedido.PENDIENTE:
    ...
if estado == EstadoPedido.ENVIADO:
    ...
```

Esto hace el código más claro y seguro.

## 15. Ventajas reales de las anotaciones

Las anotaciones ayudan a:

- que el código se entienda mejor,
- detectar errores antes de ejecutar,
- facilitar la revisión de código,
- mantener proyectos a largo plazo,
- reducir el trabajo de depuración.

## 16. Ejemplo completo

```python
from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"


def actualizar_pedido(estado: EstadoPedido) -> None:
    if estado == EstadoPedido.PENDIENTE:
        print("El pedido está pendiente")
    elif estado == EstadoPedido.ENVIADO:
        print("El pedido ya fue enviado")
    elif estado == EstadoPedido.ENTREGADO:
        print("El pedido ha sido entregado")


actualizar_pedido(EstadoPedido.ENVIADO)
```

Aquí vemos cómo las anotaciones describen el tipo esperado y el enum restringe los valores validos.

## 17. Resumen

### Enums

Los enums son útiles para representar valores limitados y bien definidos.

- Evitan errores por entradas erróneas.
- Mejoran la claridad del código.
- Son ideales para estados, roles y categorías.

### Anotaciones

Las anotaciones describen el tipo de datos esperados.

- Ayudan a entender el código.
- Mejoran el análisis estático.
- Facilitan mantenimiento y colaboración.
- Reducen errores en proyectos más grandes.

## 18. Consejo final

Si estás aprendiendo a programar, intenta pensar en dos cosas:

1. ¿Los valores de esta variable tienen un conjunto limitado y definido?
2. ¿Necesito dejar claro qué tipo de dato recibe y devuelve cada función?

Si la respuesta es sí, probablemente conviene usar `Enum` y anotaciones.

Eso no solo hace el código más ordenado, sino que también mejora mucho su calidad a largo plazo.
