import re
import copy

file = open('input.txt', 'r')
# file = open('test_input.txt', 'r')

lines = [line.split() for line in file]

result_dict = dict()
prefix = '0b'
for line in lines:
    if line[0] == 'mask':
        mask = line[-1]
        # ones_id = [i.start() for i in re.finditer('1', line[-1])]
        # zeros_id = [i.start() for i in re.finditer('0', line[-1])]
        len_mask = len(line[-1])
    else:
        cell = int(line[0][4:-1])
        value = int(line[-1])
        value_bin = bin(value)[2:]
        cell_bin = bin(cell)[2:]

        result = list('0'*len_mask)
        cell_results = list()

        if len(cell_bin) < len_mask:
            offset = len_mask - len(cell_bin)
            for i in range(offset):
                if mask[i] == 'X':
                    result[i] = 'X'
                elif mask[i] == '1':
                    result[i] = '1'
            for i in range(len(cell_bin)):
                if mask[i + offset] == 'X':
                    result[i + offset] = 'X'
                elif mask[i + offset] == '1':
                    result[i + offset] = '1'
                else:
                    result[i + offset] = cell_bin[i]
            
            Xs_id = [i for i, x in enumerate(result) if x == 'X']
            
            for id in Xs_id:
                if cell_results:
                    temp_list = list()
                    for cell_result in cell_results:
                        temp = copy.deepcopy(cell_result)
                        temp[id] = '0'
                        temp_list.append(temp)

                        temp = copy.deepcopy(cell_result)
                        temp[id] = '1'
                        temp_list.append(temp)
                    cell_results.clear()
                    cell_results = temp_list
                else:
                    temp = copy.deepcopy(result)
                    temp[id] = '0'
                    cell_results.append(temp)

                    temp = copy.deepcopy(result)
                    temp[id] = '1'
                    cell_results.append(temp)

            for cell_id in cell_results:
                cell_id = int(prefix + ''.join(cell_id), 2)
                result_dict[cell_id] = value
        else:
            print('XD')
        #print(''.join(result))
        #result_dict[cell] = int(prefix + ''.join(result), 2)

print(sum(result_dict.values()))