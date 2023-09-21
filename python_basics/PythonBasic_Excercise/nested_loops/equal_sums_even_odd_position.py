number_1 = int(input())
number_2 = int(input())
for current_number in range(number_1, number_2+1):
    even_digits = 0
    odd_digits = 0
    current_number_str = str(current_number)
    for index,digit in enumerate(current_number_str):
        if index % 2 == 0:
            odd_digits += int(digit)
        else:
            even_digits += int(digit)
    if even_digits == odd_digits:
        print(current_number, end=' ')
        