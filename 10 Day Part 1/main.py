from collections import deque


grid = open('input.txt', 'r').read().strip().splitlines()

start_row, start_column = 0, 0
for row_index, row in enumerate(grid):
    for column_index, char in enumerate(row):
        if char == 'S':
            start_row = row_index
            start_column = column_index
            break
    else:
        continue
    break

seen = {(start_row, start_column)}
q = deque([(start_row, start_column)])

while q:
    row, column = q.popleft()
    char = grid[row][column]

    if row > 0 and char in "S|JL" and grid[row - 1][column] in "|7F" and (row - 1, column) not in seen:
        seen.add((row - 1, column))
        q.append((row - 1, column))

    if row < len(grid) - 1 and char in "S|7F" and grid[row + 1][column] in "|JL" and (row + 1, column) not in seen:
        seen.add((row + 1, column))
        q.append((row + 1, column))

    if column > 0 and char in "S-J7" and grid[row][column - 1] in "-LF" and (row, column - 1) not in seen:
        seen.add((row, column - 1))
        q.append((row, column - 1))

    if column < len(grid[row]) - 1 and char in "S-LF" and grid[row][column + 1] in "-J7" and (row, column + 1) not in seen:
        seen.add((row, column + 1))
        q.append((row, column + 1))

print(len(seen) // 2)

