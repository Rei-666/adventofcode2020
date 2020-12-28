
with open("./input.txt") as file:
    text = file.readlines()

text = [int(x[:-1]) for x in text]
text.sort()
text.append(text[-1]+3)
text.insert(0, 0)
solution = 1
ps = 0
for number in range(len(text)):
    try:
        difference = text[number + 1] - text[number]
    except IndexError:
        break
    if difference == 1:
        ps += 1
    elif difference == 3:
        if ps == 2:
            solution *= 2
        elif ps == 3:
            solution *= 4
        elif ps == 4:
            solution *= 7
        ps = 0
        continue

print(solution)