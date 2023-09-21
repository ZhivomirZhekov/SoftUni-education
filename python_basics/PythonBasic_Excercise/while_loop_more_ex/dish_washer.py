bottles_detergent = int(input())
qty_detergent = bottles_detergent * 750
counter = 1
dishes = 0
pots = 0
while True:
    if qty_detergent < 0:
        print(f"Not enough detergent, {abs(qty_detergent)} ml. more necessary!")
        break
    number = input()
    if number != 'End' and qty_detergent >= 0:
        if counter % 3 != 0:
            qty_detergent -= int(number) * 5
            dishes += int(number)
            counter += 1
        else:
            qty_detergent -= int(number) * 15
            pots += int(number)
            counter += 1

    elif number == 'End':
        print("Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {qty_detergent} ml.")
        break
