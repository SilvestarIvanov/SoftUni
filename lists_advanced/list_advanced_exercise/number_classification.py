numbers = list(map(int, input().split(", ")))

positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]


print("Positive:", ", ".join(str(num) for num in positive_numbers))
print("Negative:", ", ".join(str(num) for num in negative_numbers))
print("Even:", ", ".join(str(num) for num in even_numbers))
print("Odd:", ", ".join(str(num) for num in odd_numbers))