#file = open('test_input.txt', 'r')
file = open('input.txt', 'r')
lines = [ line.split() for line in file]
#lines = file.readlines()
#lines.append([])

#print(lines)




def acc(value, i, accumulator, first_time, was_there):
    if value[0] == "-":
        accumulator -= int(value[1:])
    else:
        accumulator += int(value[1:])
    i += 1
    if i in was_there:
        first_time = False
    else:
        was_there.append(i)
    return was_there, i, accumulator, first_time

def jmp(value, i, first_time, was_there):
    if value[0] == "-":
        i -= int(value[1:])
    else:
        i += int(value[1:])

    if i in was_there:
        first_time = False
    else:
        was_there.append(i)
    return was_there, i, first_time

def nop(i, first_time, was_there):
    i += 1
    if i in was_there:
        first_time = False
    else:
        was_there.append(i)
    return was_there, i, first_time

def check_command(lines, was_there, first_time, i, accumulator):
    while(first_time and i < len(lines)):
        command, value = lines[i]
        if command == "acc":
            was_there, i, accumulator, first_time = acc(value, i, accumulator, first_time, was_there)
        elif command == "jmp":
            was_there, i, first_time = jmp(value, i, first_time, was_there)
        else: 
            was_there, i, first_time = nop(i, first_time, was_there)
    return first_time, accumulator


print(check_command(lines, list(), True, 0, 0))

for j in range(len(lines)):
        temp_lines = list()
        temp_lines = lines.copy()
        temp_temp_lines = list()
        #temp_lines.append('test')
        #temp_lines.pop()
        
        first_time = True
        accumulator = 0
        i = 0
        was_there = list()
        first_time = True
        if lines[j][0] == "jmp":
            # temp_lines[j][0] = "nop"
            temp_temp_lines = temp_lines[:j]
            temp_temp_lines.append(["nop",temp_lines[j][1]])
            temp_temp_lines[j+1:] = temp_lines[j+1:]
            first_time, accumulator = check_command(temp_temp_lines, was_there, first_time, i, accumulator)
            if first_time:
                result = accumulator
        elif lines[j][0] == "nop":
            # temp_lines[j][0] = "jmp"
            temp_temp_lines = temp_lines[:j]
            temp_temp_lines.append(["jmp",temp_lines[j][1]])
            temp_temp_lines[j+1:] = temp_lines[j+1:]
            first_time, accumulator = check_command(temp_temp_lines, was_there, first_time, i, accumulator)
            if first_time:
                result = accumulator

print(result)