#!/usr/bin/env python
from pprint import pprint
from functools import reduce

FILE = "2-2.test"
FILE = "2-2.input"

with open(FILE, "r") as f:
    data = [x.strip() for x in f.readlines()]

pprint(data)

limit = {'red': 12, 'green': 13, 'blue': 14}

parsed = [[{y.split()[1]: int(y.split()[0]) for y in x.split(", ")}
           for x in game.split(": ")[1].split("; ")]
          for game in data]

pprint(parsed)

game = parsed[0]
games = []
for game in parsed:
    games.append({})
    for sett in game:
        for k, v in sett.items():
            if games[-1].get(k):
                if v > games[-1].get(k):
                    games[-1][k] = v
            else:
                games[-1][k] = v

games_multiplied = [reduce(lambda x, y: x*y, game.values()) for game in games]


result = sum(games_multiplied)


print(result)
