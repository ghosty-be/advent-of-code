#!/usr/bin/python3

"""
6a:
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

def processanswers(answerform):
    totalsum = 0
    totalsum2 = 0
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    alphabet2 = dict.fromkeys(string.ascii_lowercase, 0)
    for groupanswers in answerform:
        groupmembers = 0
        groupsum = 0
        groupsum2 = 0
        answers = groupanswers.rstrip().split(" ")
        for answer in answers:
            groupmembers += 1
            for char in answer:
                #alphabet[char] = 1
                alphabet[char] += 1
        #groupsum = sum(alphabet.values())
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
