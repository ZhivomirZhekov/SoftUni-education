key = int(input())
number_lines = int(input())
for line in range(number_lines):
    character = input()
    ascii_value = ord(character) + key
    print(chr(ascii_value), end="")

