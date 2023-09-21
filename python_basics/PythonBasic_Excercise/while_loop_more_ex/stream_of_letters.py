count_c = 0
count_o = 0
count_n = 0
word = ''
total_phrase = ''
while True:
    character = input()
    if count_c != 0 and count_o != 0 and count_n != 0:
        word += ' '
        count_o = 0
        count_n = 0
        count_c = 0
        total_phrase += word
        word = ''
    if character == 'End':
        print(f'{total_phrase}')
        break
    ascii_number = ord(character)
    if 65 <= ascii_number <= 90 or 97 <= ascii_number <= 122:
        if character == 'c':
            count_c += 1
            if count_c < 2:
                continue
            else:
                word += character
                continue
        elif character == 'o':
            count_o += 1
            if count_o < 2:
                continue
            else:
                word += character
                continue
        elif character == 'n':
            count_n += 1
            if count_n < 2:
                continue
            else:
                word += character
                continue
        word += character
