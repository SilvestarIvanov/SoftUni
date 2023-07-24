import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
matched_emails = re.findall(pattern, sentence)
for email in matched_emails:
    print(email[0])
