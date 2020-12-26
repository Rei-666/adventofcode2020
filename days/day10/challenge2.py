
with open("./test_input.txt") as file:
    text = file.readlines()

text = [int(x[:-1]) for x in text]
text.sort()
solution = 1
ps = 0
for number in range(len(text)):
    try:
        difference = text[number + 1] - text[number]
    except IndexError:
        break
    if difference != 3:
        for i in range(1, 4):
            try:
                difference = text[number+i] - text[number+i-1]
            except IndexError:
                break
            if difference == 1:
                ps += 1
        solution *= 4 if ps == 3 else 1
    ps = 0

print(solution)



print(text)
'''for number in range(len(text)):
    for i in range(1, 4):
        try:
            difference = text[number+i]-text[number+i-1]
            print(f"Liczba: {text[number+i]} - {text[number+i-1]}")
        except IndexError:
            break
        if difference == 1:
            result_1 += 1
        elif difference == 3:
            result_3 = 1
            solutions += result_1+result_3
            break
    if result_1 == 3:
        solutions += 3
    print(solutions)
    result_1 = 0
    result_3 = 0'''


