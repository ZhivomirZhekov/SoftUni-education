# Input
type_movie = input()
number_row = int(input())
number_column = int(input())
total = 0

# Logic
premiere = 12
normal = 7.5
discount = 5
number_seats = number_row * number_column
if type_movie == 'Premiere':
    total = premiere * number_seats
elif type_movie == 'Normal':
    total = normal * number_seats
elif type_movie == 'Discount':
    total = discount * number_seats

# Output

print(f'{total:.2f} leva')
