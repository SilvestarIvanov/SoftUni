def sum_of_odd_and_even(num: int):
    num_list = list(map(int, str(num)))
    sum_of_odd = []
    sum_of_even = []
    for number in num_list:
        if number % 2 == 0:
            sum_of_even.append(number)
        else:
            sum_of_odd.append(number)
    total_sum_even = sum(sum_of_even)
    total_sum_odd = sum(sum_of_odd)
    return f"Odd sum = {total_sum_odd}, Even sum = {total_sum_even}"


number_input = int(input())
print(sum_of_odd_and_even(number_input))