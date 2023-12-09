def load_input():
    all_cards = {}
    with open("input.txt", "r") as f:
        for line in f.readlines():
            card_number, all_numbers = line.replace('Card ', '').strip().split(":")
            winning_numbers, your_numbers = all_numbers.strip().split(" | ")
            winning_numbers_list = [int(number) for number in winning_numbers.split(" ") if number]
            your_numbers_list = [int(number) for number in your_numbers.split(" ") if number]
            all_cards[card_number] = {
                'winning_numbers': winning_numbers_list,
                'your_numbers': your_numbers_list,
                'matches': 0,
                'cards_owned': 1,
                'points': 0}
    return all_cards


def get_matches_per_card(all_cards):

    for card, attributes in all_cards.items():
        card_matches = 0
        for winning_number in attributes['winning_numbers']:
            if winning_number in attributes['your_numbers']:
                card_matches += 1
        attributes['matches'] = card_matches


def calculate_cards_owned(all_cards):
    for card, attributes in all_cards.items():
        matches = attributes['matches']
        iterations = attributes['cards_owned']
        for _ in range(iterations):
            for count in range(matches, 0, -1):
                all_cards[str(count + int(card))]['cards_owned'] += 1


def add_all_cards_owned(all_cards):
    total = 0
    for card, attributes in all_cards.items():
        total += attributes['cards_owned']
    return total


def main():
    all_cards = load_input()
    get_matches_per_card(all_cards)
    calculate_cards_owned(all_cards)
    answer = add_all_cards_owned(all_cards)
    print(answer)


if __name__ == "__main__":
    main()
    