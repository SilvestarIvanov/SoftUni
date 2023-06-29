words = [el.lower() for el in input().split()]

default = 0
occurrences = dict.fromkeys(words, default)
for word in words:
    occurrences[word] += 1  # words.count(word)

for word, count in occurrences.items():
    if count % 2 != 0:
        print(word, end=' ')


# dictionary comprehension example
ex_list = [100, 200, 300]
my_dict = {index: el for index, el in enumerate(ex_list)}

# using for loops
for index, el in enumerate(ex_list):
    my_dict[index] = el
print(my_dict)

# dictionary comprehension example with if else
my_dict = {index: ("even" if index % 2 == 0 else "ood") for index, el in enumerate(ex_list)}
