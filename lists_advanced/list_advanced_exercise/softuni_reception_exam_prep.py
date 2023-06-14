efficiency_1 = int(input())
efficiency_2 = int(input())
efficiency_3 = int(input())
students_count = int(input())

hours_counter = 0
total_time = 0
students_per_hour = efficiency_1 + efficiency_2 + efficiency_3

while students_count > 0:
    hours_counter += 1
    total_time += 1
    if hours_counter % 4 == 0:
        continue
    students_count -= students_per_hour

print(f"Time needed: {total_time}h.")
