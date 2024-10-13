#!/usr/bin/python3

KEYPAD = {
    (0, 0): '1',
    (1, 0): '2',
    (2, 0): '3',
    (0, 1): '4',
    (1, 1): '5',
    (2, 1): '6',
    (0, 2): '7',
    (1, 2): '8',
    (2, 2): '9'
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
        if instruction == 'R' and postion[0] < 2:
            postion = (postion[0] + 1, postion[1])
        elif instruction == 'L' and postion[0] > 0:
            postion = (postion[0] - 1, postion[1])
        elif instruction == 'U' and  postion[1] > 0:
            postion = (postion[0], postion[1] - 1)
        elif instruction == 'D' and  postion[1] < 2:
            postion = (postion[0], postion[1] + 1)
    
    return postion



if __name__ == "__main__":
    file = "input.txt"
    code = ""
    postion = (1,1)
    instructions = parse_input(file)
    for instruction in instructions:
         postion = get_number(postion, instruction)
         code += KEYPAD[postion]
    print(code)
