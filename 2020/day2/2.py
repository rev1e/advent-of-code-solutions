#!/usr/bin/env python3
class Password:
    def __init__(self, to_parse):
        # min-max char: password
        password_array = to_parse.split(" ")
        range_array = password_array[0].split("-")
        self.first = int(range_array[0])
        self.second = int(range_array[1])
        self.char = password_array[1][0]
        self.password = password_array[2]


    def is_valid(self):
        valid = False

        if self.password[self.first - 1] == self.char:
            if self.password[self.second - 1] != self.char:
                valid = True
        elif self.password[self.second - 1] == self.char:
            valid = True

        return valid

with open("input.txt") as f:
    passwords = [Password(x) for x in f]

ans = 0
for password in passwords:
    if password.is_valid():
        ans += 1

print(f"There are {ans} valid passwords")
