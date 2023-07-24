def conceal_and_reveal():
    message = input()

    while True:
        command = input()

        if command == "Reveal":
            break

        command_parts = command.split(":|:")
        instruction = command_parts[0]

        if instruction == "InsertSpace":
            index = int(command_parts[1])
            message = message[:index] + " " + message[index:]
        elif instruction == "Reverse":
            substring = command_parts[1]
            if substring in message:
                reversed_substring = substring[::-1]
                message = message.replace(substring, "", 1) + reversed_substring
            else:
                print("error")
                continue
        elif instruction == "ChangeAll":
            substring = command_parts[1]
            replacement = command_parts[2]
            message = message.replace(substring, replacement)

        print(message)

    print(f"You have a new text message: {message}")


conceal_and_reveal()

