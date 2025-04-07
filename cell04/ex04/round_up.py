#!/usr/bin/env python3
import sys
try:
	num = float(input("Give me a number: "))
except ValueError:
	print("Please enter a valid number.")
	sys.exit(1)
if num == int(num):
	print(int(num))
else:
	print(int(num) + 1)