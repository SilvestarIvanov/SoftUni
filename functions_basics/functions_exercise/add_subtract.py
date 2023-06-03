def sum_numbers(num1_to_sum: int, num2_to_sum: int):
    return num1_to_sum + num2_to_sum


def subtract(num1_to_sum, num2_to_sum, num3):
    return sum_numbers(num1_to_sum, num2_to_sum) - num3


def add_and_subtract(num1_to_sum, num2_to_sum, num3):
    return subtract(num1_to_sum, num2_to_sum, num3)


print(add_and_subtract(int(input()), int(input()), int(input())))
