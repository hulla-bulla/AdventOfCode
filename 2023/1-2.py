#!/usr/bin/env python
from pprint import pprint

FILE = "1-2.test"
FILE = "1-2.input"

with open(FILE, "r") as f:
    data = [x.strip() for x in f.readlines()]


spelled_numbers = ("one",
                   "two",
                   "three",
                   "four",
                   "five",
                   "six",
                   "seven",
                   "eight",
                   "nine")

numbers = []

for x in data:

    digitized = ""
    for i in range(len(x)):
        if x[i].isdigit():
            digitized += x[i]

        for number in spelled_numbers:
            if x[i:i+len(number)] == number:
                digitized += str(spelled_numbers.index(number)+1)

    numbers.append(int("".join((digitized[0], digitized[-1]))))

result = sum(numbers)

print(result)


####
