
with open("input.txt") as file:
    text = file.read()

data = text.split()
data = [int(i) for i in data]

for item in data:
    temp_data = data
    temp_data.remove(item)
    for item2 in temp_data:
        if 2020-item-item2 in temp_data:
            print((2020-item-item2)*item2*item)
            break
