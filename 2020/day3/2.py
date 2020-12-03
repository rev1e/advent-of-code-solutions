#!/usr/bin/env python3

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

with open("input.txt") as f:
    tree_map = [[cell == "#" for cell in line] for line in f]
    map_width = len(tree_map[0]) - 1

answer = 1
for (slope_x, slope_y) in SLOPES:
    pos_x = 0
    pos_y = 0
    trees_count = 0
    while pos_y < len(tree_map) - slope_y:
        pos_x = (pos_x + slope_x) % map_width
        pos_y += slope_y

        # check for tree
        if tree_map[pos_y][pos_x]:
            trees_count += 1

    print(f"Slope ({slope_x}, {slope_y}) encountered trees: {trees_count}")
    answer *= trees_count

print(f"Answer: {answer}")
