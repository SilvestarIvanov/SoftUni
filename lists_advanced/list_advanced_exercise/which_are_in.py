string_one = input().split(', ')
string_two = input().split(', ')

final_result = []
for word_one in string_one:
    for word_two in string_two:
        if word_one in word_two:
            final_result.append(word_one)
            break

print(final_result)

