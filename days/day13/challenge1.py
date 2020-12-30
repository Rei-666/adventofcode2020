with open("input.txt") as file:
    text = file.readlines()

timestamp = int(text[0])
buses = [int(x) for x in text[1].split(",") if x != "x"]
time_to_wait = {(y - timestamp % y): y for y in buses}
print(min(time_to_wait)*time_to_wait[min(time_to_wait)])
