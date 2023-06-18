def blacklist(friends_name, command_name, blacklist_count):
    if command_name not in friends_name:
        print(f"{command_name} was not found.")
    else:
        for index, friend in enumerate(friends_name):
            if friend == command_name:
                real_name = friend
                friends_name[index] = "Blacklisted"
                blacklist_count += 1
                print(f"{real_name} was blacklisted.")
    return friends_name, blacklist_count


def error(friends_name, index, lost_name_count):
    if index >= 0 and index < len(friends_name):
        if friends_name[index] != "Blacklisted":
            if not friends_name[index] == "Lost":
                real_name = friends_name[index]
                friends_name[index] = "Lost"
                lost_name_count += 1
                print(f"{real_name} was lost due to an error.")
    return friends_name, lost_name_count


def change(friends_name, index, new_name):
    if 0 <= index < len(friends_name):
        real_name = friends_name[index]
        friends_name[index] = new_name
        print(f"{real_name} changed his username to {new_name}.")
    return friends_name


friends_names = input().split(", ")

command = input()
blacklisted_count = 0
lost_names = 0
while command != "Report":
    command = command.split()
    if command[0] == "Blacklist":
        friends_names, blacklisted_count = blacklist(friends_names, command[1], blacklisted_count)
    elif command[0] == "Error":
        friends_names, lost_names = error(friends_names, int(command[1]), lost_names)
    elif command[0] == "Change":
        friends_names = change(friends_names, int(command[1]), command[2])
    command = input()

print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_names}")
print(*friends_names, sep=" ")
