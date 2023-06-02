numbers_sequence = input()
text_sequence = input()

numbers = [int(num) for num in numbers_sequence.split(" ")]
message = ""

for num in numbers:
    digit_sum = sum(int(digit) for digit in str(num))
    index = digit_sum % len(text_sequence)
    char = text_sequence[index]
    message += char
    text_sequence = text_sequence[:index] + text_sequence[index + 1:]

print(message)
