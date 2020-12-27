with open("./input.txt") as file:
    text = file.readlines()
text = [x[:-1] for x in text]


class Ferry:
    DIRECTIONS = {"N": 0,
                  "E": 90,
                  "S": 180,
                  "W": 270}

    def __init__(self):
        self.degree = 90
        self.direction = self.get_direction()
        self.up = 0
        self.right = 0

    def run_in_direction(self, value, direction=None):
        if direction is None:
            direction = self.direction
        if direction == "N":
            self.up += value
        elif direction == "E":
            self.right += value
        elif direction == "S":
            self.up -= value
        elif direction == "W":
            self.right -= value

    def rotate(self, direction, value):
        if direction == "R":
            self.degree += value
        elif direction == "L":
            self.degree -= value
        self.direction = self.get_direction()

    def get_manhattan_distance(self):
        return abs(self.up) + abs(self.right)

    def get_direction(self):
        if self.degree < 0:
            self.degree += 360
        return {0: "N", 90: "E", 180: "S", 270: "W"}[self.degree % 360]


ferry = Ferry()

for command in text:
    letter = command[0]
    value = int(command[1:])
    if letter in ferry.DIRECTIONS:
        ferry.run_in_direction(value, letter)
    elif letter in ["R", "L"]:
        ferry.rotate(letter, value)
    elif letter == "F":
        ferry.run_in_direction(value)

print(ferry.get_manhattan_distance())


