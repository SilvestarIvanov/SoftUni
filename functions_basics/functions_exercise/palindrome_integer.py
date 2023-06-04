def find_palindrome(num):
    numbers_to_check = num.split(", ")
    for number in numbers_to_check:
        if number[0] == number[-1]:
            print(True)
        else:
            print(False)


some_numbers = input()
find_palindrome(some_numbers)