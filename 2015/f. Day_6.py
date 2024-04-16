light_grid = {}

for x_cord in range(0, 1000):
    for y_cord in range(0, 1000):
        light_grid[(x_cord, y_cord)] = 0


def turn_on(start, stop):
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            light_grid[(x, y)] += 1


def turn_off(start, stop):
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            if light_grid[(x, y)] > 0:
                light_grid[(x, y)] -= 1


def toggle(start, stop):
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            light_grid[(x, y)] += 2
            


with open('input.txt', 'r') as f:
    for line in f.readlines():
        temp = line.split()[-3].split(',')
        start = (int(temp[0]), int(temp[1]))

        temp = line.split()[-1].split(',')
        end = (int(temp[0]), int(temp[1]))
        if line.split()[0] == 'turn':
            if line.split()[1] == 'on':
                turn_on(start, end)
            elif line.split()[1] == 'off':
                turn_off(start, end)
        else:
            toggle(start, end)

total = 0
for key, value in light_grid.items():
    total += value

print(f'Total brightness of the lights is: {total}')
