import math 


a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
x = float(input('Введите значение x: '))

if (a + 3 * b)**0.5 < (3 * x):
    y = a * x**2 + math.tan(4 * x)
else:
    y = (a + math.sin(abs(3 * x)))**0.5

print(y)
