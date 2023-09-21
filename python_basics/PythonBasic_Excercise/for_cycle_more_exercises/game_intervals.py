# Input
moves = int(input())
# Logic
result = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0
for i in range(moves):
    numbers = int(input())
    if 0 <= numbers < 10:
        result += numbers * 0.2
        from_0_to_9 += 1
    elif 10 <= numbers < 20:
        result += numbers * 0.3
        from_10_to_19 += 1
    elif 20 <= numbers < 30:
        result += numbers * 0.4
        from_20_to_29 += 1
    elif 30 <= numbers < 40:
        result += 50
        from_30_to_39 += 1
    elif 40 <= numbers <= 50:
        result += 100
        from_40_to_50 += 1
    else:
        result /= 2
        invalid_numbers += 1
# Output
percentage_0_to_9 = from_0_to_9 / moves * 100
percentage_10_to_19 = from_10_to_19 / moves * 100
percentage_20_to_29 = from_20_to_29 / moves * 100
percentage_30_to_39 = from_30_to_39 / moves * 100
percentage_40_to_50 = from_40_to_50 / moves * 100
percentage_invalid = invalid_numbers / moves * 100
print(f'{result:.2f}')
print(f'From 0 to 9: {percentage_0_to_9:.2f}%')
print(f"From 10 to 19: {percentage_10_to_19:.2f}%")
print(f"From 20 to 29: {percentage_20_to_29:.2f}%")
print(f"From 30 to 39: {percentage_30_to_39:.2f}%")
print(f"From 40 to 50: {percentage_40_to_50:.2f}%")
print(f"Invalid numbers: {percentage_invalid:.2f}%")