# Input

city = input()
sales = float(input())

commission = 0
correct_city = True
# Logic

if city == 'Sofia':
    if 0 <= sales <= 500:
        sales *= 0.05
    elif 500 <= sales <= 1000:
        sales *= 0.07
    elif 1000 <= sales <= 10000:
        sales *= 0.08
    elif sales > 10000:
        sales *= 0.12
    else:
        correct_city = False
elif city == 'Varna':
    if 0 <= sales <= 500:
        sales *= 0.045
    elif 500 <= sales <= 1000:
        sales *= 0.075
    elif 1000 <= sales <= 10000:
        sales *= 0.1
    elif sales > 10000:
        sales *= 0.13
    else:
        correct_city = False
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        sales *= 0.055
    elif 500 <= sales <= 1000:
        sales *= 0.08
    elif 1000 <= sales <= 10000:
        sales *= 0.12
    elif sales > 10000:
        sales *= 0.145
    else:
        correct_city = False
else:
    correct_city = False

# Output

if correct_city:
    print(f'{sales:.2f}')
else:
    print('error')
