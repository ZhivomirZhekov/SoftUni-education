# Input
n = int(input())
# Logic
left_sum = 0
right_sum = 0
for i in range(n):
        left = int(input())
        left_sum += left
for i in range(n):
        right = int(input())
        right_sum += right
# Output
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')