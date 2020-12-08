#!/usr/bin/env python3

with open("input.txt") as f:
    lines = [ l.strip() for l in f ]

instructions = [ [x[0], int(x[1])] for x in map(lambda x: x.split(), lines) ]

def check_for_loop():
    accumulator = 0
    ip = 0

    seen = set()

    while (ip not in seen) and (ip != len(instructions)):
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

    if ip in seen:
        return False
    else:
        return accumulator

for i in range(len(instructions)):
    if instructions[i][0] == "jmp":
        instructions[i][0] = "nop"
    elif instructions[i][0] == "nop":
        instructions[i][0] = "jmp"
    else:
        continue

    if not check_for_loop() is False:
        break
    else:
        if instructions[i][0] == "jmp":
            instructions[i][0] = "nop"
        elif instructions[i][0] == "nop":
            instructions[i][0] = "jmp"

ans = check_for_loop()
print(f"Accumulator: {ans}")
