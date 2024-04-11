floor = 0
pos = 1
first_entry_basement = False
with open('input.txt', 'r') as f:
    for n in f.read():
        if n == '(':
            floor += 1
        elif n == ')':
            floor -= 1
        else:
            print("Unexpected Error in Input File")
            exit(1)

        if first_entry_basement == False and floor == -1:
            first_entry_basement = True
            print(f"Entered Basement at: {pos}")

        pos += 1

print(f"Ended on Floor: {floor}") 