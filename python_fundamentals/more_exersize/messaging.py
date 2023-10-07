# sequence_of_numbers = input().split()
# some_string = input()
# sum_of_digits_number = 0
# list_sum_of_numbers = []
# message = []
# some_string_as_list = []
# for char in some_string:
#     some_string_as_list.append(char)
# for number in sequence_of_numbers:
#     for digits in number:
#         sum_of_digits_number += int(digits)
#     list_sum_of_numbers.append(sum_of_digits_number)
#     sum_of_digits_number = 0
# for number in list_sum_of_numbers:
#     while number >= len(some_string):
#         number -= len(some_string_as_list)
#     message.append(some_string_as_list[number])
#     some_string_as_list.pop(number)
# message = ''.join(message)
# print(message)


sequence_of_numbers = input().split()
some_string = input()
message = ''
for numbers in sequence_of_numbers:
    char_index = 0
    for digit in numbers:
        char_index += int(digit)
    while char_index >= len(some_string):
        char_index -= len(some_string)
    message += some_string[char_index]
    some_string = some_string[:char_index] + some_string[char_index +1:]
print(message)