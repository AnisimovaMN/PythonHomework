# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


nums = input('Введите 5 чисел через пробел:').split()
max_num = int(nums[0])
for i in nums:
    if int(i) > max_num:
        max_num = int(i)
print(max_num)