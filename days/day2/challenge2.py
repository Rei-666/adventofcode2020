
with open("./input.txt") as file:
    text = file.readlines()

result = 0

for line in text:
    line = line.split(' ')
    numbers = line[0]
    numbers = numbers.split('-')
    min_number = int(numbers[0])
    max_number = int(numbers[1])
    char = line[1][0]
    input_text = line[2]

    print(f"Literka: {char}, ma występować od {min_number} do {max_number} w tekście {input_text}")

    if input_text[min_number-1] == char and input_text[max_number-1] != char:
        result += 1
        print(f"Git literka {char} jest taka sama jak {input_text[min_number-1]} lub {input_text[max_number-1]}")
    elif input_text[min_number-1] != char and input_text[max_number-1] == char:
        result += 1
        print(f"Git literka {char} jest taka sama jak {input_text[min_number - 1]} lub {input_text[max_number - 1]}")


print(result)
