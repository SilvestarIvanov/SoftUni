numbers = list(map(int, input().split(", ")))

index_of_even_number = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))

even_index = list(filter(lambda x: x != "no", index_of_even_number))
print(even_index)