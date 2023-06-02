operator_input = input()
first_num_input = int(input())
second_num_input = int(input())


def calculate(operator: str, first_num: int, second_num: int):
    if operator == "multiply":
        return first_num * second_num
    elif operator == "divide":
        return int(first_num / second_num)
    elif operator == "add":
        return first_num + second_num
    elif operator == "subtract":
        return first_num - second_num


print(calculate(operator_input, first_num_input, second_num_input))
