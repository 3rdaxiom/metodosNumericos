import numpy as np
import matplotlib.pyplot as plt

# Definición de la función original
# Esta función representa un polinomio de tercer grado
# cuyas raíces se determinarán mediante interpolación y bisección.
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

# Implementación del método de interpolación de Lagrange
# Se usa para construir un polinomio interpolante a partir de puntos dados.
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)  # Número de puntos dados
    result = 0  # Variable para almacenar el resultado de la interpolación
    for i in range(n):
        term = y_points[i]  # Se inicia con el valor de y correspondiente
        for j in range(n):
            if i != j:
                # Se construye el producto de los términos de Lagrange
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term  # Se suma el término al resultado final
    return result

# Método de Bisección para encontrar raíces de una función
# Incluye el cálculo de errores absolutos, relativos y cuadráticos.
def bisect(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError("El intervalo no contiene una raíz")

    # Listas para almacenar los errores en cada iteración
    errores_abs = []
    errores_rel = []
    errores_cuad = []

    c_old = a  # Inicialización de la variable para el cálculo de errores
    for _ in range(max_iter):
        c = (a + b) / 2  # Punto medio del intervalo
        error_abs = abs(c - c_old)  # Cálculo del error absoluto
        error_rel = error_abs / abs(c) if c != 0 else 0  # Cálculo del error relativo
        error_cuad = error_abs ** 2  # Cálculo del error cuadrático

        # Se almacenan los errores en las listas correspondientes
        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)

        # Condición de parada basada en la tolerancia
        if abs(func(c)) < tol or (b - a) / 2 < tol:
            return c, errores_abs, errores_rel, errores_cuad

        # Actualización del intervalo según el signo de la función en c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

        c_old = c  # Actualización del valor anterior de c

    return (a + b) / 2, errores_abs, errores_rel, errores_cuad

# Selección de tres puntos adecuados dentro del intervalo [1,3]
# Se eligen estos puntos para construir el polinomio interpolante.
x0 = 2.0
x1 = 2.5
x2 = 3.0
x_points = np.array([x0, x1, x2])  # Puntos de interpolación
y_points = f(x_points)  # Evaluación de la función en los puntos seleccionados

# Construcción del polinomio interpolante de Lagrange
x_vals = np.linspace(x0, x2, 100)  # Puntos para graficar la interpolación
y_interp = [lagrange_interpolation(x, x_points, y_points) for x in x_vals]

# Encontrar la raíz del polinomio interpolante usando el método de bisección
root, errores_abs, errores_rel, errores_cuad = bisect(lambda x: lagrange_interpolation(x, x_points, y_points), x0, x2)

# Gráfica de la función y la interpolación
plt.figure(figsize=(8, 6))
plt.plot(x_vals, f(x_vals), label="$f(x) = x^{3}$ - $6x^{2}$ + 11x - 6", linestyle='dashed', color='blue')
plt.plot(x_vals, y_interp, label="Interpolación de Lagrange", color='red')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Línea del eje x
plt.axvline(root, color='green', linestyle='dotted', label=f"Raíz aproximada: {root:.4f}")
plt.scatter(x_points, y_points, color='black', label="Puntos de interpolación")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Interpolación y búsqueda de raíces")
plt.legend()
plt.grid(True)
plt.savefig("interpolacion_raices.png")  # Guardar la gráfica como imagen
plt.show()

# Imprimir la raíz encontrada mediante interpolación
print(f"La raíz aproximada usando interpolación es: {root:.4f}")

# Imprimir los errores en cada iteración del método de bisección
print("Errores en cada iteración del método de bisección:")
print("Iteración\tError Absoluto\tError Relativo\tError Cuadrático")
for i, (ea, er, ec) in enumerate(zip(errores_abs, errores_rel, errores_cuad)):
    print(f"{i+1}\t{ea:.6e}\t{er:.6e}\t{ec:.6e}")
