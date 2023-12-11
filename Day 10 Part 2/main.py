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

maybe_s = {"|", "-", "J", "L", "7", "F"}

while q:
    row, column = q.popleft()
    char = grid[row][column]

    if row > 0 and char in "S|JL" and grid[row - 1][column] in "|7F" and (row - 1, column) not in seen:
        seen.add((row - 1, column))
        q.append((row - 1, column))
        if char == "S":
            maybe_s &= {"|", "J", "L"}

    if row < len(grid) - 1 and char in "S|7F" and grid[row + 1][column] in "|JL" and (row + 1, column) not in seen:
        seen.add((row + 1, column))
        q.append((row + 1, column))
        if char == "S":
            maybe_s &= {"|", "7", "F"}

    if column > 0 and char in "S-J7" and grid[row][column - 1] in "-LF" and (row, column - 1) not in seen:
        seen.add((row, column - 1))
        q.append((row, column - 1))
        if char == "S":
            maybe_s &= {"-", "J", "7"}

    if column < len(grid[row]) - 1 and char in "S-LF" and grid[row][column + 1] in "-J7" and (row, column + 1) not in seen:
        seen.add((row, column + 1))
        q.append((row, column + 1))
        if char == "S":
            maybe_s &= {"-", "L", "F"}

assert len(maybe_s) == 1

(S,) = maybe_s
grid = [row.replace("S", S) for row in grid]
grid = ["".join(char if (row_index, column_index) in seen else "." for column_index, char in enumerate(row)) for row_index, row in enumerate(grid)]

outside = set()

for row_index, row in enumerate(grid):
    within = False
    up = None

    for column_index, char in enumerate(row):
        if char == "|":
            assert up is None
            within = not within
        elif char == "-":
            assert up is not None
        elif char in "LF":
            assert up is None
            up = char == "L"
        elif char in "7J":
            assert up is not None
            if char != ("J" if up else "7"):
                within = not within
            up = None
        elif char == ".":
            pass

        if not within:
            outside.add((row_index, column_index))

print(len(grid) * len(grid[0]) - len(outside | seen))


