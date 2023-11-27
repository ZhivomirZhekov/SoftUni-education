def move(encrypted_message , number_of_letters):
    encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    return encrypted_message


def insert(encrypted_message , index , value):
    encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    return encrypted_message


def change_all(encrypted_message , substring , replacement):
    encrypted_message = encrypted_message.replace(substring , replacement)
    return encrypted_message


def main_function():
    encrypted_message = input()
    while True:
        command = input().split("|")
        if command[0] == "Decode":
            print(f"The decrypted message is: {encrypted_message}")
            break
        if command[0] == "Move":
            number_of_letters = int(command[1])
            encrypted_message = move(encrypted_message , number_of_letters)
        elif command[0] == "Insert":
            index , value = int(command[1]) , command[2]
            encrypted_message = insert(encrypted_message , index , value)
        elif command[0] == "ChangeAll":
            substring , replacement = command[1] , command[2]
            encrypted_message = change_all(encrypted_message , substring , replacement)


main_function()
