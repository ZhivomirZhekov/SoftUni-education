# Input
age = float(input())
sex = input()

# Logic
if age < 16:
    if sex == "m":
        print(f'Master')
    elif sex == 'f':
        print(f'Miss')
elif age >= 16:
    if sex == "m":
        print(f'Mr.')
    elif sex == 'f':
        print(f'Ms.')
