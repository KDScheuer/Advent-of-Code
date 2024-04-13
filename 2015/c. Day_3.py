instructions = []
with open('input.txt', 'r') as f:
    instructions = [direction for direction in f.read()]


def get_position(x_pos, y_pos, direction):
    if direction == "v":
            y_pos -= 1
    elif direction == "<":
            x_pos -= 1
    elif direction == "^":
            y_pos += 1
    elif direction == ">":
            x_pos += 1
    else:
        print(f"Error occoured unexcpected value: {direction}")
        exit(1)

    return (x_pos, y_pos)


santa_pos = (0, 0)
robot_pos = (0, 0)
houses_visted = set()
houses_visted.add((0, 0))

for index, direction in enumerate(instructions):
    if index % 2 == 0:
        santa_pos = get_position(santa_pos[0], santa_pos[1], direction)
        houses_visted.add(santa_pos)

    else:
        robot_pos = get_position(robot_pos[0], robot_pos[1], direction)
        houses_visted.add(robot_pos)

print(f"Total houses that recieve at least one present: {len(houses_visted)}")