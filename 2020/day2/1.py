#!/usr/bin/env python3
class Password:
    def __init__(self, to_parse):
        # min-max char: password
        password_array = to_parse.split(" ")
        range_array = password_array[0].split("-")
        self.minimum = int(range_array[0])
        self.maximum = int(range_array[1])
        self.char = password_array[1][0]
        self.password = password_array[2]


    def is_valid(self):
        count = self.password.count(self.char)
        return count >= self.minimum and count <= self.maximum

with open("input.txt") as f:
    passwords = [Password(x) for x in f]

ans = 0
for password in passwords:
    if password.is_valid():
        ans += 1

print(f"There are {ans} valid passwords")
