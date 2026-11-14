# Trabajo con ficheros y carpetas en Python

Cuando programas, casi siempre necesitas guardar información o leerla desde el disco. Por ejemplo:

- guardar una lista de contactos,
- leer un archivo de texto con instrucciones,
- trabajar con imágenes o datos binarios,
- guardar configuración en JSON,
- crear carpetas para organizar archivos.

Python nos ofrece herramientas muy útiles para trabajar con archivos y directorios.

## 1. ¿Qué es un fichero?

Un fichero es un archivo que se guarda en el sistema operativo. Puede contener:

- texto (por ejemplo, `.txt`, `.csv`, `.md`),
- datos binarios (por ejemplo, imágenes, archivos ejecutables, archivos comprimidos),
- información estructurada como JSON.

## 2. ¿Qué es una carpeta?

Una carpeta (o directorio) sirve para organizar archivos. Puede contener otros archivos o subcarpetas.

## 3. Módulo `os`

El módulo `os` permite interactuar con el sistema operativo, por ejemplo:

- listar archivos de una carpeta,
- crear carpetas,
- comprobar si un archivo existe,
- cambiar de directorio.

### Importar el módulo

```python
import os
```

### 3.1 `os.getcwd()`

Devuelve el directorio actual de trabajo.

```python
print(os.getcwd())
```

### 3.2 `os.listdir()`

Lista los archivos y carpetas dentro de un directorio.

```python
contenido = os.listdir(".")
print(contenido)
```

Esto devuelve una lista con nombres de archivos y carpetas.

### 3.3 `os.mkdir()`

Crea una carpeta nueva.

```python
os.mkdir("mi_carpeta")
```

### 3.4 `os.makedirs()`

Crea carpetas anidadas.

```python
os.makedirs("datos/usuarios/2025")
```

### 3.5 `os.path.exists()`

Comprueba si una ruta existe.

```python
print(os.path.exists("mi_carpeta"))
```

### 3.6 `os.path.join()`

Une partes de una ruta de forma segura.

```python
ruta = os.path.join("carpeta", "archivo.txt")
print(ruta)
```

### 3.7 `os.path.isfile()`

Comprueba si una ruta es un archivo.

```python
print(os.path.isfile("archivo.txt"))
```

### 3.8 `os.path.isdir()`

Comprueba si una ruta es una carpeta.

```python
print(os.path.isdir("mi_carpeta"))
```

### 3.9 `os.remove()`

Elimina un archivo.

```python
os.remove("archivo.txt")
```

### 3.10 `os.rmdir()`

Elimina una carpeta vacía.

```python
os.rmdir("mi_carpeta")
```

### 3.11 `os.rename()`

Renombra o mueve un archivo.

```python
os.rename("viejo.txt", "nuevo.txt")
```

## 4. Módulo `pathlib`

`pathlib` es una alternativa moderna y más clara para trabajar con rutas y directorios.

### Importar `Path`

```python
from pathlib import Path
```

### 4.1 Crear una ruta

```python
ruta = Path("mi_carpeta")
print(ruta)
```

### 4.2 Crear una carpeta

```python
ruta = Path("mi_carpeta")
ruta.mkdir(exist_ok=True)
```

`exist_ok=True` evita un error si la carpeta ya existe.

### 4.3 Listar contenido

```python
for elemento in Path(".").iterdir():
    print(elemento)
```

### 4.4 Construir rutas

```python
ruta = Path("datos") / "usuarios" / "archivo.txt"
print(ruta)
```

### 4.5 Comprobar si existe

```python
ruta = Path("archivo.txt")
print(ruta.exists())
```

### 4.6 Comprobar si es archivo o carpeta

```python
print(ruta.is_file())
print(ruta.is_dir())
```

## 5. Abrir un fichero

Para leer o escribir en un archivo, usamos la función `open()`.

```python
archivo = open("prueba.txt", "r", encoding="utf-8")
```

La función recibe:

- la ruta del archivo,
- el modo de apertura,
- la codificación (opcional, pero útil para texto).

## 6. Modos de apertura de archivos

Los modos más importantes son:

### `"r"` - lectura

Abre el archivo para leerlo. Si no existe, dará error.

```python
archivo = open("archivo.txt", "r", encoding="utf-8")
```

### `"w"` - escritura

Abre el archivo para escribir. Si existe, lo sobrescribe.

```python
archivo = open("archivo.txt", "w", encoding="utf-8")
```

### `"a"` - añadir

Abre el archivo para añadir contenido al final.

```python
archivo = open("archivo.txt", "a", encoding="utf-8")
```

### `"b"` - modo binario

Se usa con archivos no textuales.

```python
archivo = open("imagen.bin", "wb")
```

### `"r+"` - lectura y escritura

Permite leer y escribir sobre el mismo archivo.

### `"x"` - creación exclusiva

Crea un archivo y falla si ya existe.

## 7. Leer información de un fichero de texto

### `read()`

Lee todo el contenido del archivo.

```python
archivo = open("archivo.txt", "r", encoding="utf-8")
contenido = archivo.read()
print(contenido)
archivo.close()
```

### `readline()`

Lee una sola línea.

```python
archivo = open("archivo.txt", "r", encoding="utf-8")
linea = archivo.readline()
print(linea)
archivo.close()
```

### `readlines()`

Lee todas las líneas y devuelve una lista.

```python
archivo = open("archivo.txt", "r", encoding="utf-8")
lineas = archivo.readlines()
print(lineas)
archivo.close()
```

## 8. Escribir información en un fichero de texto

### `write()`

Escribe texto en el archivo.

```python
archivo = open("archivo.txt", "w", encoding="utf-8")
archivo.write("Hola mundo\n")
archivo.write("Estoy aprendiendo Python\n")
archivo.close()
```

### `writelines()`

Escribe varias líneas a la vez.

```python
archivo = open("archivo.txt", "w", encoding="utf-8")
lineas = ["Primera línea\n", "Segunda línea\n", "Tercera línea\n"]
archivo.writelines(lineas)
archivo.close()
```

## 9. Añadir contenido a un fichero

```python
archivo = open("archivo.txt", "a", encoding="utf-8")
archivo.write("Nueva línea añadida\n")
archivo.close()
```

Esto añade el contenido al final, sin borrar lo que ya había.

## 10. Buenas prácticas: usar `with`

Es recomendable abrir archivos usando `with`, porque Python los cierra automáticamente cuando termina el bloque.

```python
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)
```

Esto evita errores por no cerrar el fichero.

## 11. Ficheros binarios

Los archivos binarios no están formados por texto, sino por bytes. Se usan para:

- imágenes,
- archivos ejecutables,
- audio,
- videos,
- datos comprimidos.

### Escribir un archivo binario

```python
datos = b"\x00\x01\x02\x03\x04"

with open("datos.bin", "wb") as archivo:
    archivo.write(datos)
```

### Leer un archivo binario

```python
with open("datos.bin", "rb") as archivo:
    contenido = archivo.read()
    print(contenido)
```

### Modificar bytes

```python
with open("datos.bin", "wb") as archivo:
    archivo.write(b"Hola")
```

## 12. JSON: guardar y leer información estructurada

JSON es un formato muy popular para guardar datos de forma legible. Se usa mucho para:

- configuraciones,
- respuestas de APIs,
- datos de usuarios,
- listas de productos.

### Importar la librería `json`

```python
import json
```

### 12.1 Guardar un diccionario en JSON

```python
usuario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

with open("usuario.json", "w", encoding="utf-8") as archivo:
    json.dump(usuario, archivo, ensure_ascii=False, indent=4)
```

`json.dump()` guarda un diccionario en un archivo JSON.

### 12.2 Leer un JSON

```python
with open("usuario.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print(datos)
print(datos["nombre"])
```

`json.load()` lee la información del archivo y la convierte a Python.

### 12.3 Guardar una lista en JSON

```python
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
]

with open("personas.json", "w", encoding="utf-8") as archivo:
    json.dump(personas, archivo, ensure_ascii=False, indent=4)
```

### 12.4 Leer una lista desde JSON

```python
with open("personas.json", "r", encoding="utf-8") as archivo:
    personas = json.load(archivo)

for p in personas:
    print(p["nombre"])
```

## 13. Crear y leer carpetas con `pathlib`

### Crear una carpeta

```python
from pathlib import Path

ruta = Path("datos")
ruta.mkdir(exist_ok=True)
```

### Crear un archivo dentro de la carpeta

```python
archivo = ruta / "usuarios.txt"
archivo.write_text("Ana\nLuis\nMarta\n", encoding="utf-8")
```

### Leer un archivo dentro de una carpeta

```python
contenido = archivo.read_text(encoding="utf-8")
print(contenido)
```

### Escribir binario con `pathlib`

```python
ruta_binaria = Path("datos") / "datos.bin"
ruta_binaria.write_bytes(b"\x00\x10\x20")
```

### Leer binario con `pathlib`

```python
contenido_binario = ruta_binaria.read_bytes()
print(contenido_binario)
```

## 14. Diferencia entre texto y binario

### Texto

- se guarda como caracteres,
- suele usarse con archivos `.txt`, `.csv`, `.md`, `.json`,
- normalmente se usa codificación UTF-8.

### Binario

- se guarda como bytes,
- se usa para archivos no textuales,
- no suele leerse como texto directo.

## 15. Ejemplo práctico completo

```python
from loguru import logger
import json
from pathlib import Path

# Crear carpeta
carpeta = Path("datos")
carpeta.mkdir(exist_ok=True)

# Escribir texto
archivo_txt = carpeta / "notas.txt"
archivo_txt.write_text("Python\nJava\nC#\n", encoding="utf-8")

# Leer texto
logger.info(archivo_txt.read_text(encoding="utf-8"))

# Guardar JSON
usuario = {"nombre": "Ana", "edad": 25, "curso": "Python"}
archivo_json = carpeta / "usuario.json"
archivo_json.write_text(json.dumps(usuario, ensure_ascii=False, indent=4), encoding="utf-8")

# Leer JSON
info = json.loads(archivo_json.read_text(encoding="utf-8"))
logger.info(info["nombre"])
```

## 16. Errores comunes

### 1. Intentar leer un archivo que no existe

```python
with open("inexistente.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())
```

Esto produce un error `FileNotFoundError`.

### 2. Olvidar cerrar el archivo

Aunque Python cierra el archivo al terminar, es mejor usar `with` para evitar fugas de recursos.

### 3. Usar modo incorrecto

Si quieres escribir texto, usa `"w"` o `"a"` con texto. Si quieres archivos binarios, usa `"wb"` o `"rb"`.

## 17. Resumen

### Módulo `os`

Permite trabajar con rutas, carpetas, archivos y sistema operativo:

- `os.listdir()`
- `os.mkdir()`
- `os.makedirs()`
- `os.path.exists()`
- `os.remove()`
- `os.rename()`

### Módulo `pathlib`

Es una forma moderna y clara de manejar carpetas y archivos:

- `Path()`
- `.mkdir()`
- `.iterdir()`
- `.exists()`
- `.is_file()`
- `.write_text()`
- `.read_text()`
- `.write_bytes()`
- `.read_bytes()`

### Ficheros de texto

Se abren con `open(..., "r")`, `"w"`, `"a"`.

### Ficheros binarios

Se abren con `"rb"` y `"wb"`.

### JSON

Se guarda y lee con `json.dump()` y `json.load()`.

## 18. Consejo final

El manejo de archivos es una de las habilidades más prácticas para aprender a programar. Es muy común guardar datos, configurar proyectos o leer entradas de usuarios.

Si practicas con textos, JSON y archivos binarios, verás que trabajar con datos en Python se vuelve mucho más sencillo y útil.
