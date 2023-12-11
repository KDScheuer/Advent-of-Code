answer = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        game_id = line.split(':')[0].replace("Game", "").lstrip().strip()
        game_draws = line.split(': ')[1].replace(";", ",").replace(", ", ",").strip().split(',')

        min_red, min_green, min_blue = 0, 0, 0
        for draw in range(len(game_draws)):
            number = int(game_draws[draw].split(" ")[0])
            color = game_draws[draw].split(" ")[1]
            if color == "red" and number > min_red:
                min_red = number
            elif color == "green" and number > min_green:
                min_green = number
            elif color == "blue" and number > min_blue:
                min_blue = number

        answer += min_red * min_green * min_blue

print(answer)
