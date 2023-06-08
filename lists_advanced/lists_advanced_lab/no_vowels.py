text_input = input()

no_vowels_text = [letter for letter in text_input if letter.lower() not in['a', 'o', 'u', 'e', 'i']]
print("".join(no_vowels_text))