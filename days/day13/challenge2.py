with open("input.txt") as file:
    text = file.readlines()

buses = [(x, int(y)) for x, y in enumerate(text[1].split(",")) if y != "x"]
i = 0
flag = 0
max_value = max(buses, key=lambda item: item[1])
buses.remove(max_value)
while flag == 0:
    i += 1
    value = max_value[1]*i-max_value[0]
    for bus in buses:
        if (value+bus[0]) % bus[1] != 0:
            flag = 0
            break
        flag = 1
print(value)
# extremely inefficient
