def count(config, numbers):
    if config == "":
        return 1 if numbers == () else 0

    if numbers == ():
        return 0 if "#" in config else 1

    result = 0

    if config[0] in '.?':
        result += count(config[1:], numbers)

    if config[0] in '#?':
        if numbers[0] <= len(config) and '.' not in config[:numbers[0]] and (numbers[0] == len(config) or config[numbers[0]] != '#'):
            result += count(config[numbers[0] + 1:], numbers[1:])

    return result


total = 0

for line in open('input.txt', 'r'):
    config, numbers = line.split()
    numbers = tuple(map(int, numbers.split(',')))
    total += count(config, numbers)

print(total)
