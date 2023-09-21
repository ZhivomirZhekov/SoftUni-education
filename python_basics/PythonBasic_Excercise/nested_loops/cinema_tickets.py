student_tickets = 0
standard_tickets = 0
kid_tickets = 0

movie_name = input()
while movie_name != 'Finish':
    free_seats = int(input())
    sold_seats = 0
    for free_ticket in range(free_seats):
        type_ticket = input()
        if type_ticket == 'End':
            break
        elif type_ticket == 'student':
            student_tickets += 1
        elif type_ticket == 'standard':
            standard_tickets += 1
        elif type_ticket == 'kid':
            kid_tickets += 1
        sold_seats += 1
    percent_full = sold_seats / free_seats * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    movie_name = input()
total_sold_tickets = standard_tickets + student_tickets + kid_tickets
percent_standard = standard_tickets / total_sold_tickets * 100
percent_student = student_tickets / total_sold_tickets * 100
percent_kid = kid_tickets / total_sold_tickets * 100
print(f"Total tickets: {total_sold_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
