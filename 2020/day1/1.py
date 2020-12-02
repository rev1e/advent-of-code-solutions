#!/usr/bin/env python3

with open("input.txt") as f:
    numbers = [int(x) for x in f]

def main():
    for i, a in enumerate(numbers[:-1]):
        for b in numbers[i+1:]:
            if a + b == 2020:
                print(f"{a} * {b} = {a*b}")
                return
    print("Invalid input")

if __name__ == "__main__":
    main()
