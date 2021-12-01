#!/usr/bin/python3

"""
the pattern is infinitely repeating to the right
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
From your starting position at the top-left, check the position that is right 3 and down 1. 
Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map
Count each time you land on a tree "#"
"""

import sys
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()
#print(content)

# pseudocode
# linenumber++ position+=3
# if position > len(line) then position - len(line)
# char=line[position-1]
# if char == "#"
#   tree+=1

tree=0
position=1
linenumber=1
for line in content:
    if position > len(line):
        position-=len(line)
    if line[position-1] == "#":
        tree+=1
    position+=3

print("You hit " + str(tree) + " trees!") 

