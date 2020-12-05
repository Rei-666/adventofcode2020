
with open("input.txt") as file:
    text = file.read()

data = text.split()
data = [int(i) for i in data]

for item in data:
    if 2020-item in data:
        print(item*(2020-item))
        break

