string_input = input().split(", ")

sorted_list = sorted(string_input, key=lambda x: (-len(x), x))

print(sorted_list)