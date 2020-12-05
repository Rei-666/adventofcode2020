
with open("./input.txt") as file:
    text = file.readlines()

result = 0;

for line in text:
    line = line.split(' ')
    numbers = line[0]
    numbers = numbers.split('-')
    min_number = int(numbers[0])
    max_number = int(numbers[1])
    char = line[1][0]
    input_text = line[2]
    number_of_occurences = input_text.count(char)
    print(f"Literka: {char}, ma występować od {min_number} do {max_number} w tekście {input_text}")
    if number_of_occurences in range(min_number, max_number+1):
        result += 1
print(result)
