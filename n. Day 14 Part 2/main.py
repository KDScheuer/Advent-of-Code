grid = tuple(open('input.txt', 'r').read().splitlines())


def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map(''.join, zip(*grid)))
        grid = tuple('#'.join([''.join(sorted(tuple(group), reverse=True)) for group in row.split('#')]) for row in grid)
        grid = tuple(row[::-1] for row in grid)


seen = {grid}
array = [grid]
iterations = 0

while True:
    iterations += 1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)

first = array.index(grid)

grid = array[(1000000000 - first) % (iterations - first) + first]

total = 0
for row_index, row in enumerate(grid):
    total += row.count('O') * (len(grid) - row_index)

print(total)