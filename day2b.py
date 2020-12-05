#!/usr/bin/python3

"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
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
    first = 0
    second = 0
    if password[min-1] == letter:
        first = 1
    #if len(password) >= max and password[max-1] == letter:
    if password[max-1] == letter:
        second = 1
    if first != second:
        validpasswords += 1
        print(minmax + " " + letter + " " + password + " " + password[min-1] + " " + password[max-1] + " OK")
#    else:
#        print(minmax + " " + letter + " " + password + " " + password[min-1] + " " + password[max-1] + " NOK")

print(str(validpasswords))
