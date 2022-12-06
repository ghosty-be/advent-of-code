#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

# 3a
# split each line in half, find a char that is present in the first and second half
# assign the value a - z = 1 - 26 or A - Z = 27 - 52
# make a sum of those values
# I need a dict here with keys a - z with values 1 - 26 and A - Z with values 27 - 52 
import string
lowercasedict = dict(zip(string.ascii_lowercase, range(1,27)))
uppercasedict = dict(zip(string.ascii_uppercase, range(27,53)))
alphabetvalues = lowercasedict | uppercasedict
totalsum=0

# 3b
# find a common char in 3 consecutive lines
# assign that char a value, see 3a
# make a sum of those values
linecounter=0
# I need a dict here with keys a - z and A - Z with value 0
lowercasepack = dict.fromkeys(string.ascii_lowercase, 0)
uppercasepack = dict.fromkeys(string.ascii_uppercase, 0)
charcounter = lowercasepack | uppercasepack
groupsum=0

for line in content:
    # 3a
    linelength = len(line)
    halfline = int(len(line)/2)
    firsthalf = line[0:halfline]
    secondhalf = line[halfline:linelength]
    #print(firsthalf + " " + secondhalf)
    for char in firsthalf:
        if char in secondhalf:
            #print(char)
            #print(str(alphabetvalues[char]))
            totalsum += alphabetvalues[char]
            # multiple matches are common, so we break at the first match
            # cleaner would have been that I just make all chars unique in both halves (see 3b, this could have saved some time and stupid logic)
            break
    # 3b
    # i need a linecounter here to process 3 lines
    linecounter += 1
    # lets drop all duplicate characters from a line and sort it (uppercase chars are sorted before lowercase)
    for char in sorted(set(line)):
        # for every character we find increase the count by 1
        charcounter[char] += 1
    # we processed 3 lines
    if linecounter == 3:
        # find the key (character) where the value == 3 (hence it's present in all 3 strings)
        commonitemchar = list(charcounter.keys())[list(charcounter.values()).index(3)]
        # translate that character to a value and add the value to groupsum
        groupsum += alphabetvalues[commonitemchar]
        # reset linecounter
        linecounter = 0
        # set all values back to 0
        charcounter = dict.fromkeys(charcounter, 0)
print(str(totalsum))
print(str(groupsum))
