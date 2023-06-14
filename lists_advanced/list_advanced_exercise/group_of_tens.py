numbers = [int(s) for s in input().split(", ")]
current_group_of_numbers = 10
while numbers:
    filtered_numbers = [num for num in numbers if num <= current_group_of_numbers]
    print(f"Group of {current_group_of_numbers}'s: {filtered_numbers}")
    current_group_of_numbers += 10
    numbers = [number for number in numbers if number not in filtered_numbers]
