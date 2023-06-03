def find_smallest(a:int, b:int, c: nt):
    new_list = [a, b, c]
    new_list.sort()
    return new_list[0]


a = int(input())
b = int(input())
c = int(input())
print(find_smallest(a, b, c))






