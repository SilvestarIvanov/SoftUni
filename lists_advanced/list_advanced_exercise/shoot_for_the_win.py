numbers = [int(num) for num in input().split()]

command = input()
count = 0
while command != "End":
    command = int(command)
    if command < len(numbers):
        previous_value = numbers[command]
        numbers[command] = - 1
        count += 1
        for index, num in enumerate(numbers):
            if num != -1:
                if num > previous_value:
                    num -= previous_value
                    numbers[index] = num
                else:
                    num += previous_value
                    numbers[index] = num
    command = input()
print(f"Shot targets: {count} -> {' '.join(str(i) for i in numbers)}")





