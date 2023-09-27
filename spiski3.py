import random
 
n = int(input("Введите число - "))
a = [random.randint(0, 25) for _ in range(10)]

print(a)

if n in a:
    print(a.index(n))
else:
    print('-1')