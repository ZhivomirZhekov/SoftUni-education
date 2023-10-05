list_of_gifts = input().split()
command = input()
while command != 'No Money':
    if 'OutOfStock' in command:
        command_items = command.split(' ')
        gift = command_items[-1]
        list_of_gifts = [item.replace(gift, 'None') for item in list_of_gifts]
    elif 'Required' in command:
        command_items = command.split(' ')
        gift = command_items[1]
        searched_index = int(command_items[-1])
        if 0 <= searched_index <= len(list_of_gifts) - 1:
            list_of_gifts[searched_index] = gift
    elif 'JustInCase' in command:
        command_items = command.split(' ')
        gift = command_items[-1]
        list_of_gifts[-1] = gift
    command = input()
list_of_gifts = [item for item in list_of_gifts if item != 'None']
print(*list_of_gifts)
