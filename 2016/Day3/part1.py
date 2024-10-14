#!/usr/bin/python3

def parse_input(filename):
    contents = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            sides = []
            for side in line.strip().split():
                try:
                    sides.append(int(side))
                except:
                    print(f"ERRORED ON {line.replace(' ', '|').strip().split('|')} with side {side}")
            contents.append(sides)
    return contents


def is_trianlge(sides):
    sides.sort()
    return sides[0] + sides[1] > sides[2]


if __name__ == "__main__":
    filename = "input.txt"
    triangles = parse_input(filename)
    count = 0
    for triangle in triangles:
        if is_trianlge(triangle):
            count += 1
    print(count)
