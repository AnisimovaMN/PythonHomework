# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#  Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = [3, 5, 4, 6, 2]
lst = []
for i in range(len(list) + 1 // 2):
    lst.append(list[i] * list[len(list) - i - 1])

print(lst)