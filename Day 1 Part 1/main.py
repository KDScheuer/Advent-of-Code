answer = 0
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

with open("calibration values.txt", "r") as f:
    for line in f.readlines():
        first_digit, last_digit = None, None

        for index in range(len(line) - 1):
            if line[index] in digits:
                first_digit = line[index]
                break

        for index in range(len(line) -1, -1, -1):
            if line[index] in digits:
                last_digit = line[index]
                break

        answer += int(first_digit + last_digit)

print(answer)

