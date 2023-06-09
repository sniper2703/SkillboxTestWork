# Нас наняла букмекерская контора, где проводятся ставки на конный спорт.
# Напишите программу расчёта потенциального выигрыша игрока.
# Для этого вводится его ставка в рублях и коэффициент (вещественное число), а выводится их произведение в качестве потенциального выигрыша.
# Пример:
# Сколько ставим? 1234
# Какой коэффициент? 1.716
# Потенциальный выигрыш: 2117.544
# Усложнение задачи: сделайте так, чтобы после точки выводилось не больше двух цифр.
#
# bet = int(input("Введите ставку: "))
# coef = float(input("Введите коэффициент: "))
#
# win = bet * coef
# print("Потенциальный выигрыш:", round(win, 2))
# ---------------------------------------------------------------------------------------------------------------------
# Алексей работает диетологом в частной клинике, каждый день он принимает пациентов разных возрастов и с разными показателями роста (в метрах) и веса (в кг).
# Для каждого человека ему нужно считать индекс массы тела - это вес поделить на рост в квадрате.
# По государственным стандартам индекс округляется до двух знаков после точки.
# Затем по этому индексу определяется, всё ли в порядке у человека с массой тела:
# если до 18.5, то недобор;
# до 25 - всё нормально,
# до 30 уже идёт избыток,
# а после 30 - ожирение.
# Напишите такую программу для Алексея.
#
# height = float(input("Ваш рост: "))
# weight = float(input("Ваш вес: "))
#
# bmi = round((weight / height ** 2), 2)
# print(f"Ваш индекс массы тела: {bmi}")
#
# if bmi < 18.5:
#     print("Недостаточно веса")
# elif bmi < 25:
#     print("Норма")
# elif bmi < 30:
#     print("Избыток")
# else:
#     print("Ожирение")
# ---------------------------------------------------------------------------------------------------------------------
# Вы пишете программу-инсталлятор для компьютерной игры.
# Пока инсталлятор скачивает обновление, пользователю нужно показать, сколько процентов уже скачалось,
# чтобы он мог решить: пойти заварить чаю или подождать у экрана компьютера.
# Обновления игры всегда занимают разное количество мегабайт, да и скорость интернет-соединения у игроков разная.
# Напишите программу, принимающую на вход размер файла обновления в мегабайтах и скорость интернет-соединения в мегабайтах в секунду.
# Для каждой секунды программа рассчитывает и выводит на экран, сколько процентов от всего объёма уже скачано, до тех пор, пока не будет скачан весь объём.
# В конце программа должна показать, сколько всего секунд заняло скачивание обновления. Обеспечьте контроль ввода.
# Пример:
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения? 27
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)
#
# load = float(input("Укажите размер файла для скачивания: "))
# speed = float(input("Какова скорость вашего соединения? "))
# load_contr = 0
# time = 0
#
# while load_contr < load:
#     time += 1
#     load_contr += speed
#     if load_contr > load:
#         print(f"Прошло {int(time)} сек. Скачано {int(load)} из {int(load)} Мб (100%)")
#     else:
#         procent = 100 / (load / load_contr)
#         print(f"Прошло {int(time)} сек. Скачано {int(load_contr)} из {int(load)} Мб ({int(procent)}%)")
# ----------------------------------------------------------------------------------------------------------------------

