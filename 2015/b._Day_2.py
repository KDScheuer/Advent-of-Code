input = []
with open('input.txt', 'r') as f:
        input = [line.strip().split('x') for line in f.readlines()]

total_paper = 0
total_ribbon = 0

for box in input:
        side_1_area = int(box[0]) * int(box[1])
        side_2_area = int(box[1]) * int(box[2]) 
        side_3_area = int(box[2]) * int(box[0])

        if side_1_area <= side_2_area and side_1_area <= side_3_area:
                extra = side_1_area
        elif side_2_area <= side_1_area and side_2_area <= side_3_area:
                extra = side_2_area
        elif side_3_area <= side_1_area and side_3_area <= side_2_area:
                extra = side_3_area

        paper_required = 2 * side_1_area + 2 * side_2_area + 2 * side_3_area + extra
        total_paper += paper_required

        side_1_perimeter = 2 * int(box[0]) + 2 * int(box[1])
        side_2_perimeter = 2 * int(box[1]) + 2 * int(box[2]) 
        side_3_perimeter = 2 * int(box[2]) + 2 * int(box[0])

        if side_1_perimeter <= side_2_perimeter and side_1_perimeter <= side_3_perimeter:
                ribbon = side_1_perimeter
        elif side_2_perimeter <= side_1_perimeter and side_2_perimeter <= side_3_perimeter:
                ribbon = side_2_perimeter
        elif side_3_perimeter <= side_1_perimeter and side_3_perimeter <= side_2_perimeter:
                ribbon = side_3_perimeter

        extra_ribbon = int(box[0]) * int(box[1]) * int(box[2])
        total_ribbon += ribbon + extra_ribbon

print(f"The total amount of wrapping paper is: {total_paper}")
print(f"The total amount of ribbon is: {total_ribbon}")