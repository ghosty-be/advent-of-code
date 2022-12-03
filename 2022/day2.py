#!/usr/bin/python3

import sys
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

# lets make a dict of elfnumber:calories key value pairs
scoredict = { "A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6 }
scoredict2 = { "A X": "A Z", "A Y": "A X", "A Z": "A Y", "B X": "B X", "B Y": "B Y", "B Z": "B Z", "C X": "C Y", "C Y": "C Z", "C Z": "C X" }
counter = 0
counter2 = 0

for line in content:
    print(line + " " + str(scoredict[line]))
    print(line + " " + str(scoredict[scoredict2[line]]))
    counter += scoredict[line]
    counter2 += scoredict[scoredict2[line]]
print("Your total score a is: " + str(counter))
print("Your total score b is: " + str(counter2))

