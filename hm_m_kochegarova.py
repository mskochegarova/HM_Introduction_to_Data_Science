# -*- coding: utf-8 -*-
"""HM_M_Kochegarova

'''
Задача №1

2x1 + 2x3 = -2
2x1 - 2x3 = 6
3x2 - x1 = -1

Выражаем x3 из первого и второго уравнения

x3 = -1 - x1
x3 = x1 - 3

=> x1 = 1

Подставляем x1 в систему уравнений и получаем
x1 = 1
x2 = 0
x3 = -2

'''
import numpy as np

# Матрица коэффициентов
A = np.array([[2, 0, 2],
              [2, 0, -2],
              [-1, 3, 0]])

# Вектор констант
B = np.array([-2, 6, -1])

# Решение системы уравнений
solution = np.linalg.solve(A, B)

x1, x2, x3 = solution
print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")

# Задача №4

import matplotlib.pyplot as plt
import numpy as np

v1 = np.array([0.98480775, 0.17364818])
v2 = np.array([-0.64278761, 0.76604444])
v3 = np.array([-0.34202014, -0.93969262])

# Функция для рисования вектора
def draw_vector(origin, vector, **kwargs):
    plt.quiver(*origin, *vector, angles='xy', scale_units='xy', scale=1, **kwargs)

# Начальная точка
origin = np.array([0, 0])

# Рисуем векторы
draw_vector(origin, v1, color='r', label='v1')
draw_vector(origin, v2, color='g', label='v2')
draw_vector(origin, v3, color='b', label='v3')

# Пределы графика
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# Добавляем сетку, оси, легенду и заголовок
plt.axhline(0, color='k', lw=0.5)
plt.axvline(0, color='k', lw=0.5)
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Визуализация векторов")
plt.legend()
plt.show()

# Проверяем, равна ли сумма нулю
sum_vectors = v1 + v2 + v3
print("Сумма векторов:", sum_vectors)

# Задача №1 Lesson 2

import numpy as np

def matrix_trace(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError("Входные данные должны быть массивом NumPy.")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Матрица должна быть квадратной.")

    return np.trace(matrix)

# Пример использования:
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

trace_A = matrix_trace(A)
print("След матрицы A:", trace_A)

# Задача №5 Lesson 2
import numpy as np

def matrix_multiplication(A, B):
    """
    Умножает две матрицы A и B.

    A (np.ndarray): Первая матрица.
    B (np.ndarray): Вторая матрица.
    """
    if not (isinstance(A, np.ndarray) and isinstance(B, np.ndarray)):
        raise ValueError("Обе матрицы A и B должны быть массивами NumPy.")

    if A.shape[1] != B.shape[0]:
        raise ValueError("Количество столбцов в A должно равняться количеству строк в B.")

    return np.dot(A, B)

# Пример использования:
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = matrix_multiplication(A, B)

print("Результат умножения матриц C = AB:\n", C)
