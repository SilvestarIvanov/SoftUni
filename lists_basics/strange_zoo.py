my_list = []

for _ in range(3):
    data = input()
    my_list.append(data)
# swap the places of the data in the list
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)

# how to convert a list of strings to integers
# my_list = ["1","2","3","4","5","6","7","8","9"]
#
# for element in range(len(my_list)):
#     my_list[element] = int(my_list[element])
#
# print(my_list)