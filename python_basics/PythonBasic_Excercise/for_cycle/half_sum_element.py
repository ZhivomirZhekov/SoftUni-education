# Input
n = int(input())
first_num = int(input())
sum_numb = 0
max_numb = first_num
sum_numb += first_num
# Logic

for i in range(n-1):
    numb = int(input())
    sum_numb += numb
    if numb > max_numb:
        max_numb = numb

if max_numb == sum_numb - max_numb:
    print("Yes")
    print(f'Sum = {max_numb}')
else:
    diff = abs(max_numb - (sum_numb - max_numb))
    print('No')
    print(f'Diff = {diff}')