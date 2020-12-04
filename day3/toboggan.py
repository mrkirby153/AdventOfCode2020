
area = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '') # Strip the newlines
        row = []
        for char in line:
            if char == '.':
                row.append(False)
            elif char == '#':
                row.append(True)
            else:
                raise Exception(f"Unexpected input {char}")
        area.append(row)

dim_x = len(area[0])
dim_y = len(area)

print(f"Input is {dim_x} by {dim_y}")


def check_path(offset_x, offset_y):
    trees_hit = 0
    pos_x = 0
    pos_y = 0
    for pos_y in range(0, dim_y-1, offset_y):
        # print(f"Moving {offset_x} right and {offset_y} down")
        pos_x = (pos_x + offset_x) % dim_x
        pos_y += offset_y
        # print(f"Now at {pos_x} {pos_y}: ", end="")

        symbol = area[pos_y][pos_x]
        # print(f"{symbol}")
        if symbol:
            trees_hit += 1
    return trees_hit


print(f"Hit {check_path(3, 1)} trees along the way")


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

acc = 1
for slope in slopes:
    x, y = slope
    hit = check_path(x, y)
    print(f"Right {x}, Down {y} will hit {hit} trees")
    acc *= hit
print(f"Result: {acc}")