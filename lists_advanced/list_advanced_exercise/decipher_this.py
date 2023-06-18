messages_input = input()
new_message = messages_input.split(" ")
output = []
for item in new_message:
    new_item_to_append=item.replace(''.join(filter(str.isdigit, item)), chr(int(''.join(filter(str.isdigit, item)))))
    output.append(new_item_to_append)

for item in output:
    new_item = list(item)
    new_item[1], new_item[-1] = new_item[-1], new_item[1]
    new_string = "".join(new_item)
    print(new_string, end=' ')
