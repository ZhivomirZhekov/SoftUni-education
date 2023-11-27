def add(pieces , piece , composer , key):
    if piece in pieces.keys():
        print(f"{piece} is already in the collection!")
    else:
        pieces[piece] = {"composer": composer , "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove(pieces , piece):
    if piece in pieces.keys():
        del pieces[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(pieces , piece , new_key):
    if piece in pieces.keys():
        pieces[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def main_function():
    number_of_pieces = int(input())
    pieces = {}
    for _ in range(number_of_pieces):
        piece , composer , key = input().split("|")
        pieces[piece] = {"composer": composer , "key": key}

    while True:
        command = input().split("|")
        if command[0] == "Stop":
            break
        action = command[0]
        if action == "Add":
            piece , composer , key = command[1] , command[2] , command[3]
            add(pieces , piece , composer , key)
        elif action == "Remove":
            piece = command[1]
            remove(pieces , piece)
        elif action == "ChangeKey":
            piece , new_key = command[1] , command[2]
            change_key(pieces , piece , new_key)
    for piece , composer_key in pieces.items():
        composer = composer_key["composer"]
        key = composer_key["key"]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


main_function()

# def add(dictionary: dict , new_piece , new_composer , new_key):
#     for exist_pieces in dictionary.keys():
#         if exist_pieces == new_piece:
#             print(f"{new_piece} is already in the collection!")
#             return dictionary
#     dictionary[new_piece][new_composer] = new_key
#     print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
#     return dictionary
#
#
# def to_remove(dictionary: dict , piece_to_remove: str):
#     for exist_pieces in dictionary.keys():
#         if exist_pieces == piece_to_remove:
#             del dictionary[piece_to_remove]
#             print(f"Successfully removed {piece_to_remove}!")
#             return dictionary
#     print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
#     return dictionary
#
#
# def change_key(dictionary: dict , piece_key_to_change , new_key):
#     for exist_pieces , exist_composers in dictionary.items():
#         if exist_pieces == piece_key_to_change:
#             for composer in exist_composers.keys():
#                 dictionary[piece_key_to_change][composer] = new_key
#             print(f"Changed the key of {piece_key_to_change} to {new_key}!")
#             return dictionary
#     print(f"Invalid operation! {piece_key_to_change} does not exist in the collection.")
#     return dictionary
#
#
# number_of_pieces = int(input())
# pieces_dict = {}
# for _ in range(number_of_pieces):
#     piece , composer , key = input().split("|")
#     if composer not in pieces_dict.keys():
#         pieces_dict[piece] = {}
#     pieces_dict[piece][composer] = key
#
# while True:
#     command = input().split("|")
#     if command[0] == "Stop":
#         break
#     if command[0] == "Add":
#         piece = command[1]
#         composer = command[2]
#         key = command[3]
#         pieces_dict = add(pieces_dict , piece , composer , key)
#     elif command[0] == "Remove":
#         piece = command[1]
#         pieces_dict = to_remove(pieces_dict , piece)
#     elif command[0] == "ChangeKey":
#         piece = command[1]
#         key = command[2]
#         pieces_dict = change_key(pieces_dict , piece , key)
#
# for pieces , composers in pieces_dict.items():
#     for composer , key in composers.items():
#         print(f"{pieces} -> Composer: {composer}, Key: {key}")
