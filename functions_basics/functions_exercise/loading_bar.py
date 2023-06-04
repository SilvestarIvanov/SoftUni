def loading_bar(num):
    result = []
    if num in range(0, 101) and num % 10 == 0:
        num_count = num // 10
        dots_count = 10 - num_count
        for item in range(num_count):
            result.append("%")
        for element in range(dots_count):
            result.append(".")
        final_result = "".join(result)
        if num == 100:
            return f"{num}% Complete!\n["+final_result+"]"
        else:
            return f"{num}% ["+final_result+"]\nStill loading..."


number_input = int(input())
print(loading_bar(number_input))