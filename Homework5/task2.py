# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# вариант человек против человека:

from random import randint

def input_count(name):
    n = int(input(f"{name}, введите количество конфет от 1 до 28:\n "))
    while n < 1 or n > 28:
        n = int(input("Введите количество от 1 до 28:\n "))
    return n


def res_print(name, n, value):
    print(f"{name} взял {n} конфет. На столе осталось {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = 2021
flag = randint(0, 2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

while value > 28:
    if flag:
        n = input_count(player1)
        value -= n
        flag = False
        res_print(player1, n, value)
    else:
        n = input_count(player2)
        value -= n
        flag = True
        res_print(player2, n, value)

if flag:
    print(f"Победа! Выиграл {player1}!")
else:
    print(f"Победа! Выиграл {player2}!")

    