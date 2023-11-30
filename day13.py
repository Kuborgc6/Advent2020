import math

# file = open('input.txt', 'r')
file = open('test_input.txt', 'r')

lines = [line.split()[0] for line in file]

earliest_timestamp = int(lines[0])
bus_IDs = lines[1].split(',')

while('x' in bus_IDs):
    bus_IDs.remove('x')

for i in range(0, len(bus_IDs)):
    bus_IDs[i] = int(bus_IDs[i])

divider = list()
time_dep = list()

for id in bus_IDs:
    devider_temp = math.floor(earliest_timestamp/id)
    divider.append(devider_temp)
    time_dep.append((devider_temp + 1) * id)

result = bus_IDs[time_dep.index(min(time_dep))]*(min(time_dep)-earliest_timestamp)


print(result)

### Part Two