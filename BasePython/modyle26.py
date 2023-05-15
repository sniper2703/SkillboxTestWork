# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв) и возрастом (должен быть в диапазоне от 0 до 100),
# а внутри класса считается общее количество инициализированных объектов.
# Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических),
# а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
#
# class Person:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.set_age(age)
#         Person.__count += 1
#
#     def __str__(self):
#         return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)
#
#     def get_count(self):         # Геттер
#         return self.__count
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):      # Сеттер
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception("Недопустимый возраст")
#
# misha = Person("Misha", 20)
# tom = Person("Tom", 25)
# print(misha.get_count())
# new_age = 80
# misha.set_age(new_age)
# print(misha.get_age())
# ---------------------------------------------------------------------------------------------------------------------
#
# class Pet:
#     legs = 4
#     has_tail = True
#
#     def __str__(self):
#         tail = 'да' if self.has_tail else 'нет'
#         return f"Всего ног: {self.legs}\nХвост присутствует - {tail}"
#
# class Cat(Pet):
#     def sound(self):
#         print("Мяу")
#
# class Dog(Pet):
#     def sound(self):
#         print("Гав")
#
# cat = Cat()
# print(cat)
# print(cat.sound())
# dog = Dog()
# print(dog)
# print(dog.sound())
# ----------------------------------------------------------------------------------------------------------------------
#
# Даны два класса кораблей — грузовой и военный.
# У каждого из этих кораблей есть своя модель, и каждый может сделать два действия: сообщить свою модель и идти по воде.
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю.
# У него есть ещё два действия: погрузить и выгрузить груз с корабля.
#
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью.
# Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.
#
# Реализуйте классы грузового и военного кораблей.
# Для этого выделите общие атрибуты и методы в отдельный класс «Корабль» и используйте наследование.
# Не забудьте про функцию super в дочерних классах.
#
# class Ship:
#     def __init__(self, model):
#         self.__model = model
#
#     def __str__(self):
#         return f"\nМодель корабля: {self.__model}"
#
#     def sail(self):
#         print("\nКорабль куда-то поплыл!")
#
# class WarShip(Ship):
#     def __init__(self, model, gun):
#         super().__init__(model)
#         self.gun = gun
#
#     def attack(self):
#         print('\nКорабль атакует с помощью оружия', self.gun)
#
# class CargoShip(Ship):
#     def __init__(self,model):
#         super().__init__(model)
#         self.tonnage_load = 0
#
#     def load(self):
#         print("\nЗагружаем корабль")
#         self.tonnage_load += 1
#         print("Текущая загруженность", self.tonnage_load)
#
#     def unload(self):
#         print("\nРазгружаем корабль")
#         if self.tonnage_load > 0:
#             self.tonnage_load -= 1
#         else:
#             print("Корабль уже разгружен!")
#         print("Текущая загруженность", self.tonnage_load")
# ----------------------------------------------------------------------------------------------------------------------
#
# Мы уже говорили, что в программировании нередко необходимо создавать свои собственные структуры данных на основе уже существующих.
# Одной из таких «базовых» структур является стек.
#
# Стек — это абстрактный тип данных, представляющий собой список элементов,
# организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
# Простой пример: стек из книг на столе. Единственной книгой, чья обложка видна, является самая верхняя.
# Чтобы получить доступ к, например, третьей снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.
#
# Напишите класс, который реализует стек и его возможности (достаточно будет добавления и удаления элемента).
# После этого напишите ещё один класс — «Менеджер задач».
# В менеджере задач можно выполнить команду «Новая задача», в которую передаётся сама задача (str) и её приоритет (int).
# Сам менеджер работает на основе стека (не наследование!).
# При выводе менеджера в консоль все задачи должны быть отсортированы по приоритету: чем меньше число, тем выше задача.
#
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать дз", 2)
# print(manager)
#
# Результат:
# 1 отдохнуть
# 2 поесть; сдать дз
# 4 сделать уборку; помыть посуду

class Stack:
    def __init__(self):
        self.__st = []

    def __str__(self):
        return '; '.join(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()

class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f"{str(i_priority)} {self.task[i_priority]}\n")
        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)