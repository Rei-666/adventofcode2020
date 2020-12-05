
with open("./input.txt") as file:
    text = file.readlines()


def get_half(string, min_n=0, max_n=127):
    if string == "":
        return max_n
    if string[0] == "F" or string[0] == "L":
        max2_n = int((max_n-min_n-1)/2 + min_n)
        return get_half(string[1:], min_n, max2_n)
    elif string[0] == "B" or string[0] == "R":
        min2_n = int((max_n-min_n+1)/2 + min_n)
        return get_half(string[1:], min2_n, max_n)


seat_ids = []
for lines in text:
    row = get_half(lines[:7])
    column = get_half(lines[7:10], max_n=7)
    seat_id = row * 8 + column
    seat_ids.append(seat_id)

seat_ids.sort()

numbers = [n for n in range(seat_ids[0], seat_ids[-1])]

z = set(numbers) - set(seat_ids)

print(list(z)[0])
