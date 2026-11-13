# Proyecto Python con uv y VS Code

Este proyecto es una pequeña aplicación en Python cuyo punto de entrada es `main.py`. Está preparado para ejecutarse con `uv`, que se encarga de crear y gestionar el entorno virtual del proyecto.

## Requisitos

- Python 3.14 o superior
- VS Code
- `uv` instalado en tu sistema

## 1) Abrir el proyecto en VS Code

1. Abre la carpeta del proyecto en VS Code.
2. Abre una terminal integrada (`Terminal > New Terminal`).
3. En la terminal, desde la raíz del proyecto ejecuta:

```powershell
uv sync
```

Este comando crea el entorno virtual `.venv` y instala las dependencias definidas en `pyproject.toml`.

## 2) Seleccionar el intérprete de Python en VS Code

Para que VS Code use el entorno virtual del proyecto:

1. Pulsa `Ctrl+Shift+P`.
2. Escribe `Python: Select Interpreter`.
3. Selecciona la opción que apunte a `.venv` del proyecto.

Normalmente estará algo como:

```text
.venv\Scripts\python.exe
```

## 3) Ejecutar el proyecto

El archivo principal es `main.py` y es el punto de entrada del programa.

### Opción A: desde la terminal

```powershell
uv run python main.py
```

### Opción B: activar el entorno virtual y ejecutar directamente

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

### Opción C: desde VS Code

- Abre `main.py`
- Haz clic en el botón `Run Python File` o usa `F5` con la configuración de depuración de Python

## 4) Estructura básica

```text
bare_project/
├── main.py
├── pyproject.toml
├── uv.lock
├── .venv/
├── app/
│   ├── __init__.py
│   └── primos.py
└── README.md
```

## 5) Recomendación para el curso

Trabaja siempre desde la terminal de VS Code con `uv` para mantener un entorno limpio y reproducible:

```powershell
uv run python main.py
```

Esto asegura que el proyecto se ejecute con las dependencias correctas y que el entorno virtual quede gestionado por `uv`.

## Documentación adicional

- [Guía de números primos](./doc/primos.md)
- [Crear nuevos proyectos](./doc/crear_nuevos_proyectos.md)
- [Como crear módulos y paquetes](./doc/como_crear_modulos.md)