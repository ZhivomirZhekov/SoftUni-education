def char_position(letter):
    return ord(letter) - 96


string_input = input().split()
total_sum = 0
for string in string_input:
    string = string.strip()
    first_letter = string[0]
    number = int(string[1:len(string) - 1])
    last_letter = string[-1]
    if first_letter.isupper():
        first_letter_pos = char_position(first_letter.lower())
        new_number = number / first_letter_pos
    else:
        first_letter_pos = char_position(first_letter.lower())
        new_number = number * first_letter_pos
    if last_letter.isupper():
        last_letter_pos = char_position(last_letter.lower())
        total_sum += new_number - last_letter_pos
    else:
        last_letter_pos = char_position(last_letter.lower())
        total_sum += new_number + last_letter_pos
print(f"{total_sum:.2f}")
