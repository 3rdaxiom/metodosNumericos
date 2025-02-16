import numpy as np
import matplotlib.pyplot as plt

# Definir la función g(x) para el método de punto fijo
# Esta función es una transformación de la ecuación original cos(x) - x = 0
# El método de punto fijo busca un punto x tal que g(x) = x
# En este caso, hemos despejado x de la ecuación original para obtener g(x) = cos(x)
def g(x):
    return np.cos(x)  # Transformación de cos(x) - x = 0

# Método de punto fijo
# x0: Valor inicial para la iteración
# tol: Tolerancia para la convergencia (error máximo permitido)
# max_iter: Número máximo de iteraciones para evitar bucles infinitos
def punto_fijo(x0, tol=1e-5, max_iter=100):
    iteraciones = []  # Lista para almacenar los resultados de cada iteración
    errores_abs = []  # Lista para almacenar los errores absolutos en cada iteración

    x_old = x0  # Valor anterior de x
    for i in range(max_iter):
        x_new = g(x_old)  # Calcular el nuevo valor de x usando la función g(x)
        e_abs = abs(x_new - x_old)  # Calcular el error absoluto

        iteraciones.append((i+1, x_new, e_abs))  # Guardar la iteración y el error
        errores_abs.append(e_abs)  # Guardar el error absoluto

        if e_abs < tol:  # Si el error es menor que la tolerancia, hemos convergido
            break

        x_old = x_new  # Actualizar el valor anterior de x para la siguiente iteración

    return iteraciones, errores_abs  # Devolver la lista de iteraciones y errores

# Parámetro inicial
x0 = 0.5
iteraciones, errores_abs = punto_fijo(x0)  # Llamar a la función de punto fijo

# Imprimir resultados
print("Iteración | x_n       | Error absoluto")
print("-------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e}")

# Graficar convergencia
# Crear un rango de valores de x para graficar la función g(x)
x_vals = np.linspace(0, 1, 100)  # Valores de x entre 0 y 1
y_vals = g(x_vals)  # Valores de g(x) correspondientes

plt.figure(figsize=(8, 5))  # Crear una figura de tamaño 8x5 pulgadas
plt.plot(x_vals, y_vals, label=r"$g(x) = \cos(x)$", color="blue")  # Graficar g(x)
plt.plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")  # Graficar la recta y=x
# Mostrar los puntos de iteración en el gráfico
plt.scatter([it[1] for it in iteraciones], [g(it[1]) for it in iteraciones], color="black", label="Iteraciones")
plt.xlabel("x")  # Etiqueta del eje x
plt.ylabel("g(x)")  # Etiqueta del eje y
plt.legend()  # Mostrar la leyenda
plt.grid()  # Mostrar la cuadrícula
plt.title("Método de Punto Fijo - Ejercicio 3")  # Título del gráfico
plt.show()  # Mostrar el gráfico