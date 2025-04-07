#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
	print("none")
	sys.exit(1)

if sys.argv[1].count('z') == 0:
	print("none")
else:
	print('z' * sys.argv[1].count('z'))