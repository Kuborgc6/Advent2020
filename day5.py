#file = open('test_input.txt', 'r')
file = open('input.txt', 'r')
lines = [ line.split()[0] for line in file]
#lines = file.readlines()
all_seats = list(range(9*8-1,119*8))
result = list()
for line in lines:
    ticket_row = line[:7]
    ticket_seat = line[-3:]
    rows = [0,127]
    seats = [0,7]
    row = 0
    seat = 0
    for c in ticket_row:
        if rows[1] - rows[0] == 1:
            if c == "F":
                row = rows[0]
            else:
                row = rows[1]
        elif c == "F":
            rows[1] = rows[1] - (rows[1] - rows[0] + 1)/2
        else:
            rows[0] = rows[0] + (rows[1] - rows[0] + 1)/2

    for c in ticket_seat:
        if seats[1] - seats[0] == 1:
            if c == "L":
                seat = seats[0]
            else:
                seat = seats[1]
        elif c == "L":
            seats[1] = seats[1] - (seats[1] - seats[0] + 1)/2
        else:
            seats[0] = seats[0] + (seats[1] - seats[0] + 1)/2
    
    result.append(row*8+seat)

final_result = list(set(all_seats).difference(result))

print(final_result)
#print(result)