# for a in range(0, 10):
#     for b in range(a, a - 10, -1):
#         print(b, end = "\t")
#     print()
# ---------------------------------------------------------------------------------------------------------
# Напишите программу, которая выводит квадратную матрицу размера N на N.
# В каждой нечётной строке матрицы идут числа от 1 до N, а в каждой чётной — просто числа, равные номеру этой строки.
# size = int(input("Введите размер матрицы: "))
#
# for a in range(1, size + 1):
#     for b in range(1, size + 1):
#         if a % 2 == 0:
#             print(a, end = " ")
#         else:
#             print(b, end = " ")
#     print()
# ------------------------------------------------------------------------------------------------------------------
# Напишите программу, которая рисует координатные оси на поле 20×50.
#
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()
# ---------------------------------------------------------------------------------------------------------------------
# Напишите программу, которая выводит в консоль «врата», состоящие из тире, вертикальных линий и пробелов.
# Поле состоит из 20 строк и 30 столбцов (но не стесняйтесь пробовать и другие размеры).
#
# for row in range(20):
#     for col in range(30):
#         if row == 0:
#             print("-", end="")
#         elif col == 0 or col == 29:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()
# ---------------------------------------------------------------------------------------------------------------------
#
# Мы делаем текстовую игру — гонку, и нам нужно вывести на экран что-то вроде трассы, где будут соревноваться наши машины.
# Напишите программу, которая выводит такую дорогу на экран (поле 20×50).
#
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#         elif col == row + 29:
#             print("\\", end="")
#         elif col == -row + 19:
#             print("/", end="")
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()
# ----------------------------------------------------------------------------------------------------------------------
#
# Напишите программу, которая получает на вход размер квадратной матрицы и выводит на экран по такому принципу
# диагональ из единиц с левого нижнего угла до верхнего правого, ниже диагонали — двойки, выше — нули.
#
# size = int(input("Введите размер квадрата: "))
#
# for row in range(size):
#     for col in range(size, 0, -1):
#         if row > col - 1:
#             print("2", end=" ")
#         elif row == col - 1:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()
# ----------------------------------------------------------------------------------------------------------------------
#
# Нам дали заказ написать программу для электронной очереди.
# У каждого человека в очереди есть номер: нулевой, первый, второй, третий и так далее.
# Каждый час очередь уменьшается на одного человека, то есть уходит сначала нулевой номер, затем первый, второй и так далее.
# Наша программа получает на вход одно число — количество людей в очереди — и выводит на экран историю обслуживания очереди: какие номера в какой час оставались.
#
# people = int(input("количество людей в очереди: "))
# for hour in range(people):
#     print(f"Прошло {hour} часов")
#     for i in range(hour, people):
#         print(f"{i} номер очереди")
#     print()
# print("Все обслужены")
# ----------------------------------------------------------------------------------------------------------------------
#
# Пользователь вводит последовательность из N чисел.
# Напишите программу, которая подсчитывает общее количество цифр больше пяти во всей последовательности.
#
# seqNum = int(input("Сколько будет чисел: "))
# numeralCount = 0
# for num in range(seqNum):
#     number = int(input("Введите число: "))
#     while number > 0:
#         if number % 10 > 5:
#             numeralCount += 1
#         number //= 10
# print(f"Цифр больше 5 в последовательности {numeralCount}")
# ----------------------------------------------------------------------------------------------------------------------
#
# num = int(input("Введите число: "))
# for i in range(num + 1):
#     for y in range(i, num + 1):
#         print(y, end=" ")
#     print()
# -----------------------------------------------------------------------------------------------------------------------
# count = 11
# for i in range(6):
#     for a in range(i, count, 2):
#         print(a, end="\t")
#     count += 1
#     print()
# ----------------------------------------------------------------------------------------------------------------------
#
# num = int(input("Введите число: "))
# for i in range(num+1):
#     for a in range(i):
#         print(i, end="\t")
#     print()
# ----------------------------------------------------------------------------------------------------------------------
#
# Напишите программу, которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха (|), а для горизонтальных — дефис (-).
# Пусть пользователь вводит ширину и высоту рамки.
#
# withs = int(input("Введите ширину: "))
# hight = int(input("Введите высоту: "))
#
# for row in range(hight):
#     for col in range(withs):
#         if col == 0 or col == withs-1:
#             print("|", end="")
#         elif row == 0 or row == hight-1:
#             print("-", end="")
#         else:
#             print(" ", end="")
#     print()
# ----------------------------------------------------------------------------------------------------------------------
# Напишите программу, которая выводит на экран крест из символов «^»
# (символы выводятся по диагоналям воображаемого квадрата).
# num = int(input("Введите число: "))
#
# for row in range(num):
#     for col in range(num):
#         if col == -row + num -1 or col == row:
#             print("^", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# -----------------------------------------------------------------------------------------------------------------------
# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.
# Пример:
# Введите кол-во чисел: 6
# Введите число: 4
# Введите число: 7
# Введите число: 20
# Введите число: 3
# Введите число: 11
# Введите число: 37
# Количество простых чисел в последовательности: 4

# ----------------------------------------------------------------------------------------------------------------------
#
# Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами
#
# rows = int(input("Введите количество ступеней: "))
# new_num = 1
#
# for line in range(rows):
#     space_count = rows - line - 1
#     print("   " * space_count, end="")
#     for number in range(line + 1):
#         print(new_num, end="    ")
#         new_num += 2
#     print()
# ----------------------------------------------------------------------------------------------------------------------
#
# Вы пишите компьютерную игру с текстовой графикой, вам поручили написать генератор ландшафта.
# Напишите программу, которая получает на вход число N и выводит на экран числа в виде «ямы»

depth = int(input("Введите глубину ямы: "))

for line in range(depth):
    for left_number in range(depth, depth - line - 1, - 1):
        print(left_number, end="")
    point_count = 2 * (depth - line - 1)
    print("." * point_count, end="")
    for right_number in range(depth - line, depth + 1):
        print(right_number, end="")
    print()