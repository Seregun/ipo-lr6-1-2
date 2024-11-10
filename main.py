# Задача:
# Написать программу, которая:
# 1. Создает двумерную матрицу произвольного размера (высота и ширина от 4 до 8),
#    заполненную значениями из списка [-3, -5, -2, -12, 0, 15, 4, 7, 2].
# 2. Выводит данную матрицу в форматированном виде.
# 3. Выводит сумму всех четных элементов матрицы.

import random  # Импортируем модуль random для работы со случайными числами
values = [-3, -5, -2, -12, 0, 15, 4, 7, 2] # Исходный список значений для заполнения матрицы
rows = int(input("Введите размер высоты матрицы (от 4 до 8): ")) # Запрашиваем число для высоты матрицы в диапазоне от 4 до 8
while rows < 4 or rows > 8: # Проверка размера матрицы по высоте
    rows = int(input("Введите корректное значение для высоты (от 4 до 8): "))
cols = int(input("Введите размер ширины матрицы (от 4 до 8): ")) # Запрашиваем число для ширины матрицы в диапазоне от 4 до 8
while cols < 4 or cols > 8: # Проверка размера матрицы по ширине
    cols = int(input("Введите корректное значение для ширины (от 4 до 8): "))
matrix = [] # Создаем пустую матрицу, которая будет заполняться случайными значениями из списка values
for i in range(rows):  # Цикл для строк матрицы
    row = []  # Создаем пустой список для текущей строки
    for j in range(cols):  # Цикл для столбцов матрицы
        row.append(random.choice(values))  # Добавляем случайный элемент из values в строку
    matrix.append(row)  # Добавляем строку в матрицу
print("Сгенерированная матрица:")
for row in matrix:  # Проходим по каждой строке матрицы
    print(" ".join(f"{x:4}" for x in row))  # Форматируем и выводим каждое значение строки
even_sum = 0 # Инициализируем переменную для хранения суммы четных чисел
for row in matrix:  # Проходим по каждой строке матрицы
    for elem in row:  # Проходим по каждому элементу строки
        if elem % 2 == 0:  # Проверяем, является ли элемент четным
            even_sum += elem  # Добавляем четный элемент к сумме
print(f"Сумма всех четных элементов матрицы: {even_sum}") # Выводим результат