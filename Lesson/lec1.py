#print('hello world')

# Типы данных и переменная
# int, float, boolean? str? list, None
# value = None
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334

#s = "hello 'world"
# s = 'hello "world'
# s = 'hello \'world'
# s = 'hello \nworld' # переход на новую строку

# print(s) # вывод строки
# print(a, '-', b, '-' , s)
# print('{} - {} - {}'.format(a, b, s))
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

#f = True
# f = False
# print(f)

# list = []
#list = [1, 2, 3]
#list = ['1', '2', '3', 'hello', 1,2,4.5,True]
# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# Ввод и вывод данных. Преобразование типов.
# print, input

# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
#print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print('Введите а');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a, '+' , b, ' = ', a+b)

# print('Введите а');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+' , b, ' = ', a+b)

# Арифметические операции
# +, -, *, /, %, //, **
# **, o+, o-, *, /, //, %, +, -
# (), Сокращенные операции

# a = 123
# b = -321
# c=a+b
# print(c)

# a = 2
# b = 8
# c=a-b
# print(c)

# a = 2
# b = 8
# c=a*b
# print(c)

# a = 2
# b = 8
# c=a/b
# print(c)

# a = 12
# b = 8
# c=a//b
# print(c)

# a = 12
# b = 8
# c=a % b
# print(c)

# a = 2
# b = 8
# c=a ** b
# print(c)

# a = 1.312312
# b = 3
# c = round(a * b, 5)
# print(c)

# a = 3
# a += 5
# a *= 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

#a = 1 < 4 and 5 > 2
# a = 1 == 2
# print(a)

# a = 'qwe'
# b = 'qwe'
#print(a == b)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2

# print(func<T>x)

# f = 1 > 2 or 4 < 6
# print(f)

#f = [1,2,3,4]
#print(f)
#print(2 in f)
#print(not 2 in f)

# f = [1,2,3,4]
# is_odd = f[0] % 2 == 0
# print(is_odd)

# f = [1,2,3,4]
# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a = int(input('a ='))
# b = int(input('b ='))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя:')
# if username=='Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала вас Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted*10+(original%10)
#     original//=10
# print(inverted)

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted*10+(original%10)
#     original//=10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for 

# for i in 1,2,3,4,5:
#     print(i**2)

# list=[1,2,3,4,10,5]
# for i in list:
#     print(i)

# r=range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1, 4):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwe - rty':
#     print(i)


# text= 'съешь ещё этих мягких французских булок'


# help(text.istitle)

# print(len(text))            #39
# print('ещё' in text)        #True
# print(text.isdigit())       #False
# print(text.islower())       #True
# print(text.replace('ещё', 'ЕЩЁ'))  #

# for c in text:
#     print(c)

# text= 'съешь ещё этих мягких французских булок'

# print(text[0])                              #c
# print(text[1])                              #ъ
# # print(text[len(text)])                    # IndexError
# print(text[len(text)]-1)                   #к
# print(text[-5])                             #б
# print(text[:])                               #print(text)
# print(text[0:1])                              #съ
# print(text[len(text)-2:])                   #ок
# print(text[2:9])                         #ешь ещё
# print(text[6:-18])                     #ещё этих мягких
# print(text[0:len(text):6])              #сеикакл
# print(text[::6])                        #сеикакл
# text = text[2:9] + text[-5] + text[:2]        #...

# for c in text:
#     print(c)

# Списки: введение
## list = list




# numbers = [1, 2, 3, 4, 5]
# print(numbers)                             #[1, 2, 3, 4, 5]
# run = range (1, 6)
# print(type(run))
# numbers = list(run)
# print(type(numbers))

# print(numbers)                             #[1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                             #[10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)                               #[20, 4, 6, 8, 10]
#     print(numbers)                         #[10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)                             #red green blue

# for e in colors:
#     print(e*2)                    #red green bluered green blue

# colors.append('gray') #добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] #удалить элемент

#Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 2.3
# print(f(arg))
# print(type(f(arg)))


