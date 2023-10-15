def shoot(targets, index, power):
    if index > len(targets) - 1 or index < 0:
        return targets
    if targets[index] > power:
        targets[index] -= power
    else:
        targets.pop(index)
    return targets


def add(targets, index, value):
    if index > len(targets) - 1 or index < 0:
        return print("Invalid placement!")
    targets.insert(index, value)
    return targets


def strike(targets, index, radius):
    if index + radius > len(targets) - 1 or index - radius < 0:
        return print("Strike missed!")
    start_index = index - radius
    end_index = index + radius
    for removing_index in range(end_index, start_index - 1 ,-1):
        targets.pop(removing_index)
    return targets


sequence_of_targets = input().split()
sequence_of_targets = [int(x) for x in sequence_of_targets]
command = input().split()
while command[0] != 'End':
    if command[0] == 'Shoot':
        shoot(sequence_of_targets, int(command[1]), int(command[2]))
    elif command[0] == 'Add':
        add(sequence_of_targets, int(command[1]), int(command[2]))
    elif command[0] == 'Strike':
        strike(sequence_of_targets, int(command[1]), int(command[2]))
    command = input().split()
sequence_of_targets = [str(x) for x in sequence_of_targets]
print('|'.join(sequence_of_targets))