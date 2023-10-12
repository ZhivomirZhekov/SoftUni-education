sequence_of_elements = input().split()
moves_count = 0
while True:
    command = input().split()
    if command[0] == 'end':
        if len(sequence_of_elements) > 0:
            print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
        break
    moves_count += 1
    command = [int(x) for x in command]
    if command[0] == command[1] or not 0 <= command[0] < len(sequence_of_elements) \
            or not 0 <= command[1] < len(sequence_of_elements):
        middle_of_sequence = len(sequence_of_elements) // 2
        sequence_of_elements.insert(middle_of_sequence , f'-{moves_count}a')
        sequence_of_elements.insert(middle_of_sequence , f'-{moves_count}a')
        print("Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[command[0]] == sequence_of_elements[command[1]]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[command[0]]}!")
        if command[0] > command[1]:
            sequence_of_elements.pop(command[0])
            sequence_of_elements.pop(command[1])
        else:
            sequence_of_elements.pop(command[1])
            sequence_of_elements.pop(command[0])
    else:
        print("Try again!")

    if not sequence_of_elements:
        print(f"You have won in {moves_count} turns!")
        break
