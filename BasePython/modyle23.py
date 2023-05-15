# import os
#
# folder_name = "project"
# file_name = "my_file.txt"
#
# rel_path = os.path.join("docs", folder_name, file_name) #Относительный путь файла
# print(rel_path)
#
# abs_path = os.path.abspath(file_name) #Абсолютный путь файла
# print(abs_path)
# -------------------------------------------------------------------------------------------------------------------
#
# import os
#
# def print_dirs(project):
#     print(f"\nСодержимое дериктории: {project}")
#     for i_elem in os.listdir(project):
#         path = os.path.join(project, i_elem)
#         print('    ', path)
#
# projects_list = ['Skillbox']
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join('..', i_project))
#     print_dirs(path_to_project)
# ----------------------------------------------------------------------------------------------------------------------
#
# Вы работаете системным администратором в одной компании.
# На диске каждого сотрудника компании в специальной папке access лежит файл admin.bat.
# Этот файл предназначен для вас, и вам нужен путь до этого файла, причём как относительный, так и абсолютный.
# Недолго думая, вы решили написать небольшой скрипт, который закинете по сети к этому файлу.
# Напишите программу, которая выводит на экран относительный и абсолютный пути до файла admin.bat.
#
# Пример результата:
# Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
# Относительный путь до файла: Skillbox\access\admin.bat
#
# import os
#
# file_name = 'admin.bat'
# folder_name = 'access'
#
# rel_path = os.path.join(folder_name, file_name)
# abs_path = os.path.abspath(os.path.join(folder_name, file_name))
#
# print(rel_path)
# print(abs_path)
# ---------------------------------------------------------------------------------------------------------------------
#
# Поиск файла
#
# import os
#
# def find_file(cur_path, file_name):
#     print(f"Переходим {cur_path}")
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print(f"    Смотрим {path}")
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#             print("Это дериктория")
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
# file_path = find_file(os.path.abspath(os.path.join('..', 'Skillbox')), 'modyle5.py')
# if file_path:
#     print(f"Абсолютный путь к файлу: {file_path}")
# else:
#     print("Файл не найден")
# ----------------------------------------------------------------------------------------------------------------------
#
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его диска:
# папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.
# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь
# (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение.
# Если путь указывает на файл, то также выведите его размер (сколько он весит в байтах).
# Обеспечьте контроль ввода: проверка пути на существование.
# Подсказка: для вывода размера файла поищите соответствующий метод.
# Пример 1:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Это файл
# Размер файла: 605 байт
# Пример 2:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Указанного пути не существует
#
# import os
#
# path = input("Путь: ")
#
# if os.path.isdir(path):
#     print("Это дериктория")
# elif os.path.islink(path):
#     print("Это ссылка")
# elif os.path.isfile(path):
#     print("Это файл")
#     large = os.path.getsize(path)
#     print(f"Размер файла: {large} байт")
# else:
#     print("Указанного пути не существует")
# ---------------------------------------------------------------------------------------------------------------------
#
# Вывод на экран содержимого файла
#
# speakers_file = open('speakers.txt', 'r', encoding='utf-8') # 'r' - это символ означающий read - режим чтения
# # data = speakers_file.read() #Один вариант открытия файла
# # print(data)
# for i_line in speakers_file:  #Второй более правильный способ чтения данных файла
#     print(i_line, end='')
# speakers_file.close() #После работы с файлом его нужно закрыть, иначе другая программа не сможет открыть этот файл
# ---------------------------------------------------------------------------------------------------------------------
#
# Считаем из каких символов состоит файл и записываем эти данные в файл
#
# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# sym_count = []
# for i_line in speakers_file:
#     print(i_line, end='')
#     sym_count.append(str(len(i_line)))
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
#
# counts_file = open('sym_count.txt', 'w') # w - это символ означает режим записи write
# counts_file.write(sym_count_str)
# counts_file.close() # Можно не создавать заранее файл. После запуска программы файл создается автоматически, но при повторном запуске данные файла перезаписываются. Чтобы он добавлял нужен режим 'a'.
# ----------------------------------------------------------------------------------------------------------------------
#
# Мало кто не знает о знаменитом романе Л. Н. Толстого «Война и мир». Это довольно объёмное произведение лежит в архиве voina-i-mir.zip.
# Напишите программу, которая подсчитывает статистику по буквам (не только русского алфавита) в этом романе и выводит результат на экран (или в файл).
# Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию). Регистр символов имеет значение.
# Постарайтесь написать программу так, чтобы для её работы не требовалась распаковка архива «вручную».

import collections
import zipfile

def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()

def collect_stats(file_name):
    result = {}
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    return result

def print_stats(stats):
    print("+{:-^19}+".format("+"))
    print("|{: ^9}|{: ^9}|".format('буква', 'частота'))
    print("+{:-^19}+".format("+"))
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format("+"))

def sort_by_frequenc(stats_dict):
    sorted_values = sorted(stats_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]

    return sorted_dict

file_name = 'voina-i-mir.zip'
stats = collect_stats(file_name)
stats = sort_by_frequenc(stats)
print_stats(stats)