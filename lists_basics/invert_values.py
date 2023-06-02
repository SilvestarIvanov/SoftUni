list_of_numbers = input().split()

opposite_numbers = []
for i in list_of_numbers:
    current_number = -int(i)
    opposite_numbers.append(current_number)
print(opposite_numbers)