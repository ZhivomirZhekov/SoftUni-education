# Input
product = input()

# Logic
if 'banana' == product or product == 'apple' or product == 'kiwi' or product == 'cherry' or product == 'lemon' \
        or product == 'grapes':
    print(f'fruit')
elif product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot':
    print(f'vegetable')
else:
    print(f'unknown')
