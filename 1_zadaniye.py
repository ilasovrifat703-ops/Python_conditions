import math 


a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
x = int(input('Введите значение x: '))

if 3*b**2 > a:
    y = math.e**math.sin(x) + b
else:
    y = -(math.e)**(-x) + a*math.log10(x)

print(y)