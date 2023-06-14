numbers = list(map(int, input().split()))

average_number = sum(numbers) // len(numbers)

greater_number = [num for num in sorted(numbers, reverse=True) if num > average_number]

if len(greater_number) != 0:
    print(" ".join(map(str, greater_number[:5])))
else:
    print("No")

