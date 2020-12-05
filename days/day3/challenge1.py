with open("./input.txt") as file:
    text = [line[:-1] for line in file.readlines()]

text.pop(0)


def count_tress(right, down):
    x = 1
    result = 0
    for count, line in enumerate(text):
        if (count+1)%down == 0:
            x = x + right
            if x/len(line) >= 1:
                x = x%len(line)
            #print(f"{'Drzewo' if line[x-1]=='#' else 'Pusto'}, Lina nr: {count}, miejsce znaku {x}, znak na tym miejscu: {line[x-1]}, tekst w linii: {line}")
            if line[x-1]=='#':
                result = result+1
    return result

finish = 0
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for item in slopes:
    finish = count_tress(item[0], item[1]) if finish == 0 else finish*count_tress(item[0], item[1])
print(finish)

