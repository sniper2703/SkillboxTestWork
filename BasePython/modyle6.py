# Что нужно сделать
# В свободное время Вася любит играть в компьютерные игры. Однажды у него появилась классная идея для сюжета игры.
# Чтобы воплотить её в жизнь, он начал изучать геймдизайн. Создавать игру он начал с главного героя и его системы прокачки.
# Напишите программу, которая определяет уровень персонажа в компьютерной игре.
# Пользователь вводит число «очков опыта», а программа вычисляет уровень.
# Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.
# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4
# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2
#
# level = int(input("Введите количество очков опыта: "))
#
# if level >= 1 and level < 1000:
#     print("Ваш уровень - 1")
# elif level >= 1000 and level < 2500:
#     print("Ваш уровень - 2")
# elif level >= 2500 and level < 5000:
#     print("Ваш уровень - 3")
# elif level >= 5000:
#     print("Ваш уровень - 4")
# else:
#     print("Неверно введены данные")
#
# --------------------------------------------------------------------------------------------------------------------
#
# Учитель математики придумывает каждому ученику отдельные функции, которые нужно отобразить на графике и посчитать.
# Ещё учитель разбирается в программировании, и чтобы не считать вручную эти функции, он написал программу, которая делает работу за него.
# Напишите программу, которая получает от пользователя число X и вычисляет значение функции Y по следующей схеме:
# Напомним, как это работает:
# для X > 0, Y = X − 12
# для X = 0, Y = 5
# для X < 0, Y = X*2
# Пример:
# Введите икс: 0
# Игрек равен 5
# Пример 2:
# Введите икс: −6
# Игрек равен 36
#
# x = int(input("Введите чему равен икс: "))
# y = 0
#
# if x > 0:
#     y = x - 12
#     print("Y равен", y)
# elif x == 0:
#     y = 5
#     print("Y равен", y)
# elif x < 0:
#     y = x * 2
#     print("Y равен", y)
# else:
#     print("Неверно введены данные")
#
# ---------------------------------------------------------------------------------------------------------------------
