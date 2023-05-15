# number = int(input("Введите число: "))
# summ = 0
# while number > 0:
#  summ += number
#  number = int(input("Введите число: "))
# print(summ)
#
# -----------------------------------------------------------------------------------------------------------------
#
# В один из вечеров к Васе домой пришёл племянник и пожаловался на сложности с уроками математики: у него никак не получалось разобраться со степенями чисел.
# Вася решил помочь племяннику и написать программу, которая позволит наглядно увидеть возведение чисел в третью степень.
# Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит результат на экран.
#
# num = int(input("Введите последнее число воздвигаемое в куб: "))
# count = 1
# while count <= num:
#     cub = count * count * count
#     print(f"Число - {count} в кубе будет - {cub}")
#     count += 1
# print("Конец")
# -------------------------------------------------------------------------------------------------------------------
#
# Напишите робота для коллекторов. В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, пока должник не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга робот сообщает об этом пользователю и благодарит его.
# Пример
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!
#
# name = input("Ваше имя? ")
# credit = int(input("Сумма долга: "))
# while credit > 0:
#     print(f"{name}, ваша задолженность составляет {credit} рублей")
#     debit = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
#     credit -= debit
#     if credit <= 0:
#         break
#     print(f"Маловато, {name}. Давайте ещё раз.")
# print(f"Отлично, {name}! Вы погасили долг. Спасибо!")
# ----------------------------------------------------------------------------------------------------------------------
#
# Максим программирует целый день на работе и вечером идёт домой. Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа. Вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.
# Напишите программу, в которой считается, сколько задач выполнил Максим за день (восемь часов).
# Если он хотя бы раз взял трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
#
# Пример
# Начался восьмичасовой рабочий день.
# 1-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 2-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 3-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 4-й час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 5-й час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 6-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 7-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 8-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин.
#
# work = 8
# hours = 1
# shop = 0
# mission = 0
# print("Начался восьмичасовой рабочий день.")
# while hours < 9:
#     print(f"{hours}-й час")
#     todos = int(input("Сколько задач решит Максим? "))
#     wife = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
#     mission += todos
#     shop += wife
#     hours += 1
# print(f"Рабочий день закончился. Всего выполнено задач: {mission}")
# if shop > 0:
#     print("Нужно зайти в магазин.")
# --------------------------------------------------------------------------------------------------------------------

