import math

file = open('input.txt', 'r')
# file = open('test_input.txt', 'r')

lines = [line.split()[0] for line in file]

current_way = 0
corr = [0, 0]

positions = ['E', 'S', 'W', 'N']
positions_lib = {'E': 0.5, 'S': -1, 'W': -0.5, 'N': 1}
change_position = ['R', 'L']
change_position_library = {90: 1, 180: 2, 270: 3}
change_position_library_RL = {'R': 1, 'L': -1}

for line in lines:
    if line[0] in change_position:
        current_way = (current_way + change_position_library[int(line[1:])]*change_position_library_RL[line[0]])%4
    elif line[0] == 'E':
        corr[0] += int(line[1:])
    elif line[0] == 'W':
        corr[0] -= int(line[1:])
    elif line[0] == 'N':
        corr[1] += int(line[1:])
    elif line[0] == 'S':
        corr[1] -= int(line[1:])
    else:
        way = positions_lib[positions[current_way]]
        corr[abs(round(way))] += way/abs(way)*int(line[1:])

print(abs(corr[0])+abs(corr[1]))