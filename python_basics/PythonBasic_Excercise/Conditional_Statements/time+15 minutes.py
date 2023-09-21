# Input
hours = int(input())
minutes = int(input())

# Logic
minutes += 15
hours += minutes // 60
minutes %= 60

if hours >= 24:
    hours = 0



# Output

print(f'{hours}:{minutes:02d}')