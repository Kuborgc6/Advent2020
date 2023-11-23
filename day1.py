file1 = open('input.txt', 'r')
Lines = file1.readlines()

values = [int(i) for i in Lines]
values.sort()

for i in range(len(values)):
    for j in range(i+1,len(values)):
        if values[i] + values[j] == 2020:
            result = values[i] * values[j]
        if values[i] + values[j] > 2020:
            break
print (result)