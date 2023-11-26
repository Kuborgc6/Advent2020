#file = open('test_input.txt', 'r')
file = open('input.txt', 'r')
lines = [ line.split() for line in file]
#lines = file.readlines()
lines.append([])

#print(lines)
result = 0
temp = set()
first_obj = True
for line in lines:
    if line and first_obj == True:
        temp = set(line[0])
        first_obj = False
    elif line:
        temp = temp.intersection(set(line[0]))
    else:
        result += len(temp)
        temp = set()
        first_obj = True

print(result)