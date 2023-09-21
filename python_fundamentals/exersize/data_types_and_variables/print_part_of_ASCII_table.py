first_char_ascii = int(input())
last_char_ascii = int(input())
for letter in range(first_char_ascii, last_char_ascii + 1):
    character = chr(letter)
    print(character, end=' ')
