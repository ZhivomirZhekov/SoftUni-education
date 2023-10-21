def loot(chest_loot: list, loot_list: list):
    for items in loot_list:
        if items not in chest_loot:
            chest_loot.insert(0, items)
    return chest_loot


def drop(chest_loot: list, index_to_remove: int):
    if 0 <= index_to_remove < len(chest_loot):
        removed_item = chest_loot.pop(index_to_remove)
        chest_loot.append(removed_item)
    return chest_loot


def steal(chest_loot: list, num_items_to_remove: int):
    counter = 0
    removed_items = []
    for number_item in range(len(chest_loot) - 1, -1, -1):
        if counter == num_items_to_remove:
           break
        else:
            counter += 1
            removed_item = chest_loot.pop(number_item)
            removed_items.append(removed_item)
    removed_items.reverse()
    print(', '.join(removed_items))


def average_gain(chest_loot: list):
    treasure_gain = 0
    for item in chest_loot:
        treasure_gain += len(item)
    average_treasure_gain = treasure_gain / len(chest_loot)
    return average_treasure_gain


initial_loot = input().split("|")
command = input().split()
while command[0] != 'Yohoho!':
    if command[0] == "Loot":
        loot_items = command[1:]
        loot(initial_loot, loot_items)
    elif command[0] == "Drop":
        index = int(command[1])
        drop(initial_loot, index)
    elif command[0] == "Steal":
        count_items_to_steal = int(command[1])
        steal(initial_loot, count_items_to_steal)
    command = input().split()
if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    print(f"Average treasure gain: {average_gain(initial_loot):.2f} pirate credits.")
