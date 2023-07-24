import re

phones = input()

regex = "\\+359-2-\\d{3}-\\d{4}\\b|\\+359 2 \\d{3} \\d{4}"

matches = re.findall(regex, phones)
print(", ".join(matches))
