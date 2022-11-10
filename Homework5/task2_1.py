# вариант человек против бота:

from random import randint

def input_count(player):
    
    if player == player1:
        n = int(input(f"{player}, введите количество конфет от 1 до 28:\n "))
        while n < 1 or n > 28:
                n = int(input("Введите количество от 1 до 28:\n "))
        
    else:                 
        n = randint(1, 29)
    return n
      

def res_print(player, n, value):
    print(f"{player} взял {n} конфет. На столе осталось {value} конфет.")

player1 = input("Введите имя игрока: ")
player2 = "Бот"
value = 100
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
    print(f"Выиграл {player2}")