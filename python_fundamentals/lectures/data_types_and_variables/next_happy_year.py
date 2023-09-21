year = int(input())
is_happy = False
while not is_happy:
    year += 1
    year_as_string = str(year)
    is_happy = True
    for digit in year_as_string:   # for digit in range(len(year_as_string)):
        if year_as_string.count(digit) > 1:     # if year_as_string.count(year_as_string[digit]) > 1:
            is_happy = False
            break
print(year)
