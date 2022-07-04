from random import randint
import random
n = 10


while n >= 1:
    if n >= 1:
        print('Всього сірників:', n)
        print('Хід Дениса')
        a = int(random.randint(1, 3))
        n = n -a
        if n <=0:
            break
        print('Всього сірників:', n)
        print('Хід Андрія')
        b = int(random.randint(1, 3))
        n = n - b

print('↑↑↑↑↑Нажаль це була поразка ')
print('Спробуєш знову?')
