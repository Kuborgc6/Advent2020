#file = open('test_input.txt', 'r')
file = open('input.txt', 'r')

lines = [ line.split() for line in file]

for i in range(len(lines)):
    lines[i] = [c for c in lines[i][0]]


max_len = len(lines[0])
how_many = len(lines)
#print(lines[1][3]) #first value row, second value column
#print(max_len)
#print(how_many)

all_slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]


results = 1
for slope in all_slopes:
    result = 0
    pos = [0,0]
    for i in range(how_many - 1):
        pos[0] += slope[0]
        pos[1] += slope[1]
        if pos[1] > max_len - 1:
            pos[1] = pos[1] % max_len
        if pos[0] > how_many:
            break
        if lines[pos[0]][pos[1]] == '#':
            result += 1
    results *= result
print(results)