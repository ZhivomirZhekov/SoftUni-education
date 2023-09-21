low_range = int(input())
high_range = int(input())
magic_number = int(input())
counter = 0
is_true = False
for x1 in range(low_range,high_range+1):
    if is_true:
        break
    for x2 in range(low_range, high_range+1):
        counter += 1
        if x1 + x2 == magic_number:
            print(f"Combination N:{counter} ({x1} + {x2} = {magic_number})")
            is_true = True
            break
if not is_true:
    print(f"{counter} combinations - neither equals {magic_number}")
