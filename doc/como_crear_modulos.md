# Cómo crear un módulo en Python usando una carpeta y `__init__.py`

En Python, un **módulo** puede ser:

- Un archivo `.py` (por ejemplo, `utilidades.py`)
- O un **paquete**: una carpeta con varios módulos dentro

Cuando trabajas con una carpeta, normalmente la conviertes en paquete añadiendo un archivo `__init__.py`.

---

## 1) Estructura básica

Imagina esta estructura:

```text
mi_proyecto/
├── main.py
└── herramientas/
    ├── __init__.py
    └── calculos.py
```

- `herramientas/` es la carpeta del paquete
- `__init__.py` le dice a Python que esa carpeta debe tratarse como paquete
- `calculos.py` es un módulo dentro del paquete

---

## 2) Crear código dentro del paquete

### `herramientas/calculos.py`

```python
def sumar(a: int, b: int) -> int:
    return a + b
```

### `herramientas/__init__.py`

```python
from .calculos import sumar
```

Con esto, expones `sumar` desde el paquete `herramientas`.

---

## 3) Usarlo desde otro archivo

### `main.py`

```python
from herramientas import sumar

resultado = sumar(2, 3)
print(resultado)  # 5
```

---

## 4) ¿Para qué sirve `__init__.py`?

`__init__.py` se usa para:

1. Marcar la carpeta como paquete (compatibilidad y claridad)
2. Ejecutar inicialización del paquete (si hace falta)
3. Decidir qué funciones/clases se exportan de forma cómoda

---

## 5) Buenas prácticas

- Usa nombres de carpetas y archivos en minúsculas (`mi_paquete`, `utilidades.py`)
- Mantén `__init__.py` simple
- Organiza por responsabilidad (por ejemplo: `io.py`, `calculos.py`, `validaciones.py`)

---

## 6) Resumen

Para crear un módulo basado en carpeta:

1. Crea una carpeta (ej. `herramientas/`)
2. Añade `__init__.py`
3. Crea tus archivos `.py` dentro
4. Importa desde tu paquete en otros archivos

Así tendrás código mejor organizado y más fácil de mantener.
