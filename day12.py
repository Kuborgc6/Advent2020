import math

file = open('input.txt', 'r')
# file = open('test_input.txt', 'r')

lines = [line.split()[0] for line in file]

current_way = 0
corr = [0, 0]
waypoint = [10, 1]

change_position = ['R', 'L']
change_position_library = {90: 1, 180: 2, 270: 3}
change_position_library_RL = {'R': 1, 'L': -1}

for line in lines:
    if line[0] in change_position:
        next_way = change_position_library[int(line[1:])]*change_position_library_RL[line[0]]

        if next_way == 1 or next_way == -3:
            temp = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = -temp
        elif next_way == 2 or next_way == -2:
            waypoint[0] = -waypoint[0]
            waypoint[1] = -waypoint[1]
        else:
            temp = waypoint[0]
            waypoint[0] = -waypoint[1]
            waypoint[1] = temp

    elif line[0] == 'E':
        waypoint[0] += int(line[1:])
    elif line[0] == 'W':
        waypoint[0] -= int(line[1:])
    elif line[0] == 'N':
        waypoint[1] += int(line[1:])
    elif line[0] == 'S':
        waypoint[1] -= int(line[1:])
    else:
        corr[0] += waypoint[0]*int(line[1:])
        corr[1] += waypoint[1]*int(line[1:])

print(abs(corr[0]) + abs(corr[1]))