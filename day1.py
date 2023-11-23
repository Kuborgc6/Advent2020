file1 = open('input.txt', 'r')
Lines = file1.readlines()

values = [int(i) for i in Lines]
values.sort()
result = list()
for i in range(len(values)):
    for j in range(i+1,len(values)):
        if values[i] + values[j] > 2020:
            break
        for k in range(j+1,len(values)):
            if values[i] + values[j] + values[k] == 2020:
                result.append(values[i] * values[j] * values[k])
            if values[i] + values[j] + values[k] > 2020:
                break
print (result)

