# Input
number = int(input())

# Logic
for i in range(number+1):
    if i % 2 == 0:
        even_power = 2 ** i
        print(f'{even_power}')