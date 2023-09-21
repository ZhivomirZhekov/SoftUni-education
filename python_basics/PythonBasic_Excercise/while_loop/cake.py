# Input
width_cake = int(input())
length_cake = int(input())
cake_area = width_cake * length_cake
one_peace = 1
# Logic
while True:
    pieces = input()
    if pieces == 'STOP':
        print(f"{cake_area} pieces are left." )
        break
    cake_area -= int(pieces)
    if cake_area < 0:
        print(f"No more cake left! You need {abs(cake_area)} pieces more.")
        break
