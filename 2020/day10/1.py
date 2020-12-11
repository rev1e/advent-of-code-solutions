#!/usr/bin/env python3

with open("input.txt") as f:
    adapters = [ int(l) for l in f ]

adapters.sort()

one_count = 0
three_count = 0

one_count += adapters[0]

for i, adapter in enumerate(adapters[:-1]):
    diff = adapters[i + 1] - adapter
    if diff == 1:
        one_count += 1
    elif diff == 3:
        three_count += 1

three_count += 1

print(f"{one_count} * {three_count} = {one_count * three_count}")