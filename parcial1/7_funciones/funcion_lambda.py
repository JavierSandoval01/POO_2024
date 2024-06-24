# lambdas_intermedio.py

# Ejemplo básico de una función lambda para sumar dos números
suma = lambda x, y: x + y
print(f"Suma de 5 y 3: {suma(5, 3)}")

# Lambda en una función de orden superior (map) para elevar al cuadrado una lista de números
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Cuadrados de los números {numeros}: {cuadrados}")

# Lambda en una función de orden superior (filter) para encontrar números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares en {numeros}: {pares}")

# Lambda en una función de orden superior (reduce) para multiplicar todos los números de una lista
from functools import reduce
producto = reduce(lambda x, y: x * y, numeros)
print(f"Producto de los números {numeros}: {producto}")

# Lambda para ordenar una lista de tuplas por el segundo elemento
tuplas = [(1, 'uno'), (3, 'tres'), (2, 'dos')]
ordenado = sorted(tuplas, key=lambda x: x[1])
print(f"Lista de tuplas ordenadas por el segundo elemento: {ordenado}")

# Lambda con valores por defecto
incremento = lambda x, inc=1: x + inc
print(f"Incrementar 5 por defecto: {incremento(5)}")
print(f"Incrementar 5 en 3: {incremento(5, 3)}")
