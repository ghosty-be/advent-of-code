#!/usr/bin/python3

import sys
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

# 6a
# message starts after header, consisting of 4 unique characters, how many chars are before the message?

# 6b
# same as 6a but with 14 unique characters

def findstartofmessage(message,headersize):
    # line length
    L = len(message)
    # counter from 0 to line length - headerlength (to be sure we don't overrun end of line)
    for i in range(L-headersize):
        start = i
        end = i+headersize
        header = message[start:end]
        # if unique characters in header = headersize
        if len(set(header)) == headersize:
            #print(header)
            return(str(end))

for line in content:
    # 6a
    print("6a: " + findstartofmessage(line,4))

    # 6b
    print("6b: " + findstartofmessage(line,14))
