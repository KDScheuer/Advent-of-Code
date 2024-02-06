race_time_distance = []
with open('input.txt') as f:
    for line in f.readlines():
        numbers = ""
        numbers += line.split(':')[1].replace(" ", "").strip()
        race_time_distance.append(int(numbers))

slowest_speed_and_still_win = 0
fastest_speed_and_still_win = 0

speed = 1
while slowest_speed_and_still_win == 0:
    time_remaining = race_time_distance[0] - speed
    distance = speed * time_remaining
    if distance > race_time_distance[1]:
        slowest_speed_and_still_win = speed
        fastest_speed_and_still_win = time_remaining
    speed += 1

print(fastest_speed_and_still_win - slowest_speed_and_still_win + 1)
