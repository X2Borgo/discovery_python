#!/usr/bin/env python3
import sys
if len(sys.argv) != 1:
	print("none")
	sys.exit(1)

n = 0
while n <= 10:
	i = 0
	table = f"Table de {n}: "
	while (i <= 10):
		table += str(n * i)
		if i != 10:
			table += " "
		i += 1
	print(table)
	n += 1