def min_max_sum_of_numbers (number):
    number = [int(x) for x in number]
    min_number = min(number)
    max_number = max(number)
    sum_number = sum(number)
    return print(f'The minimum number is {min_number}\nThe maximum number is {max_number} \
           \nThe sum number is: {sum_number}')



numbers = input().split()
min_max_sum_of_numbers(numbers)