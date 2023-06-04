def check_for_perfect_number(number):
    perfect = []
    for i in range(1, number + 1):
        if number % i == 0:
            perfect.append(i)
    result = sum(perfect) // 2
    if result == number:
        return True
    else:
        return False


number_input = int(input())
if check_for_perfect_number(number_input):
    print("We have a perfect number!")
else :
    print("It's not so perfect.")