
while True:
    current_string = input()
    if current_string == 'End':
        break
    elif current_string != 'SoftUni':
        new_string = ''
        for character in current_string:
            new_string += character * 2
        print(new_string)
