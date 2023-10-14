array_with_integers = input().split()
array_with_integers = [int(s) for s in array_with_integers]
command = input().split()
while command[0] != 'end':
    if command[0] == 'swap':
        array_with_integers[int(command[1])] , array_with_integers[int(command[2])] = \
            array_with_integers[int(command[2])] , array_with_integers[int(command[1])]
    elif command[0] == 'multiply':
        product = array_with_integers[int(command[1])] * array_with_integers[int(command[2])]
        array_with_integers[int(command[1])] = product
    elif command[0] == 'decrease':
        array_with_integers = [(x - 1) for x in array_with_integers]
    command = input().split()
array_with_integers = [str(s) for s in array_with_integers]
print(', '.join(array_with_integers))
