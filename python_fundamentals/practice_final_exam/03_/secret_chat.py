def insert_space(concealed_message: str , index):
    if 0 <= index < len(concealed_message):
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
    return concealed_message


def reverse(concealed_message , substring):
    if substring in concealed_message:
        reversed_substring = substring[::-1]
        concealed_message = concealed_message.replace(substring , reversed_substring , 1)
        print(concealed_message)
    else:
        print("error")
    return concealed_message


def change_all(concealed_message , substring , replacement):
    if substring in concealed_message:
        concealed_message = concealed_message.replace(substring , replacement)
    return concealed_message


def main_function():
    concealed_message = input()
    while True:
        command = input().split(":|:")
        action = command[0]
        if action == "Reveal":
            break

        if action == "InsertSpace":
            index = int(command[1])
            concealed_message = insert_space(concealed_message , index)
            print(concealed_message)
        elif action == "Reverse":
            substring = command[1]
            concealed_message = reverse(concealed_message , substring)

        elif action == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            concealed_message = change_all(concealed_message , substring , replacement)
            print(concealed_message)
    print(f"You have a new text message: {concealed_message}")


main_function()
