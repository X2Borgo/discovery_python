#!/usr/bin/env python3
import sys
try:
	print("Enter the first number:")
	num1 = int(input())
	print("Enter the second number:")
	num2 = int(input())
except ValueError:
	print("Please enter a valid number.")
	sys.exit(1)
res = num1 * num2
print(f"{num1} x {num2} = {res}")
if res > 0:
	print("The result is positive.")
elif res < 0:
	print("The result is negative.")
else:
	print("The result is positive and negative.")