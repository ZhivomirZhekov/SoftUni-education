number_n = int(input())
for number in range(1, number_n+1):
    number_as_string = str(number)
    sum_of_digits = 0
    is_special = False
    for digit in range(len(number_as_string)):
        sum_of_digits += int(number_as_string[digit])
        if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
            is_special = True
    print(f'{number} -> {is_special}')
