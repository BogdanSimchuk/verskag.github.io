from random import random
numbers = []
for g in range(10):
    numbers.append(int(random()*10))

print(numbers)

summ_positive = 0
for number in numbers:
    if number < 0:
      continue
    summ_positive = summ_positive + number
print('Сумма додатніх  ', summ_positive)

summ_negative = 0
for number in numbers:
    if number > 0:
        continue
    summ_negative = summ_negative + number
print('Сумма від*ємних ', summ_negative)
