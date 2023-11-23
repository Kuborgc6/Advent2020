file1 = open('input.txt', 'r')
lines = file1.readlines()

result = 0
for line in lines:
    line = line.split(':')
    [how_many, which_letter] = line[0].split()
    how_many = how_many.split("-")
    how_many = [int(i) for i in how_many]
    if (line[1][how_many[0]] == which_letter or line[1][how_many[1]] == which_letter) and line[1][how_many[0]] != line[1][how_many[1]]:
        result += 1
    #print(how_many)
    #print(which_letter)
    #print(line[1][how_many[0]])
    #print(line[1][how_many[1]])

print(result)