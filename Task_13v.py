import random

days = int(input('Введите количество дней: '))
max_count = 0 # максимальное количество + температур
counter = 0
for _ in range(days):
    t = random.randint(-50, 50)
    print(t, end = ' ')
    if t > 0:
        counter += 1
    else:
        if counter > max_count:
            max_count = counter
        counter = 0
if counter > max_count:
    max_count = counter
print()
print(f'{max_count = }')