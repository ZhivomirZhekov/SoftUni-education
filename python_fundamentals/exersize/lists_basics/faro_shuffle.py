card_deck = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    middle_of_deck = len(card_deck) // 2
    left_part_of_deck = card_deck[0:middle_of_deck]
    right_part_of_deck = card_deck[middle_of_deck:]
    shuffled_deck = []
    for card_index in range(len(left_part_of_deck)):
        shuffled_deck.append(left_part_of_deck[card_index])
        shuffled_deck.append(right_part_of_deck[card_index])
    card_deck = shuffled_deck
print(card_deck)


