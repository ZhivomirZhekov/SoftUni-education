string_input = input()

while True:
    command = input().split(" ")
    action = command[0]
    if action == "End":
        break

    if action == "Translate":
        char = command[1]
        replacement = command[2]
        string_input = string_input.replace(char , replacement)
        print(string_input)
    elif action == "Includes":
        true_or_false = False
        substring = command[1]
        if substring in string_input:
            true_or_false = True
        print(true_or_false)
    elif action == "Start":
        start_with_substring = command[1]
        true_or_false = False
        if string_input.startswith(start_with_substring):
            true_or_false = True
        print(true_or_false)
    elif action == "Lowercase":
        string_input = string_input.lower()
        print(string_input)
    elif action == "FindIndex":
        char = command[1]
        index = string_input.rindex(char)
        print(index)
    elif action == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        string_to_remove = string_input[start_index: start_index + count]
        string_input = string_input.replace(string_to_remove, "")
        print(string_input)