with open("./input.txt") as file:
    text = file.readlines()
text = [x[:-1] for x in text]


class Ferry:
    DIRECTIONS = {"N": 0,
                  "E": 90,
                  "S": 180,
                  "W": 270}

    def __init__(self):
        self.up = 0
        self.right = 0
        self.waypoint_up = 1
        self.waypoint_right = 10

    def move_in_direction(self, value, direction):
        if direction == "N":
            self.waypoint_up += value
        elif direction == "E":
            self.waypoint_right += value
        elif direction == "S":
            self.waypoint_up -= value
        elif direction == "W":
            self.waypoint_right -= value

    def rotate(self, direction, value, degree=0):
        if direction == "R":
            degree += value
        elif direction == "L":
            degree -= value
            if degree < 0:
                degree += 360
        if degree == 90:
            self.waypoint_right, self.waypoint_up = self.waypoint_up, self.waypoint_right * (-1)
        elif degree == 180:
            self.waypoint_up *= -1
            self.waypoint_right *= -1
        elif degree == 270:
            self.waypoint_right, self.waypoint_up = self.waypoint_up * (-1), self.waypoint_right

    def forward(self, value):
        self.up += self.waypoint_up * value
        self.right += self.waypoint_right * value

    def get_manhattan_distance(self):
        return abs(self.up) + abs(self.right)


ferry = Ferry()

for command in text:
    letter = command[0]
    value = int(command[1:])
    if letter in ferry.DIRECTIONS:
        ferry.move_in_direction(value, letter)
    elif letter in ["R", "L"]:
        ferry.rotate(letter, value)
    elif letter == "F":
        ferry.forward(value)

print(ferry.get_manhattan_distance())
