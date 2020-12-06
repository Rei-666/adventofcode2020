
with open("./input.txt") as file:
    text = file.readlines()

result = 0
answers = set()
for line in text:
    if line == "\n":
        result += len(answers)
        print(f"Answers: {len(answers)}")
        answers = set()
    line = line.replace("\n", "")
    if line: answers.update(line)

print(result)
