
with open("./input.txt") as file:
    text = file.readlines()

result = 0
answers = []
number_of_groups = 0

for line in text:
    if line == "\n":
        print(f"Answers: {answers}, nog: {number_of_groups}")
        for letter in set(answers):
            if answers.count(letter) == number_of_groups:
                result += 1
        number_of_groups = 0
        answers = []
    else:
        line = line.replace("\n", "")
        for letter in line:
            answers.append(letter)
        number_of_groups += 1

print(result)


