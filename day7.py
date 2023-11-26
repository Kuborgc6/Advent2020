#file = open('test_input.txt', 'r')
file = open('input.txt', 'r')
lines = [ line.split() for line in file]
#lines = file.readlines()
#lines.append([])

#print(lines)

my_bag = "shiny gold"
main_name_list = list()
which_inside_list = list()
how_many_list = list()
for line in lines:
    how_many = list()
    which_inside = list()
    main_name = line[0] + ' ' + line[1]
    while len(line[4:]) > 3:
        temp_name = line[5] + ' ' + line[6]
        how_many.append(int(line[4]))
        which_inside.append(temp_name)
        del line[4:8]
    main_name_list.append(main_name)
    which_inside_list.append(which_inside)
    how_many_list.append(how_many)

def find_bag(name):
    result = 0
    what_bag = set()

    for i in range(len(main_name_list)):
        if name in which_inside_list[i]:
            result += 1
            what_bag.add(main_name_list[i])

    return result, what_bag

result_bags = set()
def rec_find_bag(name, result_bags):
    result = 0

    result_temp, what_bag_temp = find_bag(name)
    result += result_temp
    result_bags.update(what_bag_temp)

    if what_bag_temp:
        for bag in what_bag_temp:
            result_temp, result_bags = rec_find_bag(bag, result_bags)
        result += result_temp
        return result, result_bags
    else:
        return result, result_bags

    
result, result_bags = rec_find_bag(my_bag,result_bags)
print(result)
print(len(result_bags))