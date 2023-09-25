number = int(input())
counter = 0
if number > 1:
    for i in range(2, number+1):
        if number % i == 0:
            counter += 1
        if counter > 1:
            print('False')
            break
        elif counter == 1 and i == number:
            print('True')
else:
    print('False')
