grid = open('input.txt', 'r').read().splitlines()
grid = list(map(''.join, zip(*grid)))
grid = ['#'.join([''.join(sorted(list(group), reverse=True)) for group in row.split('#')]) for row in grid]
grid = list(map(''.join, zip(*grid)))

total = 0
for row_index, row in enumerate(grid):
    total += row.count('O') * (len(grid) - row_index)

print(total)