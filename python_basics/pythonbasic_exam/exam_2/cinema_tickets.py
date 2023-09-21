occupied_saloon = 0
total = 0
student = 0
standard = 0
kid = 0
is_finish = False
while True:
    if is_finish:
        break
    movie = input()
    if movie == 'Finish':
        break
    free_seats = int(input())
    occupied_saloon = 0
    for i in range(free_seats):
        type_ticket = input()
        if type_ticket == 'End':
            break
        occupied_saloon += 1
        total += 1
        if type_ticket == 'student':
            student += 1
        elif type_ticket == 'standard':
            standard += 1
        elif type_ticket == 'kid':
            kid += 1
    percent_occupied = occupied_saloon / free_seats * 100
    print(f"{movie} - {percent_occupied:.2f}% full.")
percent_student = student / total * 100
percent_standard = standard / total * 100
percent_kid = kid / total * 100
print(f"Total tickets: {total}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")