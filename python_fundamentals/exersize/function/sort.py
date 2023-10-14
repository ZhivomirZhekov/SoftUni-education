def sorting_numbers(number):
    number = [int(x) for x in number]
    number = sorted(number)

    return number


numbers = input().split()
print(sorting_numbers(numbers))
