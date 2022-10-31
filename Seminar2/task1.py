# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

#  Пример:

# Для N = 5: 1, -3, 9, -27, 81

N = int(input('Введите число N: '))
num_list = [1]
for i in range(N - 1):
    num_list.append(num_list[i] * (-3))
print(*num_list, sep=', ')


N = int(input('N: '))
print(*(-3) ** i for i in range(int(input('N: '))), sep=', ')


n = int(input(('enter range')))
for i in range(n):
    print((-3)** i, end=' ')