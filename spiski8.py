n = int(input('Введите число - '))  

b = []

for i in range(n):
    a = int(input('Число '))
    b.append(a)

del b[1::2]

print(b)