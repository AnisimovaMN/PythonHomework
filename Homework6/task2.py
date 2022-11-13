# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]


# lst = list(map(int, input('Введите последовательность чисел через пробел: ').split()))

# unique_numbers = list(set(lst))
# print(unique_numbers)

# dup_numbers = [i for i in set(lst) if lst.count(i) > 1]
# print(dup_numbers)

# without_dup_numbers = [i for i in set(lst) if lst.count(i) == 1]
# print(without_dup_numbers)

with open('file_original.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = encode_rle(my_text)
print(str_code)

with open('file_encode.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
print(str_decode)