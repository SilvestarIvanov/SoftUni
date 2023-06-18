def chat_message(message_list, message_to_add):
    message_list.append(message_to_add)
    return message_list


def delete_message(message_list, message_to_delete):
    if message_to_delete in message_list:
        message_list.remove(message_to_delete)
    return message_list


def edit_message(message_list, old_message, new_message):
    if old_message in message_list:
        for index, value in enumerate(message_list):
            if message_list[index] == old_message:
                message_list[index] = new_message
    return message_list


def pin_message(message_list, message_to_pin):
    if message_to_pin in message_list:
        for index, value in enumerate(message_list):
            if message_list[index] == message_to_pin:
                item_to_remove = message_list.pop(index)
                message_list.append(item_to_remove)
    return message_list


def spam_message(message_list, spam_message_to_add):
    for message_to_add in spam_message_to_add:
        message_list.append(message_to_add)
    return message_list


list_of_messages = []
message = input()
while message != "end":
    message = message.split()
    if message[0] == "Chat":
        list_of_messages = chat_message(list_of_messages, message[1])
    elif message[0] == "Delete":
        list_of_messages = delete_message(list_of_messages, message[1])
    elif message[0] == "Edit":
        list_of_messages = edit_message(list_of_messages, message[1], message[2])
    elif message[0] == "Pin":
        list_of_messages = pin_message(list_of_messages, message[1])
    elif message[0] == "Spam":
        list_of_messages = spam_message(list_of_messages, message[1:])

    message = input()
print(*list_of_messages, sep="\n")
