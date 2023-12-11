def get_symbol_indexes(schematic):
    """Generates a dict of symbol indexes as {line_number: index}"""
    symbols = ['*', '=', '-', '%', '&', '@', '$', '/', '+', '#']

    symbol_indexes = {}

    for line, text in schematic.items():
        indexes = []
        for index in range(len(text)):
            if text[index] in symbols:
                indexes.append(index)
        if len(indexes) > 0:
            symbol_indexes[int(line)] = indexes

    return symbol_indexes


def generate_number_and_index_dict(schematic):
    """This loop creates a dict in {number: {line_number: [char1_index, char2_index, etc.]}} format"""
    number_indexes = {}
    for line, text in schematic.items():
        number = ""
        indexes = []
        line_indexes = {}
        for index in range(len(text)):
            if text[index].isdigit():
                number += text[index]
                indexes.append(str(index))
            elif number.endswith("|"):
                continue
            else:
                if number != "":
                    line_indexes[line] = indexes
                    number_indexes[int(number)] = line_indexes
                    number = ""
                    line_indexes = {}
                    indexes = []
    return number_indexes


def find_valid_numbers(number_indexes_dict, symbol_indexes):
    total = 0
    for number, value in number_indexes_dict.items():
        for sym_line, sym_indexes in symbol_indexes.items():
            # Check on same line left
            if sym_line in value.keys():
                for sym_index in sym_indexes:
                    if str(sym_index - 1) in value[sym_line]:
                        total += number
                        break
            # Check on same line right
            if sym_line in value.keys():
                for sym_index in sym_indexes:
                    if str(sym_index + 1) in value[sym_line]:
                        total += number
                        print(number)
                        break

            # Check line above
            if sym_line != 0 and sym_line - 1 in value.keys():
                for sym_index in sym_indexes:
                    if (str(sym_index) in value[sym_line - 1] or str(sym_indexes[0] - 1) in value[sym_line - 1]
                            or str(sym_indexes[len(sym_indexes) - 1] + 1) in value[sym_line - 1]):
                        total += number
                        print(number)
                        break

            # Check line below
            if sym_line != len(number_indexes_dict) - 1 and sym_line + 1 in value.keys():
                for sym_index in sym_indexes:
                    if (str(sym_index) in value[sym_line + 1] or str(sym_indexes[0] - 1) in value[sym_line + 1]
                            or str(sym_indexes[len(sym_indexes) - 1] + 1) in value[sym_line + 1]):
                        total += number
                        print(number)
                        break

    return total


def main():
    schematic = {}
    line_numbers = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            schematic[line_numbers] = line.strip()
            line_numbers += 1

    number_index_dict = generate_number_and_index_dict(schematic)
    symbol_indexes = get_symbol_indexes(schematic)
    answer = find_valid_numbers(number_index_dict, symbol_indexes)
    print(answer)


if __name__ == "__main__":
    main()
