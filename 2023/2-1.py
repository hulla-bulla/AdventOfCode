#!/usr/bin/env python
from pprint import pprint

FILE = "2-1.test"
FILE = "2-1.input"

with open(FILE, "r") as f:
    data = [x.strip() for x in f.readlines()]

pprint(data)

limit = {'red': 12, 'green': 13, 'blue': 14}

parsed = [[{y.split()[1]: int(y.split()[0]) for y in x.split(", ")}
           for x in game.split(": ")[1].split("; ")]
          for game in data]

validgames = [game for game in parsed
              if all([v <= limit[k] for sett in game for (k, v) in sett.items()])]

games = [parsed.index(x)+1 for x in validgames]

result = sum(games)

print(result)
