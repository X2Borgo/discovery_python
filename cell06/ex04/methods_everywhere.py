#!/usr/bin/env python3
import sys
def shrink(text):
	print(text[slice(0, 8)])

def enlarge(text):
	print(text + 'z' * (8 - len(text)))

if len(sys.argv) == 1:
	print("none")
	sys.exit(1)

for s in sys.argv[1:]:
	if len (s) > 8:
		shrink(s)
	elif len(s) < 8:
		enlarge(s)
	else:
		print(s)