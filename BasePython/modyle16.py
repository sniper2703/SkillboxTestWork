# У вас есть список numbers. Напишите программу, которая заполняет список числами от 0 до 100 и выводит его на экран.
#
# numbers = []
#
# for num in range(101):
#     numbers.append(num)
# print(numbers)
# ----------------------------------------------------------------------------------------------------------------------
# В любой компании есть список сотрудников. Руководство одной компании хочет знать, на рабочем месте ли сейчас сотрудник.
# У каждого сотрудника есть пропуск со своим ID-номером (это положительное число), список активных пропусков сотрудников известен заранее.
# Напишите программу, которая сначала запрашивает у пользователя количество сотрудников в офисе, ID их пропусков,
# а затем запрашивает ID пропуска, который нужно найти в этом списке.
# Если такой есть, то вывести «Сотрудник на месте», а иначе «Сотрудник не работает!».
# Пример:
# Кол-во сотрудников в офисе: 4
# ID сотрудника: 10
# ID сотрудника: 20
# ID сотрудника: 30
# ID сотрудника: 40
# Какой ID ищем? 35
# Сотрудник не работает!
#
# id_count = int(input("Кол-во сотрудников в офисе: "))
# id_list = []
#
# for _ in range(id_count):
#     id = int(input("ID сотрудника: "))
#     id_list.append(id)
# id_search = int(input("Какой ID ищем? "))
# if id_search in id_list:
#     print("Сотрудник на месте")
# else:
#     print("Сотрудник не работает!")
# ----------------------------------------------------------------------------------------------------------------------
#
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
# maximum = nums_list[0]
# minimum = nums_list[0]
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#     elif minimum > i:
#         minimum = i
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)
# -----------------------------------------------------------------------------------------------------------------------
#
# word = input("Введите слово: ")
# replace_num = int(input("Номер символа для замены: "))
# replace_sym = input("Чем заменить? ")
#
# sym_list = list(word)
# sym_list[replace_num - 1] = replace_sym
#
# for i in sym_list:
#     print(i, end='')
# ----------------------------------------------------------------------------------------------------------------------
# Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от одного до N.
# Пример 1:
# Введите число: 1
# Список из нечётных чисел от одного до N: [1]
# Пример 2:
# Введите число: 14
# Список из нечётных чисел от одного до N: [1, 3, 5, 7, 9, 11, 13]
#
# num_list = []
# num_count = int(input("Введите число: "))
#
# for i in range(num_count + 1):
#     if i % 2 != 0:
#         num_list.append(i)
# print(f"Список из нечётных чисел от одного до {num_count}: {num_list}")
# ----------------------------------------------------------------------------------------------------------------------
# Для соревнований по волейболу необходимо сформировать турнирнирную сетку для восьми человек на два дня.
# На первый день решили выбрать каждого второго из списка участников.
# Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар.
# Напишите программу, которая выводит элементы списка только с чётными индексами.
# Пример:
# Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']
#
# players_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
# first_day = []
#
# for i in range(0, len(players_list), 2):
#     first_day.append(players_list[i])
# print(f"Первый день: {first_day}")
# ----------------------------------------------------------------------------------------------------------------------
# Илья зашёл на любительский киносайт, на котором пользователи оставляют рецензии на фильмы. Их список:
# films = [‘Крепкий орешек’, ‘Назад в будущее’, ‘Таксист’, ‘Леон’, ‘Богемская рапсодия’, ‘Город грехов’, ‘Мементо’, ‘Отступники’, ‘Деревня’]
# Илья на сайте в первый раз. Он хочет зарегистрироваться и сразу добавить часть фильмов в список любимых, чтобы позже прочитать рецензии на них.
# Напишите программу, в которой пользователь вводит фильм. Если фильм есть в перечне, то добавляется в список любимых.
# Если фильма нет, то выводится ошибка. В конце выведите весь список любимых фильмов.
# Пример:
# Сколько фильмов хотите добавить? 3
# Введите название фильма: Леон
# Введите название фильма: Безумный Макс
# Ошибка: фильма Безумный Макс у нас нет :(
# Введите название фильма: Мементо
# Ваш список любимых фильмов: Леон, Мементо
#
# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
# num = int(input("Сколько фильмов хотите добавить? "))
# like_films = []
#
# while len(like_films) != num:
#     film = input("Введите название фильма: ")
#     if film in films:
#         if film in like_films:
#             print("Этот фильм уже выбран")
#         else:
#             like_films.append(film)
#
#     else:
#         print(f"Ошибка: фильма {film} у нас нет :(")
# print(f"Ваш список любимых фильмов: {like_films}")
# ----------------------------------------------------------------------------------------------------------------------
# Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на экран.
# Дополнительный список нельзя использовать.
# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.
# Пример:
# Изначальный список: [1, 4, -3, 0, 10]
# Отсортированный список: [-3, 0, 1, 4, 10]
#
# def selection_sort(my_list):
#     for i_mn in range(len(my_list)):
#         for curr in range(i_mn, len(my_list)):
#             if my_list[curr] < my_list[i_mn]:
#                 my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]
#
# nums = [4, 9, 7, 6, 3, 2]
#
# selection_sort(nums)
#
# print(nums)
