list_happiness = list(map(int, input().split()))
factor = int(input())

improved_happiness = [h * factor for h in list_happiness]
average_happiness = sum(improved_happiness) / len(list_happiness)

happy_count = sum(h >= average_happiness for h in improved_happiness)
total_count = len(list_happiness)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
