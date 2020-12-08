
with open("./input.txt") as file:
    text = file.readlines()


def run_line(number_of_line, value=0, runned_lines=None):
    if runned_lines is None:
        runned_lines = []

    command = text[number_of_line][:3]
    number = int(text[number_of_line][3:])

    if number_of_line+1 >= len(text):
        return f"mamy to {value} {command} {number}"

    if number_of_line in runned_lines:
        return value

    runned_lines.append(number_of_line)

    if "acc" in command:
        return run_line(number_of_line+1, value+number, runned_lines)
    elif "jmp" in command:
        return run_line(number_of_line+number, value, runned_lines)
    else:
        return run_line(number_of_line+1, value, runned_lines)


for line_number, line in enumerate(text):

    # I realy don't like this mess, going to refactor it later
    if "nop" in line:
        text[line_number] = text[line_number].replace("nop", "jmp")
    elif "jmp" in line:
        text[line_number] = text[line_number].replace('jmp', 'nop')

    result = run_line(0)
    if type(result) is str:
        print(result)
        break

    line = text[line_number]
    if "nop" in line:
        text[line_number] = text[line_number].replace("nop", "jmp")
    elif "jmp" in line:
        text[line_number] = text[line_number].replace("jmp", "nop")

