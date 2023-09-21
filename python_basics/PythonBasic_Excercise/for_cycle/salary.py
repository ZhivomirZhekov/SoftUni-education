# Input
open_tab = int(input())
salary = float(input())

# Logic
for i in range(open_tab):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50
    if salary <= 0:
        break

# Output
if salary > 0:
    print(f'{int(salary)}')
else:
    print('You have lost your salary.')
