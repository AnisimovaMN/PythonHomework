# Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.

n = int(input('Введите  натуральное число: '))
lst = []
i = 2
if n > 1:
    while i <= n:
        if n % i == 0:
            while n % i == 0:
                lst.append(i)
                n //= i
                i = 2
        else:        
            i += 1
lst.append(1)

print(sorted(list(set(lst))))