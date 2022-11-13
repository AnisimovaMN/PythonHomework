# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]


lst = list(map(int, input('Введите последовательность чисел через пробел: ').split()))

unique_numbers = list(set(lst))
print(unique_numbers)

dup_numbers = [i for i in set(lst) if lst.count(i) > 1]
print(dup_numbers)

without_dup_numbers = [i for i in set(lst) if lst.count(i) == 1]
print(without_dup_numbers)
