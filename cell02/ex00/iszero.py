#!/usr/bin/env python3
try:
	n = int(input())
	if n == 0:
		print("This number is equal to zero.")
	else:
		print("This number is different from zero.")
except ValueError:
	print("Please enter a valid integer.")