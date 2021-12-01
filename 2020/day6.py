#!/usr/bin/python3

"""
6a:
form asks a series of 26 yes-or-no questions marked a through z
Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line.
see day6-example.txt

This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

6b:
You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!
for the example:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""

import sys
import string

if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
#content = file.read().splitlines()
content = file.read().replace("\n"," ").replace("  ","\n").splitlines()
file.close()
#print(content)


# 6a pseudo code
# create alphabet dict with all values 0
# import string
# alphabet = dict.fromkeys(string.ascii_lowercase, 0)
# for each letter from a group set value to 1
# for char in string:
# alphabet[char] = 1
# if empty line summarize:
# sum(alphabet.values())
# after that reset the alphabet dict back to 0
# alphabet = dict.fromkeys(alphabet, 0)
# 6b
# instead of setting the chars to 1 count the occurence and count all chars with an occurence = amount of ansers in the group
# so just abandon the initial = 1 and sum but replace by += 1 and check for > 0 for 6a

def processanswers(answerform):
    totalsum = 0
    totalsum2 = 0
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    for groupanswers in answerform:
        groupmembers = 0
        groupsum = 0
        groupsum2 = 0
        answers = groupanswers.rstrip().split(" ")
        for answer in answers:
            groupmembers += 1
            for char in answer:
                #6a: alphabet[char] = 1
                alphabet[char] += 1
        #6a: groupsum = sum(alphabet.values())
        for value in alphabet.values():
            if value > 0:
                groupsum += 1
            if value == groupmembers:
                groupsum2 += 1
        totalsum += groupsum
        totalsum2 += groupsum2
        alphabet = dict.fromkeys(alphabet, 0)
    print(totalsum)
    print(totalsum2)

processanswers(content)
