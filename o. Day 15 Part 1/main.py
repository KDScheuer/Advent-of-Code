input = open('input.txt', 'r').read().split(',')

total = 0
for string in input:
    value = 0
    for char in string:
        value += ord(char)
        value = (value * 17) % 256
    total += value

print(total)
