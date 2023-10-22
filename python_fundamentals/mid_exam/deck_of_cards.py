list_of_cards = input().split(", ")
number_of_commands = int(input())
for i in range(number_of_commands):
    command = input().split(", ")
    if command[0] == "Add":
        card_name = command[1]
        if card_name in list_of_cards:
            print("Card is already in the deck")
        else:
            list_of_cards.append(card_name)
            print("Card successfully added")
    elif command[0] == "Remove":
        card_to_remove = command[1]
        if card_to_remove not in list_of_cards:
            print("Card not found")
        else:
            list_of_cards.remove(card_to_remove)
            print("Card successfully removed")
    elif command[0] == "Remove At":
        index = int(command[1])
        if 0 <= index < len(list_of_cards):
            list_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command[0] == "Insert":
        index = int(command[1])
        card_to_insert = command[2]
        if index not in range(0, len(list_of_cards)):
            print("Index out of range")
        elif card_to_insert in list_of_cards:
            print("Card is already added")
        else:
            list_of_cards.insert(index , card_to_insert)
            print("Card successfully added")
print(', '.join(list_of_cards))

