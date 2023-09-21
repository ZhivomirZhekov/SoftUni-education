compare_number = int(input())

while True:
    number = input()
    if number == 'Stop':
        print(compare_number)
        break
    else:
        if int(number) < compare_number:
            compare_number = int(number)