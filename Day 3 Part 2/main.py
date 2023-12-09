def find_numbers_and_symbols():
    with open("input.txt", "r") as f:
        number = ""
        number_id = 1
        number_indexes = []
        line_number = 0
        index_number_dict = {}
        symbol_indexes = []
        for line in f.readlines():
            line = "." + line.strip() + "."
            # Finds any char that is digit and adds to string number
            for index in range(len(line)):
                if line[index].isdigit():
                    number += line[index]
                    number_indexes.append((int(line_number), int(index)))
                # Creates Dict in {(line_number, Index) : number} format
                else:
                    for number_index in number_indexes:
                        index_number_dict[number_index] = {"number": int(number), "num_id": number_id}
                    number = ""
                    number_id += 1
                    number_indexes = []

                    # Creates a List of symbol indexes [(line, index)]
                if line[index] == "*":
                    symbol_indexes.append((int(line_number), int(index)))

            line_number += 1

        return index_number_dict, symbol_indexes


def find_gears(index_number_dict, symbol_indexes):
    indexes_around_symbol = [(-1, 0), (1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1)]

    gears = []
    for symbol_index in symbol_indexes:
        numbers = []
        number_ids = []

        for index_search in indexes_around_symbol:
            index = (symbol_index[0] + index_search[0], symbol_index[1] + index_search[1])
            if index in index_number_dict.keys():
                if index_number_dict[index]["num_id"] not in number_ids:
                    numbers.append(index_number_dict[index]["number"])
                    number_ids.append(index_number_dict[index]["num_id"])

        if len(numbers) == 2:
            total = numbers[0] * numbers[1]
            gears.append(total)

    return gears


def main():
    index_number_dict, symbol_index_list = find_numbers_and_symbols()
    gears = find_gears(index_number_dict, symbol_index_list)
    print(sum(gears))


if __name__ == "__main__":
    main()
