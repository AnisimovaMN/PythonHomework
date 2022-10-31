# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# lst1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# lst1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# lst1 = ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# lst1 = ["123", "234", 123, "567"], ищем: "123", ответ: -1
# lst1 = [], ищем: "123", ответ: -1

# Способ 1
# from itertools import count
# test_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

# test_item = input("Введите искомую строку: ")

# def check_list(test_list, test_item):
#     count = 0
#     for i in range(len(test_list)):
#         if test_list[i] == test_item:
#             count += 1
#             if count == 2:
#                 return i
#     else:
#         return -1

# print(f'ответ: {check_list(test_list, test_item)}')

# Способ 2

lst1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
srch1 = "qwe"
lst2 =  ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
srch2 = "йцу"
lst3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
srch3 = "йцу"
lst4 = ["123", "234", 123, "567"]
srch4 = "123"
lst5 = []
srch5 = "123"

if srch1 in lst3:
    ind = lst3.index(srch3)
    for i in range(ind + 1, len(lst3)):
        if lst3[i] == srch3:
            print(i)
            break

    else:
        print(-1)
else:
    print(-1)