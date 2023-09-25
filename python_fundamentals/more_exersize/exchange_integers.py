number_1 = int(input())
number_2 = int(input())
temporary_number_1 = number_1
temporary_number_2 = number_2
number_1 = number_2
number_2 = temporary_number_1
print(f'Before:\na = {temporary_number_1}\nb = {temporary_number_2}\nAfter:\na = {number_1}\nb = {number_2} ')
