input = open('input.txt', 'r').read().split(',')


def hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value = (value * 17) % 256
    return value


boxes = [[] for _ in range(256)]
focal_lengths = {}

for instruction in input:
    if '-' in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)

    else:
        label, length = instruction.split('=')
        length = int(length)
        index = hash(label)

        if label not in boxes[index]:
            boxes[index].append(label)

        focal_lengths[label] = length

total = 0
for box_number, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += box_number * lens_slot * focal_lengths[label]

print(total)