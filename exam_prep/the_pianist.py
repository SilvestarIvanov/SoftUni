def add_piece(pieces, piece_info):
    piece, composer, key = piece_info.split("|")
    if piece in pieces:
        return f"{piece} is already in the collection!"
    else:
        pieces[piece] = {"composer": composer, "key": key}
        return f"{piece} by {composer} in {key} added to the collection!"


def remove_piece(pieces, piece):
    if piece in pieces:
        del pieces[piece]
        return f"Successfully removed {piece}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


def change_key(pieces, piece, new_key):
    if piece in pieces:
        pieces[piece]["key"] = new_key
        return f"Changed the key of {piece} to {new_key}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


def print_collection(pieces):
    for piece, info in pieces.items():
        composer = info["composer"]
        key = info["key"]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


n = int(input())
pieces = {}

for _ in range(n):
    piece_info = input()
    piece, composer, key = piece_info.split("|")
    pieces[piece] = {"composer": composer, "key": key}

while True:
    command = input()
    if command == "Stop":
        break

    action, *params = command.split("|")

    if action == "Add":
        result = add_piece(pieces, "|".join(params))
        print(result)
    elif action == "Remove":
        result = remove_piece(pieces, params[0])
        print(result)
    elif action == "ChangeKey":
        result = change_key(pieces, params[0], params[1])
        print(result)

print_collection(pieces)