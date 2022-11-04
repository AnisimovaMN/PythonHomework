# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

# запись в файл
def write_file(name, rec):
    with open(name, 'w') as data:
        data.write(rec)

# создание случайного числа от 0 до 100
def rnd():
    return random.randint(0, 101)

# создание коэффициентов многочлена
def create_coef(k):
    lst = [rnd() for i in range(k + 1)]
    return lst
    
# создание многочлена в виде строки 
def create_str(pol):
    lst = pol[::-1]
    parts = ''
    if len(lst) < 1:
        parts = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                parts += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    parts += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                parts += f'{lst[i]}x'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    parts += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                parts += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                parts += ' = 0'
    return parts

# получение степени многочлена
def degree_pol(k):
    if 'x^' in k:
        i = k.find('^')
        n = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        n = 1
    else:
        n = -1
    return n

# получение коэффицента члена многочлена
def coef_pol(k):
    if 'x' in k:
        i = k.find('x')
        n = int(k[:i])
    return n

# разбор многочлена и получение его коэффициентов
def calc_pol(rec):
    rec = rec[0].replace(' ', '').split('=')
    rec = rec[0].split('+')
    lst = []
    l = len(rec)
    k = 0
    if degree_pol(rec[-1]) == -1:
        lst.append(int(rec[-1]))
        l -= 1
        k = 1
    d = 1
    i = l - 1 
    while i >= 0:
        if degree_pol(rec[i]) != -1 and degree_pol(rec[i]) == d:
            lst.append(coef_pol(rec[i]))
            i -= 1
            d += 1
        else:
            lst.append(0)
            i += 1
    return lst
    
# создание двух файлов
k1 = int(input("Введите натуральную степень для первого файла k1: "))
k2 = int(input("Введите натуральную степень для второго файла k2: "))
coef1 = create_coef(k1)
coef2 = create_coef(k2)
write_file("file1_HW4.txt", create_str(coef1))
write_file("file2_HW4.txt", create_str(coef2))

# нахождение суммы многочлена
with open('file1_HW4.txt', 'r') as data:
    rec1 = data.readlines()
with open('file2_HW4.txt', 'r') as data:
    rec2 = data.readlines()
print(f"Первый многочлен {rec1}")
print(f"Второй многочлен {rec2}")

lst1 = calc_pol(rec1)
lst2 = calc_pol(rec2)
l1 = len(lst1)
if len(lst1) > len(lst2):
    l1 = len(lst2)
lst_res = [lst1[i] + lst2[i] for i in range(l1)]
if len(lst1) > len(lst2):
    l2 = len(lst1)
    for i in range(l1, l2):
        lst_res.append(lst1[i])
else:
    l2 = len(lst2)
    for i in range(l1, l2):
        lst_res.append(lst2[i])
write_file('file3_HW4.txt', create_str(lst_res))

with open('file3_HW4.txt', 'r') as data:
    rec3 = data.readlines()
print(f"Сумма многочленов {rec3}")