#!/usr/bin/env python
from pprint import pprint

FILE = "1-1.test"
FILE = "1-1.input"

with open(FILE, "r") as f:
    data = [x.strip() for x in f.readlines()]


numbers = ["".join([y for y in x if y.isdigit()]) for x in data]


result = sum([int(f"{x[0]}{x[-1]}") for x in numbers])

print(result)


####

