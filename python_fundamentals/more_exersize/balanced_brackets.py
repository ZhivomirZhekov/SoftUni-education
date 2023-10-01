number_lines = int(input())
bracket_counter = 0
for line in range(number_lines):
    string = input()
    if '(' in string:
        bracket_counter += 1
    elif ')' in string:
        bracket_counter -= 1

    if bracket_counter != 0 and bracket_counter != 1:
        print('UNBALANCED')
        break
else:
    print('BALANCED')

