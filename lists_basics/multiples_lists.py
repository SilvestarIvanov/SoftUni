factor = int(input())
count = int(input())

numbers_list = []

for multiplier in range(1, count + 1):
    numbers_list.append(factor * multiplier)
print(numbers_list)
