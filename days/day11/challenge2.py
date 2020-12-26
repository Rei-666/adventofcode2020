from copy import deepcopy

with open("./input.txt") as file:
    text = file.readlines()


def get_occupied_seat(seats, row, column, direction):
    row += direction[0]
    column += direction[1]
    try:
        seat_symbol = seats[row][column]
    except IndexError:
        return 0
    if seat_symbol == "#":
        return 1
    elif seat_symbol == "L":
        return 0
    elif seat_symbol == "E":
        return 0
    else:
        return get_occupied_seat(seats, row, column, direction)


def get_seats(seats, row, column):
    occupied = 0
    for i in range(-1, 2):
        for x in range(-1, 2):
            if x == 0 and i == 0:
                continue
            occupied += get_occupied_seat(seats, row, column, (i, x))
    return occupied


arr = [["E" for i in range(len(text[0])+2)]]
for line in text:
    line = "E" + line[:-1] + "E"
    arr.append(list(line))
arr.append(["E" for i in range(len(text[0])+2)])

arr2 = deepcopy(arr)
arr2.append("E")

while arr != arr2:
    arr = deepcopy(arr2)
    for number in range(len(arr)):
        for seat_id, seat in enumerate(arr[number]):
            if seat != "." and seat != "E":
                occupied = get_seats(arr, number, seat_id)
                if seat == "L" and occupied == 0:
                    arr2[number][seat_id] = "#"
                elif seat == "#" and occupied >= 5:
                    arr2[number][seat_id] = "L"

x = ""
for line in arr:
    print(line)
    x = x + str(line)
print(x.count("#"))
