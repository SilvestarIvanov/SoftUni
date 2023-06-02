line_one = list(map(int, input().split()))
line_two = list(map(int, input().split()))
line_three = list(map(int, input().split()))

combined_list = [line_one, line_two, line_three]

first_player_win = False
second_player_win = False

for line in combined_list:
    if line[0] == line[1] == line[2]:
        if line[0] == 1:
            first_player_win = True
        elif line[0] == 2:
            second_player_win = True
for x, y, z in zip(line_one, line_two, line_three):
    if x == y == z:
        if x == 1:
            first_player_win = True
        elif x == 2:
            second_player_win = True
if line_one[0] == line_two[1] == line_three[2]:
    if line_one[0] == 1:
        first_player_win = True
    elif line_one[0] == 2:
        second_player_win = True
if line_one[2] == line_two[1] == line_three[0]:
    if line_one[2] == 1:
        first_player_win = True
    elif line_one[2] == 2:
        second_player_win = True

if first_player_win:
    print("First player won")
elif second_player_win:
    print("Second player won")
else:
    print("Draw!")
