string_input = list(map(float, input().split()))
rounded_list = []
for i in string_input:
    rounded_list.append(round(i))

print(rounded_list)