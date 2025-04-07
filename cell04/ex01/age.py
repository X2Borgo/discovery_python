#!/usr/bin/env python3
import sys
try:
	n = int(input("Please tell me your age: "))
except ValueError:
	print("Please enter a valid number.")
	sys.exit(1)
print(f"You are currently {n} years old.")
print(f"In 10 years, you'll be {n + 10} years old.")
print(f"In 20 years, you'll be {n + 20} years old.")
print(f"In 30 years, you'll be {n + 30} years old.")