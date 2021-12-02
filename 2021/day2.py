#!/usr/bin/python3
# start position (0,0)
# question A
# given forward, up (negative depth), down (positive depth) 
# what is the product of the final position (forward,depth)
# question B
# instead of up and down having a direct impact you have an "aim"
# up (negative depth) and down (positive depth) are added to the aim value
# the aim only changes depth when you move forward by increasing depth by the aim * forward
# what is the product of the final position (forward,depth)

import sys
from itertools import combinations
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

# addition for B
aim=0

# A:
# forward, depth
# array = [ 0, 0 ]
# B:
# forward, depth, depthwithaim
array = [ 0, 0, 0 ]

for line in content:
    linear=line.split(" ")
    # forward
    if linear[0]=="forward":
        array[0]+=int(linear[1])
        # addition for B
        array[2]=array[2]+(aim*int(linear[1]))
    # up
    elif linear[0]=="up":
        array[1]-=int(linear[1])
        # addition for B
        aim-=int(linear[1])
    # down
    else:
        array[1]+=int(linear[1])
        # addition for B
        aim+=int(linear[1])

finalposition=array[0]*array[1]
print("A: " + str(finalposition))
finalpositionwithaim=array[0]*array[2]
print("B: " + str(finalpositionwithaim))
