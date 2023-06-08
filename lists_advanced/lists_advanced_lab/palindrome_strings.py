words = input().split()
special_word = input()

palindromes = []

for word in words:
    if word == "".join(reversed(word)):
        palindromes.append(word)
print(palindromes)
print(f"Found palindrome {palindromes.count(special_word)} times")