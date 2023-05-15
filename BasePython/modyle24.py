# nums_sum = 0
# nums_count = 0
#
# try:
#     numbers_files = open('numbers.txt', 'r')
#     for i_line in numbers_files:
#         nums_count += 1
#         nums_sum += int(i_line)
#     numbers_files.close()
#     print("Среднее арифметическое:", nums_sum / nums_count)
# except FileNotFoundError:
#     print("Такого файла не существует")
# except ValueError:
#     print("Нельзя преобразовать данные в целое число")
# ---------------------------------------------------------------------------------------------------------------------
#
# def divide(number):
#     return 10 / number
#
# def sum_of_divided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
#             div_sum += divide(i_num)
#             print(div_sum)
#         except ZeroDivisionError:
#             print("На ноль делить нельзя")
#     return div_sum
#
# total = 0
#
# try:
#     numbers_file = open("numbers.txt", 'r')
#     for i_line in numbers_file:
#         nums_list = i_line.split()
#         first_num = int(nums_list[0])
#         second_num = int(nums_list[1])
#
#         total += sum_of_divided(first_num, second_num)
#     print("Общая сумма:", total)
#
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# -----------------------------------------------------------------------------------------------------------------------
#
# В курсе по программированию студенту дали простую задачу: умножить константу (число 42) на пятый элемент строки,
# введённой пользователем. Вот код студента:
#
# BRUCE_WILLIS = 42
#
# input_data = input('Введите строку: ')
# leeloo = int(input_data[4])
# result = BRUCE_WILLIS * leeloo
# print(f'- Leeloo Dallas! Multi-pass № {result}!')
#
# Модифицируйте этот код, обработав исключения для произвольных входных параметров:
#
# ValueError — невозможно преобразовать к числу,
# IndexError — выход за границы списка,
# остальные исключения.
# Для каждого типа исключений выведите на консоль соответствующее сообщение.
#
# BRUCE_WILLIS = 42
#
# input_data = input('Введите строку: ')
# try:
#     leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * leeloo
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except ValueError:
#     print("невозможно преобразовать к числу")
# except IndexError:
#     print("выход за границы списка")
# except:
#     print("остальные исключения")
# ----------------------------------------------------------------------------------------------------------------------
#
# def divide(number):
#     return 10 / number
#
# def sum_of_divided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
#             div_sum += divide(i_num)
#             print(div_sum)
#         except ZeroDivisionError:
#             print("На ноль делить нельзя")
#     return div_sum
#
# total = 0
#
# try:
#     numbers_file = open("numbers.txt", 'r')
#     for i_line in numbers_file:
#         nums_list = i_line.split()
#         first_num = int(nums_list[0])
#         second_num = int(nums_list[1])
#
#         total += sum_of_divided(first_num, second_num)
#     print("Общая сумма:", total)
#
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
#
# answer_file = open('answer.txt', 'w')
# try:
#     answer_file.write("The answer is: ")
#     answer_file.write(str(total))
# except TypeError:
#     print("Ошибка записи в файл: тип данных не строка")
# else:                                              # выполняется если не было ошибок
#     print("Программа выполнилась без ошибок")
# finally:                                           # выполняется в любом случае
#     answer_file.close()
#     print(answer_file.closed)
# ----------------------------------------------------------------------------------------------------------------------
#В базе данных одной компании есть баг (или, может быть, фича): если ввести туда имя сотрудника меньше чем из трёх букв,
# то база сломается и упадёт. Как компания принимает на работу людей, например, с китайскими именами, непонятно.
# Дан файл people.txt, в котором построчно хранится N имён пользователей.
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка, и программа завершается.
#
# sym_sum = 0
# line_count = 0
# try:
#     with open('people.txt', 'r') as people_file:   # безопасное открытие файла, такой способ не требует прописывать функцию закрытия файла
#         for i_line in people_file:
#             length = len(i_line)
#             line_count += 1
#             if i_line.endswith('\n'):
#                 length -= 1
#             if length < 3:
#                 raise BaseException(f"Длинна строки {line_count} меньше 3 символов")
#             sym_sum += length
# except FileNotFoundError:
#     print("Файл не найден")
# finally:
#     print("Найденная сумма символов:", sym_sum)
# ----------------------------------------------------------------------------------------------------------------------
#
# names_list = []
#
# while True:
#     try:
#         name = input("Введите имя: ")
#         if name.lower() == 'error':
#             raise BaseException('Ты сломал программу')
#         if not name.isalpha():
#             raise TypeError
#         names_list.append(name)
#         if len(names_list) == 5:
#             print("Место закончилось")
#             break
#     except TypeError:
#         print("Ты чего ввел?")
#     except BaseException:
#         names_list = []
#         print("Введено стоп-слово")
#         raise ValueError("Пожалуйста не вводите стоп-слово")
#
# names_file = open('names.txt', 'w')
# names_file.write('\n'.join(names_list))
# names_file.close()
# print("Программа закончена, запись завершена")
# ----------------------------------------------------------------------------------------------------------------------
#
# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек,
# то есть программа может работать одновременно для нескольких пользователей.
# При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
# Посмотреть текущий текст чата.
# Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.
# Примечание: для решения задачи вам будет достаточно текущих знаний, нужно лишь проявить немного фантазии и хитрости.
# Не нужно лезть в дебри работы с сетями, создания GUI-приложений и прочих штук.
# (Но если очень хочется, то останавливать вас никто не будет!)

user_name = input("Введите ваше имя: ")
while True:
    print("Чтобы увидеть текст чата введите 1, чтобы написать сообщение введите 2")
    response = input("Введите 1 или 2: ")
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print("Служебное сообщение: пока ничего нет\n")
    elif response == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a') as file:
            file.write(f"{user_name}: {new_message}\n")
    else:
        print("Неизвестная команда\n")