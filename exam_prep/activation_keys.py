raw_activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    if "Contains" in command:
        instruction, substring = command.split(">>>")
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif "Flip" in command:
        instruction, case, start, end = command.split(">>>")
        start, end = int(start), int(end)
        if case == "Upper":
            raw_activation_key = raw_activation_key[:start] + raw_activation_key[start:end].upper() + raw_activation_key[end:]
        elif case == "Lower":
            raw_activation_key = raw_activation_key[:start] + raw_activation_key[start:end].lower() + raw_activation_key[end:]
        print(raw_activation_key)
    elif "Slice" in command:
        instruction, start, end = command.split(">>>")
        start, end = int(start), int(end)
        raw_activation_key = raw_activation_key[:start] + raw_activation_key[end:]
        print(raw_activation_key)
print(f"Your activation key is: {raw_activation_key}")


