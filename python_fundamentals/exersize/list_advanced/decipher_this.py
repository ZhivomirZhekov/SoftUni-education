secret_message = input().split()
deciphered_message = []
for secret_word in secret_message:
    word = []
    letter_digits = []
    for letters in secret_word:
        if letters.isnumeric():
            letter_digits.append(letters)
        else:
            word += letters
    letter_digits = ''.join(letter_digits)
    letter_digits = chr(int(letter_digits))
    word.insert(0 , letter_digits)
    word[1] , word[-1] = word[-1] , word[1]
    deciphered_message.append(''.join(word))

print(' '.join(deciphered_message))
