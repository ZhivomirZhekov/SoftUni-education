def is_even(number):
    return number % 2 == 0


numbers_as_string = input().split()
number_as_digits = []
for number in numbers_as_string:
     number_as_digits.append(int(number))
result = []
for element in number_as_digits:
    if is_even(element):
        result.append(element)
        # is_even = lambda x: x % 2 == 0
        # result = list(filter(is_even , number_as_digits))
print(result)