# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

txt = input("Введите текст через пробел:\n")  
res = list(filter(lambda x: not('а' in x and 'б' in x and 'в' in x), txt.split()))

print(' '.join(res))
