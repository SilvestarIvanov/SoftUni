number_of_messages = int(input())

for current_message in range(number_of_messages):
    num = int(input())
    if num == 88:
        print("Hello")
    elif num == 86:
        print("How are you?")
    elif num < 88:
        print("GREAT!")
    else:
        print("Bye.")