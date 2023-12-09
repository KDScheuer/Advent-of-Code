time_distance = []
with open('input.txt') as f:
    for line in f.readlines():
        numbers = [int(number) for number in line.strip().split(' ') if number.isdigit()]
        time_distance.append(numbers)

total_ways_to_win = 1
for index in range(len(time_distance[0])):
    race_time = time_distance[0][index]
    record = time_distance[1][index]
    ways_to_win = 0
    for speed in range(1, race_time + 1, 1):
        time = race_time - speed
        if time * speed > record:
            ways_to_win += 1
    total_ways_to_win *= ways_to_win

print(total_ways_to_win)