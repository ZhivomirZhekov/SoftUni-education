password = input()

while True:
    command = input().split(" ")
    action = command[0]
    if action == "Done":
        break

    if action == "TakeOdd":
        password = password[1::2]
        print(password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring_to_remove = password[index:index + length]
        password = password.replace(substring_to_remove , "" , 1)
        print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring , substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
