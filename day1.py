#!/usr/bin/python3
# question 1 A
# find the two entries that sum to 2020
# then multiply those two numbers together
# question 1 B
# instead of two entries find 3 entries

import sys
from itertools import combinations
if len(sys.argv) < 3:
    print("usage: " + sys.argv[0] + " <filename> <amount>")
    exit(1)

filename = sys.argv[1]
amount = int(sys.argv[2])

file = open(filename)
content = file.read().splitlines()
file.close()
#print(content)
prod = 1
# convert to int
icontent = map(int, content)
contentcomb = combinations(icontent, amount)
for comb in contentcomb:
    if sum(comb) == 2020:
        print(comb)
        for i in comb:
            prod = prod * i
        print(prod)
