# import random
#
# class RandomNumbers:
#     def __init__(self, limit):
#         self.__limit = limit
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__limit:
#             self.__counter += 1
#             return random.randint(0, 10)
#         else:
#             raise StopIteration
#
# my_iter = RandomNumbers(limit=3)
# for num in my_iter:
#     print(num)
# ----------------------------------------------------------------------------------------------------------------------
#
# class Fibonacci:
#     """ Итератор последовательности Фибаначчи из N элементов """
#
#     def __init__(self, number):
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         self.number = number
#
#     def __iter__(self):
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter > 1:
#             if self.counter > self.number:
#                 raise StopIteration()
#             self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
#
#         return self.cur_val
#
# fib_iterator = Fibonacci(10)
# for i_value in fib_iterator:
#     print(i_value)
# print(8 in fib_iterator)
# ----------------------------------------------------------------------------------------------------------------------

""" Реализация генератора """
def fibonacci(number):
    cur_val = 0
    next_val = 1
    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val

fib_seq = fibonacci(10)
for i_value in fib_seq:
    print(i_value)