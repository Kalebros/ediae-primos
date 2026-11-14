# Ejercicios de práctica para aprender Python

Este documento reúne cien ejercicios de programación para practicar los conceptos explicados en las guías del proyecto. Están pensados para trabajar con el proyecto actual y para reforzar tanto la lógica como la escritura de código limpio, reutilizable y mantenible.

Los ejercicios están organizados por temática y su dificultad es variable. Algunos son sencillos, otros más completos, y no todos tienen por qué seguir un orden estrictamente creciente.

## 1. Fundamentos de Python

1. Crea una variable llamada `nombre` con tu nombre y muéstrala por pantalla.
2. Escribe un programa que pida al usuario su edad y la imprima con un mensaje.
3. Calcula la suma de dos números introducidos por teclado.
4. Escribe un programa que determine si un número es positivo, negativo o cero.
5. Crea un programa que imprima los números del 1 al 10 usando un bucle `for`.
6. Haz un bucle `while` que cuente de 10 a 1.
7. Escribe una función que devuelva el doble de un número.
8. Escribe una función que reciba dos números y devuelva su resta.
9. Escribe una función que reciba una lista de números y devuelva la suma total.
10. Escribe una función que devuelva `True` si un número es par y `False` si es impar.
11. Crea un programa que recorra una cadena y muestre cada carácter en una línea.
12. Escribe una función que convierta una cadena en mayúsculas.
13. Escribe una función que reciba una cadena y diga si es un palíndromo.
14. Escribe un programa que calcule el promedio de una lista de números.
15. Crea una función que reciba una lista y devuelva el mayor elemento.

## 2. Listas, slices y comprehensions

16. Crea una lista con cinco nombres y muéstrala completa.
17. Accede al segundo elemento de una lista y muéstralo.
18. Crea una lista de números y extrae los tres primeros con slicing.
19. Crea una lista de números del 1 al 10 y obtén solo los pares con slicing.
20. Invierte una lista con slicing.
21. Añade un elemento al final de una lista usando `append()`.
22. Inserta un elemento en una posición concreta con `insert()`.
23. Elimina un elemento concreto con `remove()`.
24. Elimina el último elemento con `pop()`.
25. Ordena una lista de números de menor a mayor con `sort()`.
26. Cuenta cuántas veces aparece un valor en una lista con `count()`.
27. Obtén la posición de un valor usando `index()`.
28. Crea una lista con los cuadrados de los números del 1 al 10 usando comprehension.
29. Crea una lista con los números impares del 1 al 20 usando comprehension.
30. Dada una lista de nombres, crea otra lista con solo los que empiecen por "A".
31. Dada una lista de palabras, crea otra con sus versiones en mayúsculas.
32. Crea una lista de diccionarios con información de personas y luego extrae solo los nombres.
33. Dada una lista de números, elimina los duplicados usando `set()` y luego conviértelo a lista.
34. Crea una lista de 10 números aleatorios y calcula su suma.
35. Dada una lista de strings, ordena por longitud de palabra.

## 3. Cadenas de texto

36. Crea una función que cuente cuántos caracteres tiene una frase.
37. Escribe un programa que convierta una frase a minúsculas y luego a mayúsculas.
38. Busca la posición de la palabra "Python" en una cadena usando `find()`.
39. Reemplaza todas las apariciones de una palabra por otra usando `replace()`.
40. Divide una frase en palabras usando `split()`.
41. Une una lista de palabras con un espacio usando `join()`.
42. Elimina espacios al principio y al final de una cadena con `strip()`.
43. Crea una función que reciba un correo y devuelva el dominio usando `split("@")`.
44. Escribe un programa que detecte si una cadena empieza con una palabra determinada.
45. Escribe una función que invierta una cadena con slicing.
46. Crea una función que diga si una cadena contiene solo letras y espacios.
47. Recorre una frase y cuenta cuántas vocales tiene.
48. Escribe un código que convierta una lista de palabras en una sola frase separada por comas.
49. Crea una función que elimine los espacios duplicados de una frase.
50. Escribe un programa que cuente cuántas palabras hay en una frase.

## 4. Diccionarios, sets y frozensets

51. Crea un diccionario con información personal y muéstralo por pantalla.
52. Accede al valor de una clave concreta en un diccionario.
53. Añade una nueva clave a un diccionario.
54. Modifica el valor de una clave existente.
55. Elimina una clave del diccionario con `pop()`.
56. Recorre un diccionario con `items()` y muestra claves y valores.
57. Recorre un diccionario con `keys()` y muestra solo las claves.
58. Recorre un diccionario con `values()` y muestra solo los valores.
59. Crea un diccionario con comprehension a partir de una lista de números.
60. Crea un set con varios elementos y comprueba si un valor está dentro del set.
61. Elimina duplicados de una lista usando un set.
62. Crea un conjunto de números pares y otro de impares y muestra su intersección.
63. Calcula la unión de dos sets.
64. Calcula la diferencia entre dos sets.
65. Crea un `frozenset` y comprueba que no se puede modificar.
66. Crea un set comprehension con los cuadrados de los números del 1 al 10.
67. Haz un diccionario que relacione cada palabra con el número de veces que aparece en una lista.
68. Escribe un programa que cuente cuántos elementos únicos hay en una lista.
69. Crea un diccionario con los nombres de 5 personas y sus edades, y luego ordénalo por edad.
70. Crea un programa que convierta una lista de tuplas en un diccionario usando `dict()`.

## 5. Enums, anotaciones y clases

71. Define un `Enum` con tres estados de pedido: pendiente, enviado y entregado.
72. Escribe una función anotada que reciba un número entero y devuelva una cadena.
73. Crea una clase `Persona` con atributos `nombre` y `edad`.
74. Añade un método `saludar()` a la clase `Persona`.
75. Crea una clase `Coche` con atributos `marca`, `modelo` y `matricula`.
76. Implementa un constructor `__init__` para una clase `Libro`.
77. Crea una dataclass llamada `Producto` con `nombre`, `precio` y `stock`.
78. Añade un método a una dataclass para mostrar el precio final con IVA.
79. Crea una clase con una propiedad `edad` usando `@property`.
80. Haz una clase `Cuenta` con el atributo `_saldo` y un método para consultar el saldo.
81. Define un `Enum` para los roles de usuario: admin, editor y visitante.
82. Crea una función que reciba un `RolUsuario` y muestre un mensaje según el valor.
83. Define una clase `Animal` abstracta con un método abstracto `hablar()`.
84. Crea dos clases hijas de `Animal` y sobreescribe `hablar()`.
85. Escribe una clase `Persona` y otra `Empleado` que herede de ella.
86. Crea una clase `Figura` con método `area()` y luego implementa `Cuadrado` y `Circulo`.
87. Crea un `@staticmethod` para calcular el área de un rectángulo.
88. Crea un `@classmethod` que cuente cuántas instancias de una clase se han creado.
89. Escribe un decorador que imprima un mensaje antes y después de ejecutar una función.
90. Crea una dataclass con validación simple de datos (por ejemplo, que la edad no sea negativa).

## 6. Ficheros, JSON y excepciones

91. Escribe un programa que cree un archivo de texto llamado `notas.txt` y escriba tres líneas.
92. Lee el contenido de un archivo de texto y muéstralo por pantalla.
93. Añade una nueva línea al final de un archivo usando modo append.
94. Crea una carpeta llamada `datos` y dentro un archivo `usuarios.txt`.
95. Guarda un diccionario en un archivo JSON usando `json.dump()`.
96. Lee un archivo JSON con `json.load()` y muestra uno de sus valores.
97. Escribe un programa que lea un archivo binario y muestre sus bytes.
98. Crea un archivo binario con varios bytes y luego léelo con `read()`.
99. Escribe un bloque `try/except` para manejar una división por cero.
100. Escribe un bloque `try/except/finally` para leer un archivo que puede no existir.

## 7. Sugerencias para usar estos ejercicios

- Intenta resolver varios ejercicios sin mirar la solución.
- Reescribe las mismas soluciones en formas distintas para practicar.
- Cuando un ejercicio te parezca fácil, intenta hacerlo más general o más robusto.
- Si un resultado te preocupa, añade validaciones y manejo de errores.
- Después de resolver un ejercicio, trata de escribir una prueba con `pytest` para comprobarlo.
- Usa el proyecto actual como laboratorio: prueba ideas sobre `app/primos.py`, listas, archivos, JSON y pruebas automatizadas.

## 8. Consejos para llevarlo a la práctica

- Empieza por los ejercicios sencillos y luego ve aumentando la dificultad.
- Revisa los temas de las guías relacionadas antes de intentar los ejercicios más complejos.
- No te preocupes si algunas tareas tardan más: la práctica es la mejor forma de aprender.
- Combina teoría y ejecución: escribe código, ejecútalo y corrige errores.
- Acostúmbrate a leer la documentación, pensar antes de escribir y probar pequeñas soluciones.

Este conjunto de ejercicios está pensado para ayudarte a consolidar el aprendizaje de Python de forma práctica, aplicada y progresiva.
