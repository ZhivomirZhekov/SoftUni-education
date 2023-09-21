# Input
number_pairs = int(input())
value_1 = 0
value_2 = 0
max_diff = 0
diff = 0
# Logic
for i in range(number_pairs):
    number_a = int(input())
    number_b = int(input())
    value_compare = number_a + number_b
    if i == 0:
        value_1 = value_compare
        value_2 = value_compare
    elif i != 0:
        if value_1 == value_compare:
            pass
        elif value_1 != value_compare:
            value_1 = value_2
            value_2 = value_compare
            diff = abs(value_1 - value_2)
            if max_diff < diff:
                max_diff = diff
# Output
if max_diff != 0:
    print(f"No, maxdiff={max_diff}")
else:
    print(f'Yes, value={value_1}')

