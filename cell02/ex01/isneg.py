#!/usr/bin/env python3
try:
	n = int(input())
	if n > 0:
		print("This number is positive.")
	elif n < 0:
		print("This number is negative.")
	else:
		print("This number is both positive and negative.")
except ValueError:
	print("Please enter a valid integer")