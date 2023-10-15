neighborhood = input().split('@')
neighborhood = [int(x) for x in neighborhood]
command = input().split()
jump_counter = 0
while command[0] != 'Love!':
    jump_counter += int(command[1])
    if jump_counter > len(neighborhood) - 1:
        jump_counter = 0
    if neighborhood[jump_counter] > 0:
        neighborhood[jump_counter] -= 2
        if neighborhood[jump_counter] == 0:
            print(f"Place {jump_counter} has Valentine's day.")
    elif neighborhood[jump_counter] == 0:
        print(f"Place {jump_counter} already had Valentine's day.")
    command = input().split()

print(f"Cupid's last position was {jump_counter}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    failed_houses = 0
    for house in range(len(neighborhood)):
        if neighborhood[house] != 0:
            failed_houses += 1
    print(f"Cupid has failed {failed_houses} places.")