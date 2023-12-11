def check_possibility(round_res):
    red, green, blue = 0, 0, 0
    drawn = round_res.lstrip(" ").split(", ")

    for pair in drawn:
        number = pair.split(" ")[0]
        color = pair.split(" ")[1]
        if color == "red":
            red = number
        elif color == "green":
            green = number
        elif color == "blue":
            blue = number

    if int(red) > 12 or int(green) > 13 or int(blue) > 14:
        return False
    else:
        return True


sum_of_possible_game_IDs = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        game_possible = True
        game = line.strip().split(':')[0]
        game_results = line.strip().split(':')[1].split(';')
        draws = len(game_results)

        for round_results in game_results:
            round_possible = check_possibility(round_results)
            if not round_possible:
                game_possible = False
                break
        if game_possible:
            sum_of_possible_game_IDs += int(game.split(" ")[1])
            print(int(game.split(" ")[1]))

print(sum_of_possible_game_IDs)
