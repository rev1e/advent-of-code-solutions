#!/usr/bin/env python3
import functools
with open("input.txt") as f:
	adapters = [ int(l) for l in f ]

adapters.sort()

@functools.lru_cache
def check(i=-1, prev=0):
	if i == len(adapters) - 1:
		return 1
	
	count = 0
	for j in range(1, 4):
		if i + j >= len(adapters):
			break
		if adapters[i + j] <= prev + 3:
			count += check(i + j, adapters[i + j])
		else:
			break
	return count

print(check())