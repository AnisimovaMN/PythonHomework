# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4 + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

import random

# запись в файл
def write_file(rec1):
    with open('file1_HW4.txt', 'w') as data:
        data.write(rec1)

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
                if lst[i + 1] != 0:
                    parts += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                parts += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    parts += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                parts += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                parts += ' = 0'
    return parts

k = int(input("Введите натуральную степень k: "))
coef = create_coef(k)
write_file(create_str(coef))

with open('file1_HW4.txt', 'r') as data:
    rec1 = data.readlines()
print(f"Запись многочлена {rec1}")