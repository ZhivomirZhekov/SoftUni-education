from typing import Tuple


def even_odd_sums(some_number : str) -> tuple[int , int]:
    sum_of_even = 0
    sum_of_odd = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_odd, sum_of_even


number = input()
sum_of_odd_digits, sum_of_even_digits = even_odd_sums(number)
print(f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}')
