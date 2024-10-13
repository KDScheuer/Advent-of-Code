#!/usr/bin/python3

KEYPAD = {
    (0, 0): 'oob',
    (1, 0): 'oob',
    (2, 0): '1',
    (3, 0): 'oob',
    (4, 0): 'oob',
    (0, 1): 'oob',
    (1, 1): '2',
    (2, 1): '3',
    (3, 1): '4',
    (4, 1): 'oob',
    (0, 2): '5',
    (1, 2): '6',
    (2, 2): '7',
    (3, 2): '8',
    (4, 2): '9',
    (0, 3): 'oob',
    (1, 3): 'A',
    (2, 3): 'B',
    (3, 3): 'C',
    (4, 3): 'oob',
    (0, 4): 'oob',
    (1, 4): 'oob',
    (2, 4): 'D',
    (3, 4): 'oob',
    (4, 4): 'oob'
}

def parse_input(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            temp = []
            for char in line.strip():
                temp.append(char)
            instructions.append(temp)
    return instructions

def get_number(postion, instructions):
    for instruction in instructions:
        desired_pos = (0,0)
        if instruction == 'R' and postion[0] < 4:
            desired_pos = (postion[0] + 1, postion[1])
        elif instruction == 'L' and postion[0] > 0:
            desired_pos = (postion[0] - 1, postion[1])
        elif instruction == 'U' and  postion[1] > 0:
            desired_pos = (postion[0], postion[1] - 1)
        elif instruction == 'D' and  postion[1] < 4:
            desired_pos = (postion[0], postion[1] + 1)
        if KEYPAD[desired_pos] != 'oob':
            postion = desired_pos

    return postion



if __name__ == "__main__":
    file = "input.txt"
    code = ""
    postion = (0, 2)
    instructions = parse_input(file)
    for instruction in instructions:
         postion = get_number(postion, instruction)
         code += KEYPAD[postion]
    print(code)
