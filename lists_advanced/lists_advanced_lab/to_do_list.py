notes = []

while True:
    command = input()
    if command == "End":
        break
    notes.append(command)
    sorted_notes = sorted(notes, key=lambda x: int(x.split("-")[0]))
    result = [command.split("-")[1] for command in sorted_notes]
print(result)

