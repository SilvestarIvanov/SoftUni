number_of_lines = int(input())
total_sum = 0
for i in range(0, number_of_lines):
    user_input = input()
    values = ord(user_input)
    total_sum += values
print(f"The sum equals: {total_sum}")
