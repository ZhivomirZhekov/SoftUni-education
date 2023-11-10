string = input()
encrypted_message = ""
for char in string:
    character = ord(char) + 3
    encrypted_message += chr(character)
print(encrypted_message)
