lst_input = list(map(int, input().split()))
n = int(input())

# for i in range(n):
#     min_number = min(lst_input)
#     for element in lst_input:
#         if element <= min_number:
#             lst_input.remove(element)
# print(*lst_input, sep=", ")

for i in range(n):
    lst_input.remove(min(lst_input))
print(*lst_input, sep=", ")

