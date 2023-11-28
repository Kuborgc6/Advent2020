#file = open('test_input.txt', 'r')
file = open('input.txt', 'r')
lines = [ int(line.split()[0]) for line in file]
#lines = file.readlines()
#lines.append([])

# for i in range(0, len(lines)):
#     lines[i] = int(lines[i][0])

# print(lines)

joltage_adapter = max(lines) + 3
lines.append(joltage_adapter)
starter_joltage = 0

one_dif = 0
three_dif = 0

used_adapter = list()

current_adapter = 0
lines.sort()

for i in range(len(lines)):
    
    if current_adapter + 1 in lines:
        # lines.index(current_adapter + 1)
        one_dif += 1
        current_adapter = current_adapter + 1

    elif current_adapter + 2 in lines:
        # lines.index(current_adapter + 1)
        current_adapter = current_adapter + 2

    elif current_adapter + 3 in lines:
        # lines.index(current_adapter + 1)
        three_dif += 1
        current_adapter = current_adapter + 3

print(one_dif*three_dif)




# Example usage

paths_adapter = [0] * (max(lines) + 1)
paths_adapter[0] = 1
for adapter in lines:
    paths_adapter[adapter] = paths_adapter[adapter - 1] + paths_adapter[adapter - 2] + paths_adapter[adapter - 3]

print(paths_adapter[max(lines)])

# answer = 19208