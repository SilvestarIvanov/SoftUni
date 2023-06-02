string_input = list(map(int, input().split(", ")))

print(string_input)

zeros_count = string_input.count(0)

while 0 in string_input:
    string_input.remove(0)
for i in range(zeros_count):
    string_input.append(0)
print(string_input)
