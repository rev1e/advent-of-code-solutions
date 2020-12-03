#!/usr/bin/env python3

with open("input.txt") as f:
    tree_map = [[cell == "#" for cell in line] for line in f]
    map_width = len(tree_map[0]) - 1

pos_x = 0
pos_y = 0
trees_count = 0
while pos_y < len(tree_map) - 1:
    pos_x = (pos_x + 3) % map_width
    pos_y += 1

    # check for tree
    if tree_map[pos_y][pos_x]:
        trees_count += 1

print(f"Encountered trees: {trees_count}")
