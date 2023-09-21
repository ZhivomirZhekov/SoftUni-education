number_characters = int(input())
sum_of_characters_ascii = 0
for i in range(number_characters):
    character = input()
    sum_of_characters_ascii += ord(character)
print(f'The sum equals: {sum_of_characters_ascii}')
