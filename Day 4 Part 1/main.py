def load_input():
    all_cards = {}
    with open("input.txt", "r") as f:
        for line in f.readlines():
            card_number, all_numbers = line.strip().split(":")
            winning_numbers, your_numbers = all_numbers.strip().split(" | ")
            winning_numbers_list = [int(number) for number in winning_numbers.split(" ") if number]
            your_numbers_list = [int(number) for number in your_numbers.split(" ") if number]
            all_cards[card_number] = {
                'winning_numbers': winning_numbers_list,
                'your_numbers': your_numbers_list,
                'points': 0}
    return all_cards


def get_points_per_card(all_cards):

    for card, attributes in all_cards.items():
        card_matches = 0
        for winning_number in attributes['winning_numbers']:
            if winning_number in attributes['your_numbers']:
                card_matches += 1

        if card_matches != 0:
            points = 1 << card_matches - 1
            attributes['points'] = points


def add_all_points(all_cards):
    total_points = 0
    for card, attributes in all_cards.items():
        total_points += attributes['points']

    return total_points


def main():
    all_cards = load_input()
    get_points_per_card(all_cards)
    answer = add_all_points(all_cards)
    print(answer)


if __name__ == "__main__":
    main()
