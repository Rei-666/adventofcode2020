
with open("./input.txt") as file:
    text = file.readlines()

result_number = 776203571

text = [int(x[:-1]) for x in text]
value = 0

for number in range(len(text)):
    for line_number, x in enumerate(text[number:]):
        value += x
        if value == result_number and x!=result_number:
            correct_numbers = text[number:line_number+number+1]
            print(f"Sum of max and min: {max(correct_numbers)+min(correct_numbers)} All numbers: {correct_numbers}")
            break
        elif value > result_number:
            value = 0
            break


