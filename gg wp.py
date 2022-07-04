from random import randint

numbers = {'a' : [], 'b' : [], 'c' : [], 'd' : []}

for i in list(numbers.keys()):
        numbers[i] = [randint(-10, 10) for x in range(4)]
print(numbers)
spisk=[]
result = sorted(numbers, key=numbers.get, reverse=True)[:1]
print(result)
max_value = [max(numbers, key=numbers.get), max(sum_values.values())]

for el in numbers.values():
    spisk.append(el)
print(sorted(spisk)[(len(spisk)-1):len(spisk)])

