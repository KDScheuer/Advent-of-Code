#!/usr/bin/python3

def parse_input(filename):
    sides1 = []
    sides2 = []
    sides3 = []
    contents = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            counter = 0
            for side in line.strip().split():
                if counter == 0:
                    sides1.append(int(side))
                if counter == 1:
                    sides2.append(int(side))
                if counter == 2:
                    sides3.append(int(side))
                
                counter += 1
                
                if len(sides3) == 3: 
                    contents.append(sides1)
                    contents.append(sides2)
                    contents.append(sides3)
                    sides1 = []
                    sides2 = []
                    sides3 = []
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
