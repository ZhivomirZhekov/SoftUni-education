# Input
temperature = float(input())
# Logic
if 11.9 >= temperature >= 5:
    print(f'Cold')
elif 12 <= temperature <= 14.9:
    print(f'Cool')
elif 15 <= temperature <= 20:
    print(f'Mild')
elif 20.1 <= temperature <= 25.9:
    print(f'Warm')
elif 26 <= temperature <= 35:
    print(f'Hot')
else:
    print(f'unknown')