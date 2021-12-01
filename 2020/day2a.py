#!/usr/bin/python3

"""
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain 'a' at least 1 time and at most 3 times.
how many passwords are valid?
"""

import sys
from itertools import combinations
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()
#print(content)
validpasswords = 0
array = []
for i in content:
    array.append(i.split(" "))
    for value in array:
        minmax = value[0]
        min = int(minmax.split("-")[0])
        max = int(minmax.split("-")[1])
        letter = value[1].replace(":", "")
        password = value[2]
        count = password.count(letter)
    if count >= min and count <= max:
      validpasswords += 1
      #print(minmax + " " + letter + " " + password + " " + str(count))

print(str(validpasswords))
