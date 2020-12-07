#!/usr/bin/env python3

# { color_name: [{ count, color }] }
bags = {}
with open("input.txt") as f:
    lines = [[ word for word in l.strip().split() ] for l in f]

    for l in lines:
        color_name = " ".join(l[0:2])
        bags[color_name] = []

        if l[4] == "no":
            continue

        for i in range((len(l) - 4) // 4):
            color_index = i * 4 + 5
            bag_color = " ".join(l[color_index:color_index+2])
            bag_count = l[color_index-1]
            bags[color_name].append({ "count": int(bag_count), "color": bag_color })

def check(current_bag):
    count = 0
    for bag in bags[current_bag]:
        count += bag["count"]
        count += check(bag["color"]) * bag["count"]
    return count

ans = check("shiny gold")

print(f"Shiny gold bag holds {ans} bags")
