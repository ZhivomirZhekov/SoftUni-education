def flip(raw_key , upper_or_lower , start_index , end_index):
    old_string = raw_key[start_index:end_index]
    if upper_or_lower == "Upper":
        new_string = old_string.upper()
    else:
        new_string = old_string.lower()
    raw_key = raw_key.replace(old_string , new_string)
    print(raw_key)
    return raw_key


def slice_instruction(raw_key: str , start_index , end_index):
    characters_to_delete = raw_key[start_index:end_index]
    raw_key = raw_key.replace(characters_to_delete , '')
    print(raw_key)
    return raw_key

def main_function():
    raw_key = input()
    command = input().split('>>>')
    while command[0] != 'Generate':
        instruction = command[0]
        if instruction == 'Contains':
            substring = command[1]
            if substring in raw_key:
                print(f"{raw_key} contains {substring}")
            else:
                print("Substring not found!")
        elif instruction == "Flip":
            upper_or_lower = command[1]
            start_index = int(command[2])
            end_index = int(command[3])
            raw_key = flip(raw_key , upper_or_lower , start_index , end_index)
        elif instruction == "Slice":
            start_index = int(command[1])
            end_index = int(command[2])
            raw_key = slice_instruction(raw_key , start_index , end_index)
        command = input().split('>>>')
    print(f"Your activation key is: {raw_key}")


main_function()
