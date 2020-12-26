
with open("./input.txt") as file:
    text = file.readlines()


text = [int(x[:-1]) for x in text]

for number, line in enumerate(text[25:]):
    flag = False
    last_25_numbers = text[number:number+25]
    for number_to_subtract in last_25_numbers:
        if int(line)-int(number_to_subtract) in last_25_numbers:
            flag = True
            break
    if flag is False:
        print(line)
