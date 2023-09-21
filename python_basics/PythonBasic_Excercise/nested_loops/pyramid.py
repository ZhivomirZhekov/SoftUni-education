number = int(input())
counter = 1
is_printed = False
for row in range(1, number+1):
    for column in range(1, row+1):
        print(counter, end=' ')
        counter += 1
        if counter > number:
            is_printed = True
            break
    if is_printed:
        break
    print()
