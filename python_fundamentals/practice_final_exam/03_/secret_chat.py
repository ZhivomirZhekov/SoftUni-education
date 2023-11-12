def insert_space(string: str , _index: int) -> str:
    left_side = string[:_index]
    right_side = string[_index:]
    string = left_side + " " + right_side
    return string


def reverse(string: str , string_to_reverse: str , _is_reversed: bool):
    if string_to_reverse in string:
        reversed_string = string_to_reverse[::-1]
        string = string.replace(string_to_reverse , "" , 1)
        string = string + reversed_string
    else:
        print("error")
        _is_reversed = False
    return string , _is_reversed


def change_all(string: str , string_to_replace: str , replacement_string: str) -> str:
    if string_to_replace in string:
        string = string.replace(string_to_replace , replacement_string)
    return string


concealed_message = input()
while True:
    instruction = input().split(":|:")
    if instruction[0] == "Reveal":
        break
    if instruction[0] == "InsertSpace":
        index = int(instruction[1])
        concealed_message = insert_space(concealed_message , index)

    elif instruction[0] == "Reverse":
        is_reversed = True
        substring = instruction[1]
        concealed_message , is_reversed = reverse(concealed_message , substring , is_reversed)
        if not is_reversed:
            continue
    elif instruction[0] == "ChangeAll":
        substring = instruction[1]
        replacement = instruction[2]
        concealed_message = change_all(concealed_message , substring , replacement)
    print(concealed_message)
print(f"You have a new text message: {concealed_message}")
