def calculate_factorial(number : int):
    for digit in range(1, number):
        number *= digit
    return number   # initial number factorial -> number!


first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_factorial(first_number)
second_number_factorial = calculate_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f'{result:.2f}')
