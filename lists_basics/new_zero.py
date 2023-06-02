numbers = list(map(int, input().split(", ")))
new_lst = []
zero_lst = []
for item in numbers:
    if item != 0:
        new_lst.append(item)
    else:
        zero_lst.append(item)

print(new_lst + zero_lst)



