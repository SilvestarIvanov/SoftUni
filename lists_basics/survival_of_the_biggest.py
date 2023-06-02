lst_input = list(map(int, input().split()))
n = int(input())

for i in range(n):
    min_number = min(lst_input)
    for element in lst_input:
        if element <= min_number:
            lst_input.remove(min_number)
print(*lst_input, sep=", ")


