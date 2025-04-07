#!/usr/bin/env python3
import sys
if len(sys.argv) == 1:
	print("none")
	sys.exit(1)
print(f"parameters: {len(sys.argv) - 1}")
for s in sys.argv[1:]:
	print(f"{s}: {len(s)}")