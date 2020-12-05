#!/usr/bin/python3

"""
Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

import sys
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

results = []

def treeseeker(shift,lineshift):
    tree=0
    position=1
    linenumber=1
    for line in content:
        if position > len(line):
            position-=len(line)
        if lineshift == 1 or (linenumber % lineshift) == 1:
            if line[position-1] == "#":
                tree+=1
            position+=shift
        linenumber+=1
    return tree

def prod(list):
    prod = 1
    for item in list:
        prod = prod * item
    return prod

for (x,y) in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
    amount=treeseeker(x,y)
    results.append(amount)
    print("You hit " + str(amount) + " trees!") 

alltrees=prod(results)
print("product " + str(alltrees))
