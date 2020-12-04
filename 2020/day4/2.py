#!/usr/bin/env python3
import re

with open("input.txt") as f:
    documents = []
    document = {}
    for line in f:
        if line in ["\n", "\r\n"]:
            documents.append(document)
            document = {}
            continue
        for param_pair in line.split():
            param = param_pair.split(":")
            document[param[0]] = param[1]
    if document:
        documents.append(document)

valid_count = 0
for document in documents:
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)
    if not (
        "byr" in document and "iyr" in document and
        "eyr" in document and "hgt" in document and
        "hcl" in document and "ecl" in document and
        "pid" in document
        ):
        continue

    byr = document["byr"]
    if not (
        re.fullmatch(r"\d{4}", byr) and
        int(byr) >= 1920 and int(byr) <= 2002
    ):
        continue

    iyr = document["iyr"]
    if not (
        re.fullmatch(r"\d{4}", iyr) and
        int(iyr) >= 2010 and int(iyr) <= 2020
    ):
        continue

    eyr = document["eyr"]
    if not (
        re.fullmatch(r"\d{4}", eyr) and
        int(eyr) >= 2020 and int(eyr) <= 2030
    ):
        continue

    hgt = document["hgt"]
    if re.fullmatch(r"\d+(cm|in)", hgt):
        hgt_int = int(hgt[:-2])
        if not (
            (hgt[-2:] == "cm" and hgt_int >= 150 and hgt_int <= 193) or
            (hgt[-2:] == "in" and hgt_int >= 59 and hgt_int <= 76)
        ):
            continue
    else:
        continue

    hcl = document["hcl"]
    if not re.fullmatch(r"#[\da-f]{6}", hcl):
        continue

    ecl = document["ecl"]
    if not ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    pid = document["pid"]
    if not re.fullmatch("\d{9}", pid):
        continue

    valid_count += 1

print(f"Valid documents: {valid_count}")
