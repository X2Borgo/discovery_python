#!/usr/bin/env python3
import sys
try:
	print("Enter a number less than 25")
	n = int(input())
	if n > 25:
		print("Error")
		sys.exit(1)
	while n <= 25:
		print(f"Inside the loop, my variable is {n}")
		n += 1
except ValueError:
	print("Please enter a valid number")