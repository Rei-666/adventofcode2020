with open("./input.txt") as file:
    text = file.readlines()

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passport = ""
number_of_valid_passports = 0
for lines in text:
    passport += lines
    if lines == '\n':
        if all(x in passport for x in fields):
            number_of_valid_passports += 1
        passport = ''
print(number_of_valid_passports)


