def all_characters_between(first_char : str, last_char : str) -> list:
    characters = []
    for current_character in range(ord(first_char) + 1 , ord(last_char)):
        characters.append(chr(current_character))
    return characters


first_character = input()
second_character = input()
result = all_characters_between(first_character, second_character)
print(' '.join(result))

