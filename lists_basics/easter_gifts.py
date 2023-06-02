name_of_gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    commands = command.split()
    if commands[0] == "OutOfStock":
        gift = commands[1]
        for i in range(len(name_of_gifts)):
            if name_of_gifts[i] == gift:
                name_of_gifts[i] = "None"
    if commands[0] == "Required":
        if 0 < int(commands[2]) <= len(name_of_gifts) - 1:
            gift = commands[1]
            index_to_replace = int(commands[2])
            name_of_gifts[index_to_replace] = gift
    if commands[0] == "JustInCase":
        gift = commands[1]
        name_of_gifts[-1] = gift
for item in name_of_gifts:
    if item != "None":
        print(item, end=' ')
