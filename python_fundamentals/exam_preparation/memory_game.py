def main():
    sequence_of_elements = input().split()
    count_moves = 0

    while True:
        command = input()
        count_moves += 1
        if command == 'end':
            print(f"Sorry you lose :(\n{sequence_of_elements}")
            break

        index1 , index2 = map(int, command.split())

        if is_invalid_input(index1, index2, sequence_of_elements):
            handle_invalid_input(sequence_of_elements, count_moves)
        else:
            handle_valid_input(index1 , index2, sequence_of_elements , count_moves)


def is_invalid_input(index1, index2 , sequence_of_elements):
    return (
        index1 == index2
        or index1 < 0
        or index2 < 0
        or index1 >= len(sequence_of_elements) - 1
        or index2 >= len(sequence_of_elements) - 1
    )


def handle_invalid_input(sequence_of_elements, count_moves):
    mid_index = len(sequence_of_elements) // 2
    sequence_of_elements.insert(mid_index, f'-{count_moves}a')
    sequence_of_elements.insert(mid_index, f'-{count_moves}a')
    print("Invalid input! Adding additional elements to the board")


def handle_valid_input(index1 , index2, sequence_of_elements , count_moves):
    if sequence_of_elements[index1] == sequence_of_elements[index2]:
        print(f"Congrats! You have found matching elements - ${sequence_of_elements[index2]}!")
        second_el = sequence_of_elements[index2]
        sequence_of_elements.pop(index1)
        sequence_of_elements.remove(second_el)

    else:
        print('Try again!')

    if len(sequence_of_elements) == 0:
        print(f"You have won in {count_moves} turns!")
        exit()

