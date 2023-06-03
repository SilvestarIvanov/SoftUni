def find_all_characters(number_one, number_two):
    characters = []
    for char in range(ord(number_one) + 1, ord(number_two)):
        characters.append(chr(char))
    return characters


num_one = input()
num_two = input()
print(" ".join(find_all_characters(num_one, num_two)))