def swap(numbers, first_inx, second_inx):
    numbers[first_inx], numbers[second_inx] = numbers[second_inx], numbers[first_inx]
    return numbers


def multiply(numbers, first_inx, second_inx):
    numbers[first_inx] = numbers[first_inx] * numbers[second_inx]
    return numbers


def decrease(numbers):
    numbers = [num - 1 for num in numbers]
    return numbers


numbers = [int(num) for num in input().split()]
command = input()
while command != "end":
    command = command.split()
    action = command[0]
    if len(command) > 1:
        index_one, index_two = command[1], command[2]
    if command[0] == "swap":
        numbers = swap(numbers, int(index_one), int(index_two))
    elif command[0] == "multiply":
        numbers = multiply(numbers, int(index_one), int(index_two))
    elif command[0] == "decrease":
        numbers = decrease(numbers)

    command = input()

print(*numbers, sep=", ")
