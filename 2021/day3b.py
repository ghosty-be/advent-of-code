#!/usr/bin/python3

import re
import sys

# read input file from cli and split lines in the 'content' variable
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()
# end reading input file

def binlisttoint(binlist):
    return int(''.join(map(str,binlist)),2)

def filterbinlist(binlist, flip=False, index=0, filterstring=""):
    zerocounter=0
    onecounter=0
    '''
    print(binlist)
    print(index)
    print(filterstring)
    print(len(binlist))
    '''

    # end recursion 
    # base condition: amount of binary numbers in the list == 1
    if len(binlist)==1:
        #print(binlisttoint(binlist))
        return binlisttoint(binlist)
    
    if len(binlist)>1:
        # proces each number in the list
        for number in binlist:
            if int(number[index])==0:
                zerocounter+=1
            else:
                onecounter+=1
        if not flip:
            if zerocounter>onecounter:
                filterstring=filterstring + '0'
            else:
                filterstring=filterstring + '1'
        else:
            if onecounter<zerocounter:
                filterstring=filterstring + '1'
            else:
                filterstring=filterstring + '0'
        # filter it out
        r = re.compile("^"+filterstring)
        filtered_list = list(filter(r.match, binlist))
        index+=1
        # recursion
        return filterbinlist(filtered_list,flip,index,filterstring)

## MAIN
oxygen=filterbinlist(content)
print(oxygen)
co2=filterbinlist(content,True)
print(co2)

prod=oxygen * co2
print(prod)
