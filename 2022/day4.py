#!/usr/bin/python3

import sys
import re

if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

# 4a
# range pairs like start1-end1,start2-end2 
# In how many pairs does one range fully contain the other
matches = 0

# 4b
# In how many pairs do the ranges overlap? (only partially)
overlap = 0

for line in content:
    # 4a
    # split line on , and - to get an array with the 4 values
    # gets you an array: [start1,end1,start2,end2]
    splitline = re.split(',|-',line)
    # make all values type int
    splitline = [int(x) for x in splitline]
    # make it easier to read
    start1 = splitline[0]
    end1 = splitline[1]
    start2 = splitline[2]
    end2 = splitline[3]

    if ((start1 >= start2) and (end1 <= end2)) or ((start2 >= start1) and (end2 <= end1)):
        matches += 1

    # 4b
    if ((start1 >= start2) and (start1 <= end2)) or ((start2 >= start1) and (start2 <= end1)):
        overlap += 1
print("4a: " + str(matches))
print("4b: " + str(overlap))
