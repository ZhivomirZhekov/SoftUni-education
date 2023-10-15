targets = input().split()
targets = [int(x) for x in targets]
command = input()
shouted_index = []
while command != 'End':
    command = int(command)
    if command > len(targets) - 1:
        command = input()
        continue
    if command not in shouted_index:
        shouted_index.append(command)
        shot = targets[command]
        targets[command] = -1
        for index in range(len(targets)):
            if index in shouted_index:
                continue
            if targets[index] > shot:
                targets[index] -= shot
            else:
                targets[index] += shot
    command = input()
targets = [str(x) for x in targets]
print(f"Shot targets: {len(shouted_index)} -> {' '.join(targets)}")
