def urgent(groceries_list: list , item: str):
    if item not in groceries_list:
        groceries_list.insert(0 , item)
        return groceries_list
    return groceries_list


def unnecessary(groceries_list: list , item: str):
    if item in groceries_list:
        groceries_list.remove(item)
        return groceries_list
    return groceries_list


def correct(groceries_list: list , old_item: str , new_item: str):
    if old_item in groceries_list:
        index = groceries_list.index(old_item)
        groceries_list[index] = new_item
        return groceries_list
    return groceries_list


def rearrange(groceries_list: list , item: str):
    if item in groceries_list:
        groceries_list.remove(item)
        groceries_list.append(item)
        return groceries_list
    return groceries_list


list_with_groceries = input().split('!')
command = input().split()
while command[0] != 'Go':
    if command[0] == 'Urgent':
        urgent(list_with_groceries , command[1])
    elif command[0] == 'Unnecessary':
        unnecessary(list_with_groceries , command[1])
    elif command[0] == 'Correct':
        correct(list_with_groceries , command[1] , command[2])
    elif command[0] == 'Rearrange':
        rearrange(list_with_groceries , command[1])
    command = input().split()
print(', '.join(list_with_groceries))
