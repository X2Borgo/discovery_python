#!/usr/bin/env python3
def famous_births(scientists):
	if not isinstance(scientists, dict):
		return
	i = 0
	while i < len(scientists):
		lowest = min(scientists, key=lambda x: scientists[x]["date_of_birth"])
		name = scientists[lowest]["name"]
		date = scientists[lowest]["date_of_birth"]
		print(f"{name} is a great scientist born in {date}.")
		scientists.pop(lowest)

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)