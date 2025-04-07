#!/usr/bin/env python3
import sys
if len(sys.argv) == 1:
	print("none")
	sys.exit(1)
for s in sys.argv[1:]:
	if not s.endswith("ism"):
		print(f"{s}ism")