import re

message = input()
pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
matches = re.findall(pattern, message)
mirror_words = {}
for match in matches:
    reversed_string = match[2][::-1]
    if match[1] == reversed_string:
        mirror_words[match[1]] = match[2]
if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:\n" + ', '.join(str(key) + " <=> " + str(value) for key, value in mirror_words.items()))
