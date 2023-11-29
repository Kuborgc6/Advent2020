import copy

file = open('input.txt', 'r')
# file = open('test_input.txt', 'r')

lines = [line.split()[0] for line in file]
# lines.append([])

# for i in range(0, len(lines)):
#     lines[i] = int(lines[i][0])


layout = list()
for line in lines:
    layout.append(list(line))

max_len_i = len(layout)
max_len_j = len(layout[0])

def change_layout(layout, max_len_i, max_len_j):
    # result_layout = [None]*len(layout)
    # for i in range(len(result_layout)):
    #     result_layout[i] =  list('.'*len(layout[i]))
    result_layout = copy.deepcopy(layout)
    for i in range(max_len_i):
        for j in range(max_len_j):
            if layout[i][j] == 'L':
                result_layout = change_L(i,j,layout,result_layout, max_len_i, max_len_j)
            elif layout[i][j] == '#':
                result_layout = change_taken(i,j,layout,result_layout, max_len_i, max_len_j)
    return result_layout

def change_L(i,j,layout,result_layout, max_len_i, max_len_j):
    if i == 0:
        if j == 0:
            if '#' not in layout[i][j:j+2] and '#' not in layout[i+1][j:j+2]:
                result_layout[i][j] = '#'
        elif j == max_len_j - 1:
            if '#' not in layout[i][j-1:j+1] and  '#' not in layout[i+1][j-1:j+1]:
                result_layout[i][j] = '#'
        else:
            if '#' not in layout[i][j-1:j+2] and  '#' not in layout[i+1][j-1:j+2]:
                result_layout[i][j] = '#'
    elif i == max_len_i - 1:
        if j == 0:
            if '#' not in layout[i-1][j:j+2] and '#' not in layout[i][j:j+2]:
                result_layout[i][j] = '#'
        elif j == max_len_j - 1:
            if '#' not in layout[i-1][j-1:j+1] and  '#' not in layout[i][j-1:j+1]:
                result_layout[i][j] = '#'
        else:
            if '#' not in layout[i-1][j-1:j+2] and  '#' not in layout[i][j-1:j+2]:
                result_layout[i][j] = '#'
    else:
        if j == 0:
            if '#' not in layout[i-1][j:j+2] and '#' not in layout[i][j:j+2] and '#' not in layout[i+1][j:j+2]:
                result_layout[i][j] = '#'
        elif j == max_len_j - 1:
            if '#' not in layout[i-1][j-1:j+1] and  '#' not in layout[i][j-1:j+1] and '#' not in layout[i+1][j:j+1]:
                result_layout[i][j] = '#'
        else:
            if '#' not in layout[i-1][j-1:j+2] and  '#' not in layout[i][j-1:j+2] and  '#' not in layout[i+1][j-1:j+2]:
                result_layout[i][j] = '#'     
    return result_layout

def change_taken(i,j,layout,result_layout, max_len_i, max_len_j):
    adjacent_seats = list()
    if i == 0:
        if j == 0:
            adjacent_seats.append(layout[i][j+1])
            adjacent_seats.extend(layout[i+1][j:j+2])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'

        elif j == max_len_j - 1:
            adjacent_seats.append(layout[i][j-1])
            adjacent_seats.extend(layout[i+1][j-1:j+1])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'
        else:
            adjacent_seats.append(layout[i][j-1])
            adjacent_seats.append(layout[i][j+1])
            adjacent_seats.extend(layout[i+1][j-1:j+2])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'
    elif i == max_len_i - 1:
        if j == 0:
            adjacent_seats.extend(layout[i-1][j:j+2])
            adjacent_seats.append(layout[i][j+1])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'
        elif j == max_len_j - 1:
            adjacent_seats.extend(layout[i-1][j-1:j+1])
            adjacent_seats.append(layout[i][j-1])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'
        else:
            adjacent_seats.extend(layout[i-1][j-1:j+2])
            adjacent_seats.append(layout[i][j-1])
            adjacent_seats.append(layout[i][j+1])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'
    else:
        if j == 0:
            adjacent_seats.extend(layout[i-1][j:j+2])
            adjacent_seats.append(layout[i][j+1])
            adjacent_seats.extend(layout[i+1][j:j+2])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'
        elif j == max_len_j - 1:
            adjacent_seats.extend(layout[i-1][j-1:j+1])
            adjacent_seats.append(layout[i][j-1])
            adjacent_seats.extend(layout[i+1][j-1:j+1])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'
        else:
            adjacent_seats.extend(layout[i-1][j-1:j+2])
            adjacent_seats.append(layout[i][j-1])
            adjacent_seats.append(layout[i][j+1])
            adjacent_seats.extend(layout[i+1][j-1:j+2])
            if adjacent_seats.count('#') >= 4:
                result_layout[i][j] = 'L'     
    return result_layout

chaos = True
test = 0
while(chaos):
    test += 1
    result_layout = change_layout(layout, max_len_i, max_len_j)
    if result_layout == layout:
        chaos = False
    layout = result_layout


all_seats = list()
for line in result_layout:
    all_seats.extend(line)

print(all_seats.count('#'))