#!/usr/bin/env python3

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
    if (
        "byr" in document and "iyr" in document and
        "eyr" in document and "hgt" in document and
        "hcl" in document and "ecl" in document and
        "pid" in document
        ):
        valid_count += 1;

print(f"Valid documents: {valid_count}")
