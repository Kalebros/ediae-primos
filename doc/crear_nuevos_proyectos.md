# Guía rápida para crear nuevos proyectos usando uv.

El gestor de paquetes `uv` tiene muchas opciones para crear proyectos desde cero, con una estructura propia. Sin embargo, estos proyectos pueden resultar confusos para empezar. Aquí proporcionamos una guía para crear nuevos projectos desde cero y poder gestionarlos con `uv` y VSCode.

## 1) Preparar el esqueleto inicial.

Desde un terminal Powershell, nos vamos a la carpeta donde tenemos guardados nuestros proyectos y llamaos a uv con la opción `--bare`:

```powershell
uv init nombre-de-proyecto --bare
```

Esto nos creará una carpeta `nombre-de-proyecto` con un archivo `pyproject.toml` básico y nada más. Podemos entrar en la carpeta recien creada y completar el proyecto.

## 2) Abrir proyecto con VSCode

Nuestro siguiente paso es abrir el proyecto utilizando VSCode. Para ello tenemos dos opciones:

### Opcion A: Abrir directamente desde VSCode

Abrimos el VSCode si no lo tenemos abierto previamente. Nos aseguramos de que no tenemos abierto ningún otro proyecto o carpeta. Si lo tenemos, lo cerramos con `CTRL + K F` o bien desde `File -> Close folder`.

Una vez comprobamos que no tenemos ninguna otra carpeta abierta, podemos abrir nuestro nuevo proyecto desde `File -> Open Folder`

### Opcion B: Abrir desde el terminal

Si estamos en la carpeta contenedora del proyecto, entramos dentro de la carpeta del proyecto; una vez estemos dentro de la carpeta de nuestro proyecto, lanzamos el VSCode desde el terminal indicando que queremos abrir la carpeta actual:

```powershell
-- SI NO ESTAMOS EN LA CARPETA DEL PROYECTO RECIEN CREADO, ENTRAMOS
cd nombre-de-proyecto
code .
```

Esto nos abrirá el VSCode con la carpeta del proyecto

## 3) Añadir archivo main.py y dependencias básicas.

Sólo tenemos el archivo `pyproject.toml`. Lo abrimos
y añadimos en la lista de dependencies los módulos de
**loguru** y **pytest**:

```
[project]
name = "nombre-de-proyecto"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "loguru",
    "pytest"
]
```

Guardamos el archivo y creamos un nuevo archivo `main.py` desde `File -> New file` o bien pulsando `Ctrl + N`

Añadimos el siguiente código básico y guardamos el archivo:

```python
from loguru import logger

logger.info('Hello world!')
```

## 4) Sincronizamos el entorno virtual con las dependencias.

Por último, sincronizamos el entorno virtual y las dependencias usando `uv` desde un terminal de Powershell abierto en la carpeta del proyecto

```powerhsell
uv sync
```

También podemos hacerlo desde un terminal de VSCode, el cual podemos abrir desde `Terminal -> New Terminal`
o pulsando `Ctrl + Shift + ñ`

## OPCIONAL: Archivo .gitignore y módulo para funciones y librerias.

### Archivo .gitignore

Podemos completar el proyecto si creamos un archivo `.gitignore`. Para ello podemos pulsar `Ctrl + N` para crear un nuevo archivo. Para encontrar su contenido, podemos acudir a [.gitignore de Python](https://github.com/github/gitignore/blob/main/Python.gitignore), donde tenemos un ejemplo funcional de archivo .gitignore. Podemos pulsar en el boton `RAW` que aparece en la interfaz para que nos muestre una versión apta para copiar en el navegador. Copiamos y pegamos el contenido en nuestro archivo local `.gitignore` y lo guardamos.


### Módulo para funciones y librerías

Para crear un módulo de para funciones y librerías, debemos crear una carpeta en el mismo nivel que nuestro archivo `main.py`. En esta carpeta, creamos un archivo `__init__.py` en el cual no añadimos contenido.

A la hora de modularizar el código, para tenerlo separado por librerías y funciones, consulta [como crear modulos](./como_crear_modulos.md)