# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

from itertools import count

# Способ 1
# list = ['jjhggf23dd', 'gfde56tjk', 'ggd1dds']
# n = input('Введите искомое число: ')
# for i in list:
#     if n in i:
#         print("да, есть")
# else:
#     print("Отсутствует")

# Способ 2
# list = ['jjhggf23dd', 'gfde56tjk', 'ggd1dds']
# n = input('Введите искомое число: ')
# print("да" if n in "".join(list) else "нет")

# Способ 3
def second_enter(lst, fnd):
    count = 0
    for i in range(len(lst)):
        if lst[i] == fnd:
            count += 1
            if count == 2:
                return i
    return -1

lst = ["йцу", "фыв", "ячс", "цук", "йцукен"]
fnd = "йцу"

print(second_enter(lst, fnd))

