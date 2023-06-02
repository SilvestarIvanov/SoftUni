numbers = list(map(float, input().split()))
new_lst = []
for i in numbers:
    absolute_numbers = abs(i)
    new_lst.append(absolute_numbers)
print(new_lst)

