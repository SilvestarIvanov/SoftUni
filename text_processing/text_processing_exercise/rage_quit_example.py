text = input()
unique_symbols = ""
current_symbol = ""
repetitions = ""

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else:
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)