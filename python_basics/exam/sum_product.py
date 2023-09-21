n = int(input())
is_found = False
number = 0
for a in range(1, 9):
    if is_found:
        break
    for b in range(9, a, -1):
        if is_found:
            break
        for c in range(9):
            if is_found:
                break
            for d in range(9, c, -1):
                if a+b+c+d == a*b*c*d and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    is_found = True
                    break
                elif (a*b*c*d) // (a+b+c+d) == 3 and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    is_found = True
                    break

if not is_found:
    print("Nothing found")