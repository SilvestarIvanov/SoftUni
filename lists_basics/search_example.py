number = int(input())
word = input()

result = []
for i in range(number):
    str_input = input()
    result.append(str_input)
print(result)

for i in range(len(result) - 1, - 1, - 1):
    element = result[i]
    if word not in element:
        result.remove(element)
print(result)