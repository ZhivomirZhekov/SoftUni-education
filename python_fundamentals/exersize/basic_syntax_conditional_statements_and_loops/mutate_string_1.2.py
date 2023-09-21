string_1 = input()
string_2 = input()
last_printed_string = string_1
for index in range(len(string_2)):
    left_side = string_2[:index+1]
    right_side = string_1[index+1:]
    new_string = left_side + right_side
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string
    