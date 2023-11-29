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

def search_adjacent(layout, i, j, max_len_i, max_len_j):
    result = list()

    k = i - 1 
    l = j - 1
    while(k >= 0 and l >= 0):
        if layout[k][l] != '.':
            result.append(layout[k][l])
            break
        k -= 1
        l -= 1
    
    k = i - 1 
    while(k >= 0):
        if layout[k][j] != '.':
            result.append(layout[k][j])
            break
        k -= 1

    k = i - 1 
    l = j + 1
    while(k >= 0 and l <= max_len_j - 1):
        if layout[k][l] != '.':
            result.append(layout[k][l])
            break
        k -= 1 
        l += 1

    l = j - 1
    while(l >= 0):
        if layout[i][l] != '.':
            result.append(layout[i][l])
            break
        l -= 1

    k = i + 1 
    l = j - 1
    while(k <= max_len_i - 1 and l >= 0):
        if layout[k][l] != '.':
            result.append(layout[k][l])
            break
        k += 1
        l -= 1

    k = i + 1 
    while(k <= max_len_i - 1):
        if layout[k][j] != '.':
            result.append(layout[k][j])
            break
        k += 1

    k = i + 1 
    l = j + 1
    while(k <= max_len_i - 1 and l <= max_len_j - 1):
        if layout[k][l] != '.':
            result.append(layout[k][l])
            break
        k += 1
        l += 1
    
    l = j + 1
    while(l <= max_len_j - 1):
        if layout[i][l] != '.':
            result.append(layout[i][l])
            break
        l += 1

    return result

def change_L(i,j,layout,result_layout, max_len_i, max_len_j):
    adjacent_seats = search_adjacent(layout, i, j, max_len_i, max_len_j)
    if '#' not in adjacent_seats:
        result_layout[i][j] = '#'
    return result_layout

def change_taken(i,j,layout,result_layout, max_len_i, max_len_j):
    adjacent_seats = search_adjacent(layout, i, j, max_len_i, max_len_j)
    
    if adjacent_seats.count('#') >= 5:
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