input_strings = []
nice_strings = []


with open('input.txt', 'r') as f:
    for line in f.readlines():
        input_strings.append(line.strip())


def check_appears_twice(line):
    for index, letter in enumerate(line):
        if index + 1 < len(line):
            double = line[index] + line[index + 1]
            if double in line[index + 2:]:
                return True
    return False


def check_repeat_overlap(line):
    for index, letter in enumerate(line):
        if index + 2 < len(line) and letter == line[index + 2]:
            return True
    return False


for line in input_strings:
    meets_appears_twice_req = check_appears_twice(line)
    meets_repeat_overlap = check_repeat_overlap(line)

    if meets_appears_twice_req and meets_repeat_overlap:
        nice_strings.append(line)

print(f'The total number of nice strings is: {len(nice_strings)}')
    