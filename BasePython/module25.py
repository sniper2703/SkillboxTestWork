# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#
# user_1 = User() # экземпляр класса User
# ---------------------------------------------------------------------------------------------------------------------
#
# class Tayota:
#     color_car = 'Red'
#     price_car = 100000000
#     max_speed = 200
#     moment_speed = 0
#
# my_car = Tayota()
# dad_car = Tayota()
# mom_car = Tayota()
#
# mom_car.moment_speed = 100
# my_car.moment_speed = 150
# dad_car.moment_speed = 200
#
# print(Tayota.moment_speed, mom_car.moment_speed, my_car.moment_speed, dad_car.moment_speed) # 0 100 150 200
# ---------------------------------------------------------------------------------------------------------------------
#
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников.
# У монитора есть четыре характеристики: название производителя, матрица, разрешение и частота обновления экрана.
# Все четыре монитора отличаются только частотой.
#
# У наушников три характеристики: название производителя, чувствительность и наличие микрофона.
# Отличие только в наличии микрофона.
#
# class Monitor:
#     brend = 'Lg'
#     matrix = 'IPS'
#     res = 'QHD'
#     freq = 90
#
# class Headphones:
#     brend = 'Sony'
#     sensitivity = 108
#     micro = True
#
# monitor1 = Monitor()
# monitor2 = Monitor()
# monitor3 = Monitor()
# monitor4 = Monitor()
# headphones1 = Headphones()
# headphones2 = Headphones()
# headphones3 = Headphones()
#
# monitor1.freq = 60
# monitor2.freq = 144
# monitor3.freq = 165
# headphones1.micro = False
# print(monitor1.freq, monitor2.freq, monitor3.freq, monitor4.freq) # 60 144 165 90
# print(headphones1.micro, headphones2.micro, headphones3.micro) # False True True
# ----------------------------------------------------------------------------------------------------------------------
#
# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     friends = []
#
#     def print_info(self):
#         print("Name: {}\nPassword: {}\nBan status: {}\nFriends: {}".format(
#             self.user_name, self.password, self.is_banned, self.friends))
#
#     def add_friends(self, friend):
#         if isinstance(friend, User):
#             self.friends.append(friend.user_name)
#         else:
#             self.friends.append(friend)
#
#
# user_1 = User()
# user_2 = User()
# user_2.user_name = 'Alina'
# user_1.add_friends('Bob')
# user_1.add_friends(user_2)
# user_1.print_info()
# ----------------------------------------------------------------------------------------------------------------------
#
# Реализуйте класс «Семья», который состоит из атрибутов
# «Имя», Деньги» и «Наличие дома» и объекты которого могут выполнять следующие действия:
# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.
#
# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
#
# Family name: Common family
# Family funds: 100000
# Having a house: False
# Try to buy a house
# Not enough money!
# Earned 800000 money! Current value: 900000
# Try to buy a house again
# House purchased! Current money: 0.0
# Family name: Common family
# Family funds: 0.0
# Having a house: True
#
# class Family:
#     surname = 'Common family'
#     money = 100000
#     have_a_house = False
#
#     def info(self):
#         print(
#             'Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
#                 self.surname, self.money, self.have_a_house
#             )
#         )
#
#     def earn_money(self, amount):
#         self.money += amount
#         print('Earned {} money! Current value: {}'.format(amount, self.money))
#
#     def buy_house(self, house_price, discount=0):
#         house_price -= house_price * discount / 100
#         if self.money >= house_price:
#             self.money -= house_price
#             self.have_a_house = True
#             print('House purchased! Current money: {}\n'.format(self.money))
#         else:
#             print('Not enough money!\n')
#
# my_family = Family()
# my_family.info()
#
# print('Try to buy a house')
# my_family.buy_house(10 ** 6)
#
# if not my_family.have_a_house:
#     my_family.earn_money(800000)
#     print('Try to buy a house again')
#     my_family.buy_house(10 ** 6, 10)
#
# my_family.info()
# ----------------------------------------------------------------------------------------------------------------------
#
# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def print_info(self):
#         print(
#             'Name: {}\nSalary: {}'.format(self.name, self.salary)
#         )
#
# emp1 = Employee('Tom', 10000)
# emp2 = Employee('Bob', 20000)
# emp1.print_info()
# emp2.print_info()
# ----------------------------------------------------------------------------------------------------------------------
#
# Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс «Грядка картошки».
# У картошки есть её номер в грядке, а также стадия зрелости.
# Она может предоставлять информацию о своей зрелости и расти. Всего у картошки может быть четыре стадии зрелости.
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
# а также предоставлять информацию о зрелости всей картошки на своей территории.
# Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.
#
# Пример результата (проверка на зрелость и три взращивания):
# Картошка ещё не созрела!
# Картошка прорастает!
# Картошка 1 сейчас Росток
# Картошка 2 сейчас Росток
# Картошка 3 сейчас Росток
# Картошка 4 сейчас Росток
# Картошка 5 сейчас Росток
# Картошка ещё не созрела!
#
# Картошка прорастает!
# Картошка 1 сейчас Зелёная
# Картошка 2 сейчас Зелёная
# Картошка 3 сейчас Зелёная
# Картошка 4 сейчас Зелёная
# Картошка 5 сейчас Зелёная
# Картошка ещё не созрела!
#
# Картошка прорастает!
# Картошка 1 сейчас Зрелая
# Картошка 2 сейчас Зрелая
# Картошка 3 сейчас Зрелая
# Картошка 4 сейчас Зрелая
# Картошка 5 сейчас Зрелая
# Вся картошка созрела. Можно собирать!
#
# import module25_classes
#
# my_garden = module25_classes.PotatoGarden(5)
# my_garden.are_all_ripe()
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()
# ---------------------------------------------------------------------------------------------------------------------
#
# Вы работаете в команде разработчиков мобильной игры, и вам досталась такая часть от ТЗ заказчика:
#
# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
# Реализуйте такую программу.
#
# import random
# class Unit:
#
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health
#
#     def print_info(self):
#         print('Name: {}\nHealth: {}'.format(self.name, self.health))
#
#     def damage(self):
#         self.health -= 20
#
#
#
# unit1 = Unit('Bob')
# unit2 = Unit('Tom')
#
# print("Да начнется битва!")
# while True:
#     step = input("Введите 1, чтобы какой-то воин атаковал. Для закрытия программы введите 2: ")
#     if step == "1":
#         kick = random.randint(1, 3)
#         if kick == 1:
#             print(f'{unit1.name} атоковал!')
#             unit2.damage()
#             if unit2.health <= 0:
#                 print(f"{unit1.name} победил!")
#                 break
#             else:
#                 unit2.print_info()
#                 print()
#         else:
#             print(f'{unit2.name} атоковал!')
#             unit1.damage()
#             if unit1.health <= 0:
#                 print(f"{unit2.name} победил!")
#                 break
#             else:
#                 unit1.print_info()
#                 print()
#     elif step == "2":
#         print("Бой завершён!")
#         break
#     else:
#         print("Неверная команда!")
# ---------------------------------------------------------------------------------------------------------------------
#
# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать свои или запросить их у пользователя)
# и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.
#
# student_list = []
#
# class Student:
#     def __init__(self, name, num_group, academ):
#         self.name = name
#         self.num_group = num_group
#         self.academ = academ
#         self.mean = self.med_academ()
#
#     def med_academ(self):
#         summ = sum(self.academ)
#         mean = int(summ / len(self.academ))
#         return mean
#
#     def print_info(self):
#         print('Name: {}\nNum_group: {}\nacadem: {}\nmean: {}'.format(self.name, self.num_group, self.academ, self.mean))
#
#
# for _ in range(2):
#     name = input("Введите имя студента: ")
#     num_group = int(input("Введите номер группы: "))
#     academ = input("Введите через запятую пять оценок: ").split(",")
#     int_academ = list(map(int, academ))
#     student = Student(name, num_group, int_academ)
#     student_list.append(student)
#
# sort_list = sorted(student_list, key=lambda student: student.mean)
# print(sort_list[0].print_info())
# print(sort_list[1].print_info())
# ----------------------------------------------------------------------------------------------------------------------
#
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# Имя.
# Возраст.
# Список детей.
# И он может:
# Сообщить информацию о себе.
# Успокоить ребёнка.
# Покормить ребёнка.
# У ребёнка есть:
# Имя.
# Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
# Состояние спокойствия.
# Состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-нибудь ещё интереснее.
#
# class Child:
#     def __init__(self, name, old, calm=False, hungry=False):
#         self.name = name
#         self.old = old
#         self.calm = calm
#         self.hungry = hungry
#
#     def hungrys(self):
#         self.hungry = False
#
#     def print_info(self):
#         print('Name: {}\nOld: {}\nCalm: {}\nHungry: {}'.format(self.name, self.old, self.calm, self.hungry))
#
# class Parent:
#     def __init__(self, name, old, child_list):
#         self.name = name
#         self.old = old
#         self.child_list = child_list
#
#     def print_info(self):
#         print('Name: {}\nOld: {}\nChild_list: {}'.format(self.name, self.old, self.child_list))
#
#     def calm_child(self, child):
#         child.calm = True
#
#     def hung_child(self, child):
#         child.hungry = True
#
#
# child_list = [Child('Ann', 7), Child('Tom', 2)]
# alex = Parent('Alex', 30, child_list)
# alex.hung_child(child_list[0])
# child_list[0].print_info()
# child_list[0].hungrys()
# child_list[0].print_info()
# ---------------------------------------------------------------------------------------------------------------------
#
# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
# У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
# Из них как раз и получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
#
# Вот таблица преобразований:
# «Вода» + «Воздух» = «Шторм»
# «Вода» + «Огонь» = «Пар»
# «Вода» + «Земля» = «Грязь»
# «Воздух» + «Огонь» = «Молния»
# «Воздух» + «Земля» = «Пыль»
# «Огонь» + «Земля» = «Лава»
# Напишите программу, которая реализует все эти элементы.
# Каждый элемент необходимо организовать как отдельный класс. Если результат не определён, то возвращается None.
#
# Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:
#
# class Example_1:
#     def __add__(self, other):
#         return Example_2()
#
# class Example_2:
#     answer = 'сложили два класса и вывели'
#
# a = Example_1()
# b = Example_2()
# c = a + b
# print(c.answer)
#
# class Element:
#
#     def __init__(self, name):
#         if name in ("Вода", "Воздух", "Огонь", "Земля", "Шторм", "Грязь", "Пыль", "Лава", "Молния", "Пар"):
#             self.name = name
#         else:
#             raise ValueError
#
#     def __str__(self):
#         return "</" + self.name + "/>"
#
#     def __add__(self, other):
#         if set((self.name, other.name)) == set(("Вода", "Воздух")):
#             return Element("Шторм")
#         if set((self.name, other.name)) == set(("Вода", "Огонь")):
#             return Element("Пар")
#         if set((self.name, other.name)) == set(("Вода", "Земля")):
#             return Element("Грязь")
#         if set((self.name, other.name)) == set(("Воздух", "Огонь")):
#             return Element("Молния")
#         if set((self.name, other.name)) == set(("Воздух", "Земля")):
#             return Element("Пыль")
#         if set((self.name, other.name)) == set(("Огонь", "Земля")):
#             return Element("Лава")
#         raise ValueError
#
#
# e1 = Element("Огонь")
# e2 = Element("Земля")
# e3 = e1 + e2
# print(e1, "+", e2, "=", e3)
# -----------------------------------------------------------------------------------------------------------------------
