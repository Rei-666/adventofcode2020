
with open("./input.txt") as file:
    text = file.readlines()



text = [int(x[:-1]) for x in text]
text.sort()
result_1 = 1
result_3 = 1
for number in range(len(text)):
    try:
        difference = text[number+1]-text[number]
    except IndexError:
        break
    if difference == 1:
        result_1 += 1
    elif difference == 3:
        result_3 += 1
print(result_1*result_3)

