def sort_numbers(num):
    numbers_list = num.split()
    sorted_list = sorted(numbers_list, key=int)
    return sorted_list


numbers_input = input()
print(list(map(int, sort_numbers(numbers_input))))