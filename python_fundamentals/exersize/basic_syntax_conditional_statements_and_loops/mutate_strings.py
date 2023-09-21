string_1 = input()
string_2 = input()
last_printed_string = string_1
for character_index in range(len(string_2)):
    left_part = string_2[:character_index+1]
    right_part = string_1[character_index+1:]
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string
