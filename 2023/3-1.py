#!/usr/bin/env python
from pprint import pprint
from functools import reduce

FILE = "3-1.input"
FILE = "3-1.test"

with open(FILE, "r") as f:
    data = [x.strip() for x in f.readlines()]


pprint(data)

potential_neighbours_indexes = []
for y in range(len(data)):
    # print(data[y])
    for x in range(len(data[y])):
        if not data[y][x].isdigit() \
                and not data[y][x].isalpha() \
                and not data[y][x] == ".":

            print(f"x:{x} y:{y} {data[y][x]}")

            neighbours = [
                (
                    min(max(x+i, 0), len(data[y])),
                    min(max(y+ii, 0), len(data))
                )
                for i in range(-1, 2) for ii in range(-1, 2)
                if not (i == 0 and ii == 0)
            ]

            potential_neighbours_indexes.extend(neighbours)

# remove dups
potential_neighbours_indexes = list(set(potential_neighbours_indexes))
potential_neighbours_indexes.sort()

neighbour_indexes = []
for x, y in potential_neighbours_indexes:
    # print((x, y))
    if data[y][x].isdigit():

        valid_start = None
        for start in range(x, -1, -1):

            if valid_start and not data[y][start].isdigit():
                # aleady found start
                break
            elif data[y][start].isdigit():
                valid_start = start

        valid_end = None
        for end in range(x, len(data[y])):
            if valid_end and not data[y][end].isdigit():
                # aleady found end
                break
            elif data[y][end].isdigit():
                valid_end = end

        print(f"y: {y}")
        print(f"start: {valid_start}")
        print(f"end: {valid_end}")
        print(f"thing: {data[y][valid_start:valid_end+1]}")

        neighbour_indexes.append((y, valid_start, valid_end+1))

neighbour_indexes = list(set(neighbour_indexes))

result = sum([int(data[y][start:end])
             for (y, start, end) in neighbour_indexes])

print(result)
