number_of_rooms = int(input())

room_number = 0
needed_chairs = 0
visitors_count = 0
for room in range(number_of_rooms):
    number_of_visitors_and_chairs = input().split()
    chairs = len(number_of_visitors_and_chairs[0])
    visitors = int(number_of_visitors_and_chairs[1])
    room_number += 1
    needed_chairs += chairs
    visitors_count += visitors
    if visitors > chairs:
        chairs_diff = visitors - chairs
        print(f"{chairs_diff} more chairs needed in room {room_number}")
if visitors_count <= needed_chairs:
    free_chairs = needed_chairs - visitors_count
    print(f"Game On, {free_chairs} free chairs left")




