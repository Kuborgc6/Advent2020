import math

file = open('input.txt', 'r')
# file = open('test_input.txt', 'r')

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

bus_IDs = lines[1].split(',')
t = 0

not_now = True
required_t = list()
for id in bus_IDs:
    if id != 'x':
        required_t.append(-bus_IDs.index(id)%int(id))

while('x' in bus_IDs):
    bus_IDs.remove('x')

for i in range(0, len(bus_IDs)):
    bus_IDs[i] = int(bus_IDs[i])

nk = bus_IDs 
yk = required_t
M_chinise = math.prod(nk)
result = 0
for i in range(len(nk)):
    Mi = M_chinise/nk[i]
    for g in range(max(nk)):
        e = Mi*g
        if e % nk[i] == 1:
            result += e*yk[i]
            break

print(result%M_chinise)


from math import prod

def chinese_remainder_theorem(moduli, remainders):
    # Chinese Remainder Theorem implementation
    product = prod(moduli)
    result = sum(r * pow(product // m, -1, m) * (product // m) for m, r in zip(moduli, remainders))
    return result % product

def earliest_timestamp(bus_ids):
    moduli = []
    remainders = []

    for i, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            moduli.append(int(bus_id))
            remainders.append((-i) % int(bus_id))

    return chinese_remainder_theorem(moduli, remainders)

# Example usage:
bus_ids = lines[1].split(',')
result = earliest_timestamp(bus_ids)
print(result)
