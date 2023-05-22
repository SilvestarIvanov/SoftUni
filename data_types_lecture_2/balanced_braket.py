number_of_lines = int(input())

balance = 0
for line in range(number_of_lines):
    new_lines = input()
    if new_lines == "(":
        balance += 1
        if balance > 1:
            print("UNBALANCED")
            exit()
    elif new_lines == ")":
        balance -= 1

if balance == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
