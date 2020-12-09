#!/usr/bin/env python3
import itertools

PREAMBLE_LEN = 25

with open("input.txt") as f:
    numbers = [int(l) for l in f]

invalid = 0
for i, num in enumerate(numbers[PREAMBLE_LEN:]):
    valid = False
    for a, b in itertools.product(
            numbers[i:i+PREAMBLE_LEN], numbers[i+1:i+PREAMBLE_LEN]):
        if a + b == num and a != b:
            valid = True
            break
    if not valid:
        print(f"{num} is not valid")
        invalid = num
        break

for a, b in itertools.product(range(len(numbers)), repeat=2):
    if sum(numbers[a:b]) == invalid:
        maximum = max(numbers[a:b])
        minimum = min(numbers[a:b])
        print(f"{minimum} + {maximum} = {minimum + maximum}")
        break
