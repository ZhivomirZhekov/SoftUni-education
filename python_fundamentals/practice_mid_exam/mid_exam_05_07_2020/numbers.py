numbers = input().split()
numbers = [int(x) for x in numbers]
greater_than_average = []
average_number_in_numbers = sum(numbers) // len(numbers)
for number in numbers:
    if number > average_number_in_numbers:
        greater_than_average.append(number)
greater_than_average = sorted(greater_than_average, reverse=True)
greater_than_average = greater_than_average[:5]
greater_than_average = [str(x) for x in greater_than_average]
if len(greater_than_average) == 0:
    print('No')
else:

    print(' '.join(greater_than_average))
