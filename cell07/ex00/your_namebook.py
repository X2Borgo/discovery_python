#!/usr/bin/env python3
def array_of_names(persons):
	if not isinstance(persons, dict):
		return None
	arr = []
	for key in persons:
		arr.append(key.capitalize() + " " + persons[key].capitalize())
	return arr

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}
print(array_of_names(persons))