def shoot(list_targets, target_index, shoot_power):
    if target_index in range(len(list_targets)):
        if list_targets[target_index] <= shoot_power:
            list_targets.pop(target_index)
        else:
            list_targets[target_index] -= shoot_power
    return list_targets


def add(list_targets, target_index, target_value):
    if target_index in range(len(list_targets)):
        list_targets.insert(target_index, target_value)
    else:
        print("Invalid placement!")
    return list_targets


def strike(list_targets, target_index, target_radius):
    if target_index - target_radius in range(len(list_targets)) and target_index + target_radius in range(len(list_targets)):
        list_targets = list_targets[0:target_index - target_radius] + list_targets[target_index + target_radius + 1:]
    else:
        print("Strike missed!")
    return list_targets


targets = [int(target) for target in input().split()]
command = input()

while command != "End":
    command = command.split()
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)

    command = input()
print(*targets, sep="|")