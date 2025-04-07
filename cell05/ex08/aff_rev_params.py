#!/usr/bin/env python3
import sys
i = len(sys.argv) - 1
if i <= 1:
	print("none")
	sys.exit(0)
while i >= 1:
	print(sys.argv[i])
	i -= 1