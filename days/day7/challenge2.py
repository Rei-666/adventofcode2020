
with open("./input.txt") as file:
    text = file.readlines()

bags = {}


def find_bag(bag):
    if bag not in bags:
        for line in text:
            occurrence = line.find("bags")
            if bag in line[:occurrence-1]:
                if "contain no other" in line:
                    bags[bag] = 1
                    return 1
                bags[bag] = 1
                other_bags = line[occurrence+13:]
                other_bags = other_bags.split(", ")
                for id_of_bag, bags_ in enumerate(other_bags):
                    splitted = bags_.split()
                    color = splitted[1] + " " + splitted[2]
                    bags[bag] += int(splitted[0]) * int(find_bag(color))
                return bags[bag]
    else:
        return bags[bag]


print(find_bag("shiny gold")-1)
