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

# 5a
# given stacks in day5-stacks.txt
# converted by hand to this:
stacks = ['ZTFRWJG','GWM','JNHG','JRCNW','WFSBGQVM','SRTDVWC','HBNCDZGV','SJNMGC','GPNWCJDL']
# day5-input.txt contains:
# move A(mount) of crates from S(ource) to D(estination) stack (1 at a time)
# return the top crates

# 5b
# similar to 5a but:
# move A(mount) of crates from S(ource) to D(estination) stack (Amount at the same time!)
stacks2 = ['ZTFRWJG','GWM','JNHG','JRCNW','WFSBGQVM','SRTDVWC','HBNCDZGV','SJNMGC','GPNWCJDL']

def move5a(stackarray,amount,source,destination):
    for i in range(amount):
        # lastchar of Source
        L = stackarray[source][-1]
        # add lastchar to destination
        stackarray[destination] += L
        # remove lastchar from source
        stackarray[source] = stackarray[source][:-1]
    return(stackarray)

def move5b(stackarray,amount,source,destination):
    L = stackarray[source][-amount:]
    stackarray[destination] += L
    stackarray[S] = stackarray[source][:-amount]
    return(stackarray)

def lastchars(stackarray):
    topcontainers = ""
    stackcount = len(stackarray)
    for i in range(stackcount):
        topcontainers += stackarray[i][-1]
    return(topcontainers)

for line in content:
    # 5a
    # remove the 'move ',' from ' and ' to ' from the line and split into an array
    splitline = re.split('move | from | to ',line)
    # getting rid of the blank at the front of the array for some reason present...
    splitline = list(filter(None, splitline))
    # Amount
    A = int(splitline[0])
    # Source stack
    S = int(splitline[1])-1
    # Destination stack
    D = int(splitline[2])-1

    result = move5a(stacks,A,S,D)

    # 5b
    result2 = move5b(stacks2,A,S,D)

print(lastchars(result))
print(lastchars(result2))
