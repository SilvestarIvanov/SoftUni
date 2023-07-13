number = int(input())
digit = int(input())

count = 0
while number > 0:
    remain_amount = number % 2

    if remain_amount == digit:
        count += 1

    number = number // 2

print(count)