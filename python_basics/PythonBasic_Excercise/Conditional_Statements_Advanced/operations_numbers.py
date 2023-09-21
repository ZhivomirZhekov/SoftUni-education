# Input
number_1 = int(input())
number_2 = int(input())
operator = input()
result = 0
even_or_odd = ''
# Logic
if operator == '+':
    result = number_1 + number_2
    if result % 2 ==0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
elif operator == '-':
    result = number_1 - number_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
elif operator == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
elif operator == '/' and number_2 != 0:
    result = number_1 / number_2
elif operator == '%' and number_2 != 0:
    result = number_1 % number_2



# Output

if operator == '+' or operator == '-' or operator == '*':
    print(f"{number_1} {operator} {number_2} = {result} - {even_or_odd}")
elif operator == '/' and number_2 != 0:
    print(f"{number_1} / {number_2} = {result:.2f}" )
elif operator == '%' and number_2 != 0:
    print(f"{number_1} % {number_2} = {result}")
elif number_2 == 0:
    print(f'Cannot divide {number_1} by zero')
