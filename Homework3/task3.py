# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

list = [1.1, 1.2, 3.1, 5, 10.01]
lst = []
for i in range(len(list)):
    lst.append((list[i] % 1))
    
print(round(max(lst) - min(lst), 2))