def is_even(num):
    numbers_evens = num.split()
    even_nums = list(filter(lambda x: int(x) % 2 == 0, numbers_evens))
    return even_nums


number = input()
even_num_list = is_even(number)
print(list(map(int, even_num_list)))