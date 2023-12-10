temp_instructions = []
elements = {}

start_position = "AAA"
end_position = "ZZZ"
file_input = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        if line != "\n":
            file_input.append(line.strip())

    temp_instructions = file_input.pop(0)

    for element in file_input:
        instruction_set, temp = element.replace('(', '').replace(')', '').split(' = ')
        left_instruction, right_instruction = temp.split(', ')
        elements[instruction_set] = [left_instruction, right_instruction]

instructions = []
for instruction in temp_instructions:
    if instruction == 'R':
        instructions.append(1)
    elif instruction == 'L':
        instructions.append(0)

count = 0
current_position = start_position
while current_position != end_position:
    for direction in instructions:
        next_position = elements[current_position][direction]
        current_position = next_position
        count += 1

print(count)
