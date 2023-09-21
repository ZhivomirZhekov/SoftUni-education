number = int(input())
for current in range(1111, 9999+1):
    current_numb_string = str(current)
    is_special = True
    for current_digit in current_numb_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            is_special = False
            break
    if is_special:
        print(current_numb_string, end=' ')

