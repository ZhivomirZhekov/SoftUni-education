def moving_zeros(list_as_string: list) -> list:
    for digits in list_as_string:
        if int(digits) == 0:
            list_as_string.remove(digits)
            list_as_string.append(digits)
    list_as_digits = []
    for digits in list_as_string:
        list_as_digits.append(int(digits))
    return list_as_digits


single_string = input().split(", ")
# for digit in single_string:
#     if int(digit) == 0:
#         single_string.remove(digit)
#         single_string.append(digit)
# list_as_a_digits = []
# for digit in single_string:
#     list_as_a_digits.append(int(digit))
print(moving_zeros(single_string))
