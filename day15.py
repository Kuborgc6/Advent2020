file = open('input.txt', 'r')
# file = open('test_input.txt', 'r')

lines = [line.split() for line in file]

values =lines[0][0].split(',')
for i in range(0, len(values)):
    values[i] = int(values[i])


current = 0
i = 1
values_dict = dict()
values_dict_new = dict()

for value in values:
    current = value
    values_dict[current] = i
    values_dict_new[current] = i
    i += 1

last_spoken = current
while(i <= 30000000):
    if last_spoken not in values_dict.keys():
        current = 0
        
    else:
        space = (i - 1) - values_dict[last_spoken] 
        current = space

    values_dict[last_spoken] = i - 1

    last_spoken = current
    i += 1

print(current)