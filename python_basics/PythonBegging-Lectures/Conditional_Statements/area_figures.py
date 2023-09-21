# Input
from math import pi
figure = input()
area = 0
# Logic
if figure == 'square':
    a = float(input())
    area = a * a
    print(f'{area:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
elif figure == 'circle':
    r = float(input())
    area = pi*r*r
    print(f'{area:.3f}')
else:
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f'{area:.3f}')