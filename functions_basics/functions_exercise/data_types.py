def check_data_type(data_type, num):
    if data_type == "int":
        num_int = int(num)
        result_int = num_int * 2
        return result_int
    elif data_type == "real":
        num_float = float(num)
        result_float = num_float * 1.50
        return f"{result_float:.2f}"
    elif data_type == "string":
        result_str = f"${num}$"
        return str(result_str)


str_input = input()
number_input = input()
print(check_data_type(str_input, number_input))