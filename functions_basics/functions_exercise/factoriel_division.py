def calculate_factorial(number):
    for current_num in range(1, number):
        number *= current_num
    return number


first_num = int(input())
second_num = int(input())
first_num_factorial = calculate_factorial(first_num)
second_num_factorial = calculate_factorial(second_num)
result = first_num_factorial / second_num_factorial
print(f"{result:.2f}")