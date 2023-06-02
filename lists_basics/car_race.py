# cars_time = list(map(int, input().split()))
#
# finish_line = len(cars_time) // 2
#
# left_car = cars_time[0:finish_line]
# right_car = cars_time[finish_line + 1:]
# total_left = 0
# total_right = 0
# for value in left_car:
#     if value != 0:
#         total_left += value
#     elif value == 0:
#         total_left *= 0.80
# for value in right_car:
#     if value != 0:
#         total_right += value
#     elif value == 0:
#         total_right *= 0.80
#
# if total_left < total_right:
#     print(f"The winner is left with total time: {total_left:.1f}")
# else:
#     print(f"The winner is right with total time: {total_right:.1f}")


def multiply_my(b,c):
    a=b*c
    return a