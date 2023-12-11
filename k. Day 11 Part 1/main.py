galaxy = open('input.txt', 'r').read().strip().splitlines()

empty_rows = []
columns_seen = []
empty_columns = []

for row_index, row in enumerate(galaxy):

    if '#' not in row:
        empty_rows.append(row_index)

    for column_index, char in enumerate(row):

        if char == '.' and column_index not in empty_columns and column_index not in columns_seen:
            empty_columns.append(column_index)
        elif char == '#' and column_index in empty_columns:
            empty_columns.remove(column_index)

        columns_seen.append(column_index)

adjust = 0
for index in empty_columns:

    for row_index, row in enumerate(galaxy):

        galaxy[row_index] = galaxy[row_index][:index + adjust] + '.' + galaxy[row_index][index + adjust:]

    adjust += 1

empty_string_list = galaxy[empty_rows[0]]
adjust = 0
for row_index, row in enumerate(galaxy):
    for empty_row in empty_rows:
        if row_index == empty_row:
            galaxy.insert(row_index + adjust, empty_string_list)
            adjust += 1

galaxies = []
for row_index, row in enumerate(galaxy):
    for column_index, char in enumerate(row):
        if char == '#':
            galaxies.append((row_index, column_index))

total_distances = []
galaxies_seen = []
for start_row, start_column in galaxies:
    galaxies_seen.append((start_row, start_column))

    for end_row, end_column in galaxies:
        if (end_row, end_column) in galaxies_seen:
            continue

        total_r_dist = abs(start_row - end_row)
        total_c_dist = abs(start_column - end_column)

        total = total_r_dist + total_c_dist

        total_distances.append(total)

print(sum(total_distances))

