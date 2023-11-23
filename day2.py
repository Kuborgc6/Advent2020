file1 = open('input.txt', 'r')
lines = file1.readlines()

result = 0
for line in lines:
    line = line.split(':')
    [how_many, which_letter] = line[0].split()
    how_many = how_many.split("-")
    how_many = [int(i) for i in how_many]
    if line[1].count(which_letter) >= how_many[0] and line[1].count(which_letter) <= how_many[1]:
        result += 1
    #print(how_many)
    #print(which_letter)

print(result)