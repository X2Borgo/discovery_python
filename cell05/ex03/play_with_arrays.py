#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = []
for n in set(arr):
	if n > 5:
		arr2.append(n + 2)
print(arr)
print(arr2)