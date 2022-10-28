# Вычислить число с заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10) 

from decimal import Decimal


n = input('Введите число: ')
d = input('Введите точность числа: ')
n = Decimal(n)
n = n.quantize(Decimal(d))

print(n)

