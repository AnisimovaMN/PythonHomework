# Файлы

# colors = ['red', 'green', 'blue123']
# data = open('file_1.txt', 'a')
# data.writelines(colors)
# data.close()

# exit()

# colors = ['red', 'green', 'blue123']
# data = open('file_1.txt', 'a')
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close()

# exit()

# with open('file_1.txt', 'a') as data:
#     data.write('line 1111\n')
#     data.write('line 2222\n')

# path = 'file_1.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# Функции и модули

# import lec1
# print(lec1.f(1))

# import lec1 as l
# print(l.f(1))

# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5))

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1', 'd', '2'))

# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4))

# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи

# from turtle import color


# t = ()
# print(type(t))

# t = (1,)
# print(type(t))

# t = (1)
# print(type(t))

# t = (28, 9, 1990)
# print(type(t))

# colors = ['red', 'green', 'blue']
# print(colors)

# t = tuple(colors)
# print(t)

# a = (3, 4)
# print(a)
# print(a[0])
# print(a[-1])

# a = (3, 4, 5)
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# print(t[0])
# print(t[2])
# print(t[-2])
# for e in t:
#     print(e)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))

# Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': '^',
#         'left': '<',
#         'down': 'v',
#         'right': '>'
#     }
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# for v in dictionary:
#     print(dictionary[v])

# dictionary['left'] = '<'
# print(dictionary['left'])
# del dictionary['left']

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# print(dictionary['up'])
# dictionary['up'] = 'up'
# print(dictionary['up'])


# Множества

# colors = {'red', 'green', 'blue'}
# print(type(colors))
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print('work')
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)
# print(c)
# print(u)
# print(i)
# print(dl)
# print(dr)

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)

# неизменяемые множества

# s = frozenset(a)

# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)

# for e in list2:
#     print(e)

# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)

# for e in list2:
#     print(e)


# list1 = [1, 2, 3, 4, 5]

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# list1 = [1, 2, 3, 4, 5]
# print(list1.pop(2))
# print(list1)

# list1 = [1, 2, 3, 4, 5]
# print(list1.insert(2, 11))
# print(list1)

list1 = [1, 2, 3, 4, 5]
print(list1.append(11))
print(list1)
