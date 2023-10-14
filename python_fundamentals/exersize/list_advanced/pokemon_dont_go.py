sequence_of_numbers = input().split()
sequence_of_numbers = [int(x) for x in sequence_of_numbers]
removed_numbers_sum = 0
while sequence_of_numbers:
    index_to_remove = int(input())
    if index_to_remove < 0:
        index_to_remove = 0
        removed_number = sequence_of_numbers.pop(index_to_remove)
        removed_numbers_sum += removed_number
        sequence_of_numbers.insert(0 , sequence_of_numbers[-1])
    elif index_to_remove > len(sequence_of_numbers) - 1:
        index_to_remove = -1
        removed_number = sequence_of_numbers.pop(index_to_remove)
        removed_numbers_sum += removed_number
        sequence_of_numbers.append(sequence_of_numbers[0])
    else:
        removed_number = sequence_of_numbers.pop(index_to_remove)
        removed_numbers_sum += removed_number
    for digit in range(len(sequence_of_numbers)):
        if sequence_of_numbers[digit] > removed_number:
            sequence_of_numbers[digit] -= removed_number
        else:
            sequence_of_numbers[digit] += removed_number
print(removed_numbers_sum)
