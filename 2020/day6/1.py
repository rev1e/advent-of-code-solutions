#!/usr/bin/env python3

with open("input.txt") as f:
    answers = []
    group_answer = []

    for line in f:
        if line in ["\n", "\r\n"]:
            answers.append(group_answer)
            group_answer = []
            continue
        for answer in line.strip():
            if group_answer.count(answer) == 0:
                group_answer.append(answer)

    if group_answer:
        answers.append(group_answer)

answers_sum = 0
for group_answer in answers:
    answers_sum += len(group_answer)

print(f"Sum of all answers is: {answers_sum}")
