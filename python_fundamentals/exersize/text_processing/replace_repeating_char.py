text = input()
final_message = ""
last_added_latter = ""

for current_character in text:
    if last_added_latter != current_character:
        final_message += current_character
        last_added_latter = current_character
print(final_message)