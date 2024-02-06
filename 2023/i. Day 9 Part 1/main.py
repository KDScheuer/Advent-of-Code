original_inputs = {}
line_number = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        original_inputs[line_number] = {0: [int(number) for number in line.strip().split(" ")]}
        line_number += 1


for line_number, value in original_inputs.items():
    step = 0
    while value[step].count(0) != len(value[step]):
        num_1, num_2 = 0, 1
        temp_list = []

        for _ in range(len(value[step]) - 1):
            temp_list.append(value[step][num_2] - value[step][num_1])
            num_1 += 1
            num_2 += 1

        step += 1
        value[step] = temp_list

answer = 0
for line_num, steps in original_inputs.items():
    step = len(steps) - 1
    last_index = len(steps[step]) - 1
    num_1 = steps[step][last_index]
    last_index = len(steps[step]) - 1
    num_2 = steps[step - 1][last_index + 1]
    step_answer = num_1 + num_2
    step -= 1

    while step != 0:
        last_index = len(steps[step]) - 1
        num_2 = steps[step - 1][last_index + 1]
        step_answer += num_2
        step -= 1
    answer += step_answer

print(answer)
