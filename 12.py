S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

found_solution = False
X = 1

while X <= 100:
    Y = S - X

    if X * Y == P:
        found_solution = True
        break

    X += 1

if found_solution:
    print("Задуманные числа:", X, Y)
else:
    print("Нет решения")
