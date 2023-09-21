most_powerful_word = ''
powerful_sum = 0
compare = 0
command = input()
while command != "End of words":

    for char in range(len(command)):
        compare += ord(command[char])

    if command[0] == 'a' or command[0] == 'A' or command[0] == 'e' or command[0] == 'E' \
            or command[0] == 'i' or command[0] == 'I' or command[0] == 'o' or command[0] == 'O' \
            or command[0] == 'u' or command[0] == 'U' or command[0] == 'y' or command[0] == 'Y':
        compare *= len(command)
    else:
        compare = round(compare / len(command))
    if compare > powerful_sum:
        powerful_sum = compare
        most_powerful_word = command
    compare = 0
    command = input()
print(f"The most powerful word is {most_powerful_word} - {powerful_sum}")
