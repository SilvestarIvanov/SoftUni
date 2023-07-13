all_strings = input().split()
total_sum = 0
for current_str in all_strings:
    first_letter = current_str[0]
    last_letter = current_str[-1]
    current_num = int(current_str[1:len(current_str) - 1])
    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += current_num / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += current_num * first_letter_position
    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position


print(f"{total_sum:.2f}")