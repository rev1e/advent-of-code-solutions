#!/usr/bin/env python3

with open("input.txt") as f:
    numbers = [int(x) for x in f]

def main():
    for i, a in enumerate(numbers[:-2]):
        for b in numbers[i+1:]:
            for c in numbers[i+2:]:
                if a + b + c == 2020:
                    print(f"{a} * {b} * {c} = {a*b*c}")
                    return
    print("Invalid input")

if __name__ == "__main__":
    main()
