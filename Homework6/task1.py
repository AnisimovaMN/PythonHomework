# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

# expr = input('Введите арифметическое выражение:') 
# num1 = int(expr[0])
# num2 = int(expr[2])
# op = expr[1]

# if op == '*':
#     result = num1 * num2
# elif op == '/' and num2 != 0:
#     result = num1 / num2
# elif op == '+':
#     result = num1 + num2
# elif op == '-':
#     result = num1 - num2
# print(result)


import re
 
actions = {
  "*": lambda num1, num2: str(float(num1) * float(num2)),
  "/": lambda num1, num2: str(float(num1) / float(num2)),
  "+": lambda num1, num2: str(float(num1) + float(num2)),
  "-": lambda num1, num2: str(float(num1) - float(num2))
}
 
priority_exp = r"\((.+?)\)"
action_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
  
def calc(expresion: str):
 
    while (match := re.search(priority_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), calc(match.group(1)))
 
    for symbol, action in actions.items():
        while (match := re.search(action_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
    return expresion
 
 
exp = input('Введите арифметическое выражение:')    
print(calc(exp))



