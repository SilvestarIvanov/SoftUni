def password_check(password):
    if not 6 <= len(password) <= 10:
        print(f"Password must be between 6 and 10 characters")

    if not password.isalnum():
        print(f"Password must consist only of letters and digits")

    count_number = 0
    for item in password:
        if item.isdigit():
            count_number += 1
    if count_number < 2:
        print(f"Password must have at least 2 digits")

    if count_number >= 2 and password.isalnum() and 6 <= len(password) <= 10:
        print(f"Password is valid")


password_input = input()
password_check(password_input)