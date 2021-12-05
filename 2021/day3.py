#!/usr/bin/python3

import array

import sys
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

def arraycompare(array1,array2):
    result=""
    for count in range(0,len(array1)):
        if array1[count]>array2[count]:
            result=result + '0'
        else:
            result=result + '1'
    return result

def inversestring(bit_s):
    inverse_s = ''
    for i in bit_s:
        if i == '0':
            inverse_s += '1'
        else:
            inverse_s += '0'
    return inverse_s

def findgamma(content):
    digits = 5
    zerocount = array.array('i',(0 for i in range(0,digits)))
    onecount = array.array('i',(0 for i in range(0,digits)))

    for binary in content:
        lst = list(binary)
        for count in range(0,len(lst)):
            if int(lst[count])==0:
                zerocount[count]=zerocount[count]+1
            else:
                onecount[count]=onecount[count]+1
    return arraycompare(zerocount,onecount)


## MAIN
bgamma=findgamma(content)
bepsilon=inversestring(bgamma)
#print(bgamma)
#print(bepsilon)
gamma=int(bgamma,2)
epsilon=int(bepsilon,2)
print(gamma)
print(epsilon)
print(gamma*epsilon)
