from copy import deepcopy

with open("./input.txt") as file:
    text = file.readlines()

arr = [["." for i in range(len(text[0])+2)]]
for line in text:
    line = "." + line + "."
    arr.append(list(line))
arr.append(["." for i in range(len(text[0])+2)])

occupied = 0
arr2 = deepcopy(arr)
arr2.append(".")
while arr != arr2:
    arr = deepcopy(arr2)
    for number in range(len(arr)):
        for seat_id, seat in enumerate(arr[number]):
            if seat != ".":
                occupied += arr[number - 1][seat_id - 1:seat_id + 2].count("#")
                occupied += arr[number][seat_id - 1].count("#")
                occupied += arr[number][seat_id + 1].count("#")
                occupied += arr[number + 1][seat_id - 1:seat_id + 2].count("#")
                if seat == "L" and occupied == 0:
                    arr2[number][seat_id] = "#"
                elif seat == "#" and occupied >= 4:
                    arr2[number][seat_id] = "L"
                occupied = 0

x = ""
for line in arr:
    print(line)
    x = x + str(line)
print(x.count("#"))