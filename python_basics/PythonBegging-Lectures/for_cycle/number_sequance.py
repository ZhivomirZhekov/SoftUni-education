# Input
total_numbers = int(input())
biggest_number = 0
lowest_number = 0
# Logic
for i in range(total_numbers):
    number = int(input())
    if i == 0:
        biggest_number = number
        lowest_number = number
        
    if number > biggest_number:
        biggest_number = number
    elif number < lowest_number:
        lowest_number = number
# Output
print(f'Max number: {biggest_number}')
print(f'Min number: {lowest_number}')
