#!/usr/bin/env python3

with open("input.txt") as f:
    boarding_passes = [line.strip() for line in f]

max_id = 0
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

    seat_id = row * 8 + col
    if seat_id > max_id:
        max_id = seat_id

print(f"Maximum id is: {max_id}")
