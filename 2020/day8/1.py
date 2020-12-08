#!/usr/bin/env python3

with open("input.txt") as f:
    lines = [ l.strip() for l in f ]

instructions = [ (x[0], int(x[1])) for x in map(lambda x: x.split(), lines) ]

accumulator = 0
ip = 0

seen = set()

while not ip in seen:
    seen.add(ip)

    instruction = instructions[ip]

    if instruction[0] == "acc":
        accumulator += instruction[1]
    elif instruction[0] == "nop":
        pass
    elif instruction[0] == "jmp":
        ip += instruction[1]
        continue

    ip += 1

print(f"Accumulator: {accumulator}")
