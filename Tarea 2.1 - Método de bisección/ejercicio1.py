import numpy as np
import matplotlib.pyplot as plt

# Definir la función cúbica a evaluar
def f(x):
    """
    Función cúbica: f(x) = x³ - 4x - 9.
    Esta función es la que se utilizará para encontrar la raíz mediante el método de bisección.
    """
    return x**3 - 4*x - 9  # Función f(x) = x³ - 4x - 9

# Algoritmo del método de bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    """
    Encuentra la raíz de una función mediante el método de bisección.

    Args:
        a: Límite inferior del intervalo inicial.
        b: Límite superior del intervalo inicial.
        tol: Tolerancia para la convergencia (error máximo permitido).
        max_iter: Número máximo de iteraciones para evitar bucles infinitos.

    Returns:
        Una tupla que contiene:
            - iteraciones: Una lista con los valores de 'c' (punto medio) en cada iteración.
            - errores_abs: Una lista con los errores absolutos en cada iteración.

    Raises:
        ValueError: Si el método de bisección no es aplicable en el intervalo dado (f(a) * f(b) >= 0).
    """
    if f(a) * f(b) >= 0:
        raise ValueError("El método de bisección no es aplicable en el intervalo dado. f(a) y f(b) deben tener signos opuestos.")

    iteraciones, errores_abs = [], []
    c_old = a  # Variable para calcular el error absoluto (valor de 'c' en la iteración anterior)

    for _ in range(max_iter):
        c = (a + b) / 2  # Punto medio del intervalo
        iteraciones.append(c)
        error = abs(c - c_old)  # Cálculo del error absoluto
        errores_abs.append(error)

        # Condición de parada: si la función en c es cercana a 0 o el error es menor que la tolerancia
        if abs(f(c)) < tol or error < tol:
            break

        # Determinar el nuevo intervalo
        if f(a) * f(c) < 0:
            b = c  # La raíz está entre 'a' y 'c'
        else:
            a = c  # La raíz está entre 'c' y 'b'

        c_old = c  # Actualizar el valor de c_old para la siguiente iteración

    return iteraciones, errores_abs

# Parámetros iniciales
a, b = 2, 3  # Intervalo donde se encuentra la raíz. Se debe cumplir f(a) * f(b) < 0

# Ejecutar el método de bisección
iteraciones, errores = biseccion(a, b)

# Graficar la convergencia
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(errores) + 1), errores, marker='o', linestyle='-', color='r')
plt.yscale("log")  # Escala logarítmica para el eje y (error)
plt.xlabel("Iteración")
plt.ylabel("Error Absoluto")
plt.title("Convergencia del Método de Bisección (Función Cúbica)")
plt.grid()
plt.show()

# Imprimir resultados (opcional)
# print("Iteraciones:", iteraciones)
# print("Errores absolutos:", errores)