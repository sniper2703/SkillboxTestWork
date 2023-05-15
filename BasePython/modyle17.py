# Вашему другу, который тоже начал изучать Python, спикер дал следующие условия:
# есть три списка — основной и два побочных. В основном лежат элементы [1, 5, 3], а в побочных — [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно.
# Первый побочный закидывается в основной, в нём считается и выводится на экран количество цифр «5»,
# а затем они удаляются из основного списка. После этого в основной закидывается второй побочный список,
# в нём считается и выводится на экран количество цифр «3». В конце также выводится и сам список.
# Результат работы программы:
# Кол-во цифр 5 при первом объединении: 3
# Кол-во цифр 3 при втором объединении: 4
# Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]
#
# direct_list = [1, 5, 3]
# pob1_list = [1, 5, 1, 5]
# pob2_list = [1, 3, 1, 5, 3, 3]
#
# direct_list.extend(pob1_list)
# count = direct_list.count(5)
# print("Кол-во цифр 5 при первом объединении:", count)
# while count != 0:
#     direct_list.remove(5)
#     count -= 1
# direct_list.extend(pob2_list)
# print("Кол-во цифр 3 при втором объединении: ", direct_list.count(3))
# print("Итоговый список: ", direct_list)
# ----------------------------------------------------------------------------------------------------------------------
#
# Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево.
# Например, следующие последовательности являются симметричными:
# 1 2 3 4 5 4 3 2 1
# 1 2 1 2 2 1 2 1
# Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет,
# какое минимальное количество и каких чисел надо добавить в конец этой последовательности, чтобы она стала симметричной.
# Пример 1:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2
# Последовательность: [1, 2, 1, 2, 2]
# Нужно добавить чисел: 3
# Сами числа: [1, 2, 1]
# Пример 2:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 3
# Число: 4
# Число: 5
# Последовательность: [1, 2, 3, 4, 5]
# Нужно добавить чисел: 4
# Сами числа: [4, 3, 2, 1]

def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False

nums = [1, 2, 3, 4, 5]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print("Исходный список:", nums)
print("Нужно чисел для полиндрома:", len(answer))
print("Список этих чисел:", answer)