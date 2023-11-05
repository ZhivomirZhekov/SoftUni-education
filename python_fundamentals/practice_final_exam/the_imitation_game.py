def move(message: str , letters: int) -> str:
    left_message = message[:letters]
    right_message = message[letters:]
    message = right_message + left_message
    return message


def insert(message: str , position_index: int , value_char: str) -> str:
    left_message = message[:position_index]
    right_message = message[position_index:]
    message = left_message + value_char + right_message
    return message


def change_all(message: str , new_string: str , old_string: str) -> str:
    message = message.replace(old_string , new_string)
    return message


encrypted_message = input()

while True:
    command = input().split("|")
    if command[0] == 'Decode':
        break
    if command[0] == "Move":
        number_of_letter = int(command[1])
        encrypted_message = move(encrypted_message , number_of_letter)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = insert(encrypted_message , index , value)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = change_all(encrypted_message , replacement , substring)
print(f"The decrypted message is: {encrypted_message}")
