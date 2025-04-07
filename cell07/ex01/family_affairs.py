#!/usr/bin/env python3
def find_the_redheads(family):
	if not isinstance(family, dict):
		return None
	arr = []
	for key in family:
		if family[key] == 'red':
			arr.append(key)
	return arr

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))