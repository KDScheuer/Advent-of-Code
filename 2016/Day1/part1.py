#!/usr/bin/python3

POSTION = [0,0]
FACING = 0 
DIRECTIONS = ["North", "East", "South", "West"]


def Turn(direction):
    global FACING
    if direction == 'L' and FACING >=1:
        FACING -= 1
    elif direction =='L' and FACING == 0:
        FACING = 3
    elif direction == 'R' and FACING <=2:
        FACING += 1
    elif direction == 'R' and FACING == 3:
        FACING = 0
    else:
        print(f'ERROR TURNING TO {direction}\nFACING={FACING}')
        exit(1)


def Walk(steps):
    global FACING, POSTION
    for step in range(0, steps, 1):
        if FACING == 0:
            POSTION[1] += 1
        elif FACING == 1:
            POSTION[0] += 1
        elif FACING == 2:
            POSTION[1] -= 1
        elif FACING == 3:
            POSTION[0] -= 1
        else:
            print(f'ERROR STEPING {step}:{steps} CURRENT POSITION={POSTION}')
        

def Blocks_From_Home():
    global POSTION
    if POSTION[0] < 0:
        POSTION[0] *= -1
    if POSTION[1] < 0:
        POSTION[1] *= -1
    return POSTION[0] + POSTION[1]


def Parse_Input(filename):
    directions = []
    with open(filename, 'r') as f:
        for line in f:
            instructions = line.strip().split(', ')
            directions.extend(instructions)

    return directions


if __name__== "__main__":
    filename = input('Enter Input Filename: ')
    directions = Parse_Input(filename)
    for direction in directions:
        Turn(direction[0])
        Walk(int(direction[1:]))
    print(f'You are {Blocks_From_Home()} Blocks From Home')

