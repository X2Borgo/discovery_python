#!/usr/bin/env python3
import sys
try:
	num1 = int(input("Give me the first number: "))
	num2 = int(input("Give me the second number: "))
except ValueError:
	print("Please enter a valid number.")
	sys.exit(1)
print("Thank you")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {int(num1 / num2)}")
print(f"{num1} * {num2} = {num1 * num2}")