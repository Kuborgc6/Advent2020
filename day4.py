#file = open('test_input.txt', 'r')
file = open('input.txt', 'r')
lines = [ line.split() for line in file]
#lines = file.readlines()

passpord_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"]
eye_colour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
lines.append([])
temp_line = list()
result = 0
test = 0

for line in lines:
    
    if line:
        temp_line.extend(line)
    else:
        #print(temp_line)
        #passport = list()
        passport_key = [ temp.split(":")[0] for temp in temp_line]
        passport_value = [ temp.split(":")[1] for temp in temp_line]
        
        check =  all(item in passport_key for item in passpord_fields)
        invalid = True
        if check:
            byr = int(passport_value[passport_key.index('byr')])
            if byr < 1920 or byr > 2002 or len(passport_value[passport_key.index('byr')]) != 4:
                invalid = False
                test += 1
                
            iyr = int(passport_value[passport_key.index('iyr')])
            if iyr < 2010 or iyr > 2020 or len(passport_value[passport_key.index('iyr')]) != 4:
                invalid = False
                test += 1
                
            eyr = int(passport_value[passport_key.index('eyr')])
            if eyr < 2020 or eyr > 2030 or len(passport_value[passport_key.index('eyr')]) != 4:
                invalid = False
                test += 1

            hgt = passport_value[passport_key.index('hgt')]
            if hgt[-2:] == "cm":
                hgt = int(hgt.replace("cm",""))
                if hgt < 150 or hgt > 193:
                    invalid = False
                    test += 1
            elif hgt[-2:] == "in":
                hgt = int(hgt.replace("in",""))
                if hgt < 59 or hgt > 76:
                    invalid = False
                    test += 1
            elif hgt[-2:] != "in" and hgt[-2:] != "cm":
                invalid = False
                test += 1

            hcl = passport_value[passport_key.index('hcl')]
            if hcl[0] != "#" or len(hcl[1:]) != 6:
                invalid = False
                test += 1

            if passport_value[passport_key.index('ecl')] not in eye_colour:
                invalid = False
                test += 1

            if len(passport_value[passport_key.index('pid')]) != 9:
                invalid = False
                test += 1

            if invalid:
                result += 1
        temp_line = list()

print(test)
print(result)