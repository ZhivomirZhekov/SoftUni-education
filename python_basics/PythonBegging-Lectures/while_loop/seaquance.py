# Input
number = int(input())
number_k = 1
# Logic
while True:

    if number_k > number:
        break
    else:
        print(number_k)
        number_k = 2 * number_k + 1
