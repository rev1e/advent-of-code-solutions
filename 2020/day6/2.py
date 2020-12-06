#!/usr/bin/env python3

with open("input.txt") as f:
    answers = []
    group_count = 0
    group_answer_map = {}

    for line in f:
        if line in ["\n", "\r\n"]:
            answers.append([ k for k, v in group_answer_map.items() if v == group_count ])
            group_answer_map = {}
            group_count = 0
            continue

        group_count += 1

        for answer in line.strip():
            if answer in group_answer_map:
                group_answer_map[answer] += 1
            else:
                group_answer_map[answer] = 1

    if group_answer_map:
        answers.append([ k for k, v in group_answer_map.items() if v == group_count ])

answers_sum = 0
for group_answer in answers:
    answers_sum += len(group_answer)

print(f"Sum of all answers is: {answers_sum}")
