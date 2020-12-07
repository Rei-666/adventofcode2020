
with open("./input.txt") as file:
    text = file.readlines()

bags = {}


def find_bag(bag):
    if bag not in bags:
        for line in text:
            occurrence = line.find("bags")
            if bag in line[:occurrence-1]:
                if "shiny gold" in line[occurrence-1:]:
                    bags[bag] = 1
                    return 1
                if "contain no other" in line:
                    bags[bag] = 0
                    return 0
                bags[bag] = 0
                other_bags = line[occurrence+13:]
                other_bags = other_bags.split(", ")
                for id_of_bag, bags_ in enumerate(other_bags):
                    splited = bags_.split()
                    if find_bag(splited[1] + " " + splited[2]) == 1:
                        bags[bag] = 1
                return bags[bag]

    else:
        return bags[bag]


result = 0
for lines in text:
    place = lines.find("bags")
    if find_bag(lines[:place-1]):
        result += 1

print(result)
