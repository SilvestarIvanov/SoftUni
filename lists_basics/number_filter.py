number = int(input())

my_list = []
filtered_list = []

for i in range(number):
    new_numbers = int(input())
    my_list.append(new_numbers)
command = input()
if command == 'even':
    for num in my_list:
        if num % 2 == 0:
            filtered_list.append(num)
elif command == 'odd':
    for num in my_list:
        if num % 2 != 0:
            filtered_list.append(num)
elif command == 'negative':
    for num in my_list:
        if num < 0:
            filtered_list.append(num)
elif command == "positive":
    for num in my_list:
        if num >= 0:
            filtered_list.append(num)
print(filtered_list)