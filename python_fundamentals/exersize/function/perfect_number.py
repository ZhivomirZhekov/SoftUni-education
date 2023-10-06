def perfect_or_not(some_number : int) -> str:
    sum_divisors = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            sum_divisors += divisor
    if sum_divisors == number:
        return 'We have a perfect number!'
    return "It's not so perfect."


number = int(input())
print(perfect_or_not(number))