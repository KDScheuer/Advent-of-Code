galaxy = open('input.txt', 'r').read().strip().splitlines()

MULTIPLIER = 1000000

empty_rows = []
columns_seen = []
empty_columns = []
galaxies = []

for row_index, row in enumerate(galaxy):

    if '#' not in row:
        empty_rows.append(row_index)

    for column_index, char in enumerate(row):

        if char == '.' and column_index not in empty_columns and column_index not in columns_seen:
            empty_columns.append(column_index)
        elif char == '#':
            galaxies.append((row_index, column_index))
            if column_index in empty_columns:
                empty_columns.remove(column_index)

        columns_seen.append(column_index)

new_galaxy_locations = []
for row_index, column_index in galaxies:
    crossed_columns = 0
    crossed_rows = 0

    for n in range(0, column_index, 1):
        if n in empty_columns:
            crossed_columns += 1

    for n in range(0, row_index, 1):
        if n in empty_rows:
            crossed_rows += 1

    if crossed_columns >= 1:
        new_col_index = (column_index - crossed_columns) + (crossed_columns * MULTIPLIER)
    else:
        new_col_index = column_index

    if crossed_rows >= 1:
        new_row_index = (row_index - crossed_rows) + (crossed_rows * MULTIPLIER)
    else:
        new_row_index = row_index

    new_galaxy_locations.append((new_row_index, new_col_index))

total_distances = []
galaxies_seen = []
for start_row, start_column in new_galaxy_locations:
    galaxies_seen.append((start_row, start_column))

    for end_row, end_column in new_galaxy_locations:
        if (end_row, end_column) in galaxies_seen:
            continue

        total_r_dist = abs(start_row - end_row)
        total_c_dist = abs(start_column - end_column)

        total = total_r_dist + total_c_dist

        total_distances.append(total)

print(sum(total_distances))
