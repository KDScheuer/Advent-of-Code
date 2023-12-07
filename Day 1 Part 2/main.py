ANSWER = 0
NUMBERS = {"zero": "0",
           "one": "1",
           "two": "2",
           "three": "3",
           "four": "4",
           "five": "5",
           "six": "6",
           "seven": "7",
           "eight": "8",
           "nine": "9"}


def find_digit(line, for_start, for_end, for_iter):
    for index in range(for_start, for_end, for_iter):
        if line[index] in NUMBERS.values():
            return line[index]
        else:
            for number in NUMBERS.keys():
                end_index = index + len(number)
                if line[index:end_index] in NUMBERS.keys():
                    return NUMBERS[line[index:end_index]]


with open("calibration values.txt", "r") as f:
    for line in f.readlines():
        first_digit = find_digit(line=line, for_start=0, for_end=len(line) - 1, for_iter=1)
        last_digit = find_digit(line=line, for_start=len(line) - 1, for_end=-1, for_iter=-1)
        ANSWER += int(first_digit + last_digit)

    print(ANSWER)
