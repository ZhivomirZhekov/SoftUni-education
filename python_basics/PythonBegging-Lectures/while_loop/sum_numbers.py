# Input
total = int(input())
sum_total = 0
# Logic
while True:
    input_number = int(input())
    sum_total += input_number
    if sum_total >= total:
        print(sum_total)
        break

