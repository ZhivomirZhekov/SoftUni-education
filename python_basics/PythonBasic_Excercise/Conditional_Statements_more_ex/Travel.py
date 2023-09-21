# Input
kilometers_n = int(input())
day_night = input()

# Logic
price = 0

if kilometers_n < 20:
    if day_night == 'day':
        price = 0.7 + kilometers_n * 0.79
    else :
        price = 0.7 + kilometers_n *0.9
elif kilometers_n >= 100:
    price = 0.06 * kilometers_n
else:
    price = 0.09 * kilometers_n

# Output
print(f'{price:.2f}')


