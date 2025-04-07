#!/usr/bin/env python3
try:
	print("Enter a number")
	n = int(input())
	i = 0
	while i < 10:
		print(f"{i} x {n} = {n * i}")
		i += 1
except ValueError:
	print("Please enter a valid number")