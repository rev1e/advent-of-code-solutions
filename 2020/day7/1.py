#!/usr/bin/env python3

# { color_name: [bags that it can contain] }
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
            bags[color_name].append(" ".join(l[color_index:color_index+2]))

ans = 0
def check(current_bag):
    if current_bag == "shiny gold":
        global ans
        ans += 1
        return True

    for bag in bags[current_bag]:
        if check(bag):
            return True

del bags["shiny gold"]

for bag in bags:
    check(bag)

print(f"{ans} bags can hold shiny gold bag")
