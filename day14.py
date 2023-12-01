import re

file = open('input.txt', 'r')
# file = open('test_input.txt', 'r')

lines = [line.split() for line in file]

result_dict = dict()
prefix = '0b'
for line in lines:
    if line[0] == 'mask':
        mask = line[-1]
        ones_id = [i.start() for i in re.finditer('1', line[-1])]
        zeros_id = [i.start() for i in re.finditer('0', line[-1])]
        len_mask = len(line[-1])
    else:
        cell = int(line[0][4:-1])
        value = int(line[-1])
        value_bin = bin(value)[2:]

        result = list('0'*len_mask)

        if len(value_bin) < len_mask:
            offset = len_mask - len(value_bin)
            for i in range(offset):
                if mask[i] != 'X':
                    result[i] = mask[i]
            for i in range(len(value_bin)):
                if mask[i + offset] == 'X':
                    result[i + offset] = value_bin[i]
                else:
                    result[i + offset] = mask[i + offset]
        else:
            print('XD')
        #print(''.join(result))
        result_dict[cell] = int(prefix + ''.join(result), 2)

print(sum(result_dict.values()))