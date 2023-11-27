import random

#file = open('test_input.txt', 'r')
file = open('input.txt', 'r')
lines = [ line.split() for line in file]
#lines = file.readlines()
#lines.append([])

#print(lines)
for i in range(0, len(lines)):
    lines[i] = int(lines[i][0])

# rand_list = list(range(1,26))
# random.shuffle(rand_list)
# print(rand_list)

# for value in lines:
#     rand_list.append(int(value[0]))
# print(rand_list)

preamble = 25

def find_invalid(rand_list, preamble):
    for i in range(preamble,preamble+len(rand_list[preamble:])):
        sum_list = list()
        for j in range(i-preamble,i):
            for k in range(j,i):
                sum_list.append(rand_list[j]+rand_list[k])
        if rand_list[i] not in sum_list:
            for j in range(i):
                temp_result = rand_list[j]
                list_result = list()
                list_result.append(rand_list[j])
                while(temp_result < rand_list[i]):
                    j += 1
                    temp_result += rand_list[j]
                    list_result.append(rand_list[j])
                if rand_list[i] == temp_result:
                    result = min(list_result) + max(list_result)
                    return result

print(find_invalid(lines, preamble))