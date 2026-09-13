x,y = map(float,input('Введите значения x и y через пробел: ').split())

def func(x,y):
    return True if (x**2 + y**2 <= 2**2 and x < 0) or (x**2 + y**2 > 1 and x**2 + y**2 <= 2**2 and x >= 0) else False

print(func(x,y))
