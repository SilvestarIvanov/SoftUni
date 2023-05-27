number = int(input())

positive_lst = []
negative_lst = []

for i in range(number):
    numbers_input = int(input())
    if numbers_input >= 0:
        positive_lst.append(numbers_input)
    else:
        negative_lst.append(numbers_input)
print(positive_lst)
print(negative_lst)
print(f"Count of positives: {len(positive_lst)}")
print(f"Sum of negatives: {sum(negative_lst)}")