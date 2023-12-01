# file = open('input.txt', 'r')
file = open('test_input.txt', 'r')

lines = [line.split() for line in file]

values =lines[0][0].split(',')
for i in range(0, len(values)):
    values[i] = int(values[i])


current = 0
i = 1
values_dict = dict()


for value in values:
    current = value
    values_dict[current] = i
    i += 1

while(i < 2020):
    temp = 0
    if current in values_dict.keys():
        space = (i - 1) - values_dict[current] 
        current = space
    else:
        current = 0
    temp = values_dict[current]
    values_dict[current] = i
    i += 1

