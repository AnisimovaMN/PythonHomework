# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

o = 1
for X in range(2):
    for Y in range(2):
        for Z in range(2):
            o *= (not(X or Y or Z) == (not X and not Y and not Z))
if o == 1:
    print(True)