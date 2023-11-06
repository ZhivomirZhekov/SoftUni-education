def add(dictionary: dict , new_piece , new_composer , new_key):
    for exist_pieces in dictionary.keys():
        if exist_pieces == new_piece:
            print(f"{new_piece} is already in the collection!")
            return dictionary
    dictionary[new_piece][new_composer] = new_key
    print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
    return dictionary


def to_remove(dictionary: dict , piece_to_remove: str):
    for exist_pieces in dictionary.keys():
        if exist_pieces == piece_to_remove:
            del dictionary[piece_to_remove]
            print(f"Successfully removed {piece_to_remove}!")
            return dictionary
    print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
    return dictionary


def change_key(dictionary: dict , piece_key_to_change , new_key):
    for exist_pieces , exist_composers in dictionary.items():
        if exist_pieces == piece_key_to_change:
            for composer in exist_composers.keys():
                dictionary[piece_key_to_change][composer] = new_key
            print(f"Changed the key of {piece_key_to_change} to {new_key}!")
            return dictionary
    print(f"Invalid operation! {piece_key_to_change} does not exist in the collection.")
    return dictionary


number_of_pieces = int(input())
pieces_dict = {}
for _ in range(number_of_pieces):
    piece , composer , key = input().split("|")
    if composer not in pieces_dict.keys():
        pieces_dict[piece] = {}
    pieces_dict[piece][composer] = key

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        pieces_dict = add(pieces_dict , piece , composer , key)
    elif command[0] == "Remove":
        piece = command[1]
        pieces_dict = to_remove(pieces_dict , piece)
    elif command[0] == "ChangeKey":
        piece = command[1]
        key = command[2]
        pieces_dict = change_key(pieces_dict , piece , key)

for pieces , composers in pieces_dict.items():
    for composer , key in composers.items():
        print(f"{pieces} -> Composer: {composer}, Key: {key}")