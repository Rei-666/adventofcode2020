import re

with open("./input.txt") as file:
    text = file.readlines()

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def check_if_in_range(passport, field, least, most):
    occurrence = passport.find(field)
    end = passport.find(" ", occurrence)
    number = int(passport[occurrence+4:end])
    if number in range(least, most+1):
        return True
    return False


def check_hgt(passport):
    occurrence = passport.find("hgt")
    end = passport.find(" ", occurrence)
    number = passport[occurrence+4:end]
    unit = number[-2:]
    try:
        height = int(number[:-2])
    except ValueError:
        return False
    if unit == "in":
        return True if height in range(59, 76+1) else False
    if unit == "cm":
        return True if height in range(150, 193+1) else False
    return False


def check_hcl(passport):
    occurrence = passport.find("hcl")
    number = passport[occurrence+4:occurrence+11]
    if re.match('#[a-f0-9]{6}', number):
        return True
    return False


def check_ecl(passport):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    occurrence = passport.find("ecl")
    end = passport.find(" ", occurrence+4)
    color = passport[occurrence+4:end]
    if any(color == x for x in colors):
        return True
    return False


def check_pid(passport):
    occurrence = passport.find("pid")
    end = passport.find(" ", occurrence)
    number = passport[occurrence+4:end+1]
    if re.match('[0-9]{9} ', number):
        return True
    return False


def check_passport(passport):
    if (
            check_if_in_range(passport, "byr", 1920, 2002)
            and check_if_in_range(passport, "iyr", 2010, 2020)
            and check_if_in_range(passport, "eyr", 2020, 2030)
            and check_hgt(passport)
            and check_hcl(passport)
            and check_ecl(passport)
            and check_pid(passport)
    ):
        return True
    return False


pp = ""
number_of_valid_passports = 0
for lines in text:
    pp += lines
    if lines == '\n':
        if all(x in pp for x in fields):
            if check_passport(pp):
                number_of_valid_passports += 1
        pp = ''
    pp = pp.replace('\n', ' ')
print(number_of_valid_passports)