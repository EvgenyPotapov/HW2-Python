coins = input("Введите последовательность монеток (герб - 0, решка - 1): ")
count_heads = 0
count_tails = 0

for coin in coins:
    if coin == '0':
        count_heads += 1
    else:
        count_tails += 1

if count_heads < count_tails:
    count_flips = count_heads
else:
    count_flips = count_tails

print("Минимальное количество монет, которые нужно перевернуть:", count_flips)

