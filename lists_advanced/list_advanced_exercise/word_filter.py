text_input = input().split()

filtered_words = [word for word in text_input if len(word) % 2 == 0]
for word in filtered_words:
    print(word)