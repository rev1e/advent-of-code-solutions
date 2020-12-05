#!/usr/bin/env python3

with open("input.txt") as f:
    boarding_passes = [line.strip() for line in f]

id_list = []
for boarding_pass in boarding_passes:
    lower = 0
    upper = 127
    for c in boarding_pass[:7]:
        if lower == upper - 1:
            if c == "F":
                row = lower
            else:
                row = upper
        elif c == "F":
            upper -= round((upper - lower) / 2)
        else:
            lower += round((upper - lower) / 2)

    lower = 0
    upper = 7
    for c in boarding_pass[7:]:
        if lower == upper - 1:
            if c == "L":
                col = lower
            else:
                col = upper
        elif c == "L":
            upper -= round((upper - lower) / 2)
        else:
            lower += round((upper - lower) / 2)

    id_list.append(row * 8 + col)

for i in range(127 * 8 + 7):
    if id_list.count(i) == 0 and id_list.count(i - 1) == 1 and id_list.count(i + 1) == 1:
        print(f"Your seat is {i}")
        break
