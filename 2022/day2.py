#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

# 2a
# first column: A for Rock, B for Paper, and C for Scissors
# second column: X for Rock, Y for Paper, and Z for Scissors
# score per line: 
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
# calculate the total score from all rounds
# --
# lets make a dict of elfnumber:calories key value pairs
scoredict = { "A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6 }
counter = 0

# 2b
# same as 2a but:
# second column predicts the outcome:
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
# calculate the new total score from all rounds
scoredict2 = { "A X": "A Z", "A Y": "A X", "A Z": "A Y", "B X": "B X", "B Y": "B Y", "B Z": "B Z", "C X": "C Y", "C Y": "C Z", "C Z": "C X" }
counter2 = 0

for line in content:
    #print(line + " " + str(scoredict[line]))
    #print(line + " " + str(scoredict[scoredict2[line]]))
    counter += scoredict[line]
    counter2 += scoredict[scoredict2[line]]
print("2a: " + str(counter))
print("2b: " + str(counter2))
