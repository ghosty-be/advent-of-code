#!/usr/bin/python3

"""
7a:
"""

import sys
import string
import re

if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
#content = file.read().replace("\n"," ").replace("  ","\n").splitlines()
file.close()
#print(content)

bagcolor = "shiny gold"

bagcolor = bagcolor.replace(" ", "_")

def formatline(dirtystring):
    return(re.sub(' bags contain [\d ]*| bag[s]*, [\d]* | bag[s]*\.', '+', dirtystring).replace(" ", "_").replace("+", " ").rstrip())

def strings2kvpairdict(string):
    keyvaluepairdict = {}
    array = []
    for kv in string.split(' '):
        array =  kv.split(':')
        keyvaluepairdict[array[1]] = array[0]
    return(keyvaluepairdict)
    #return keyvaluepairdict
    #print(list(keyvaluepairdict.keys())[0])


def formatline7b(dirtystring):
    substring = re.sub(' bags contain no other bags\.| bags contain| bag[s]*[,|\.]', '', dirtystring)
    substring = re.sub(r' (\d) ', r'-\1:', substring)
    substring = '1:' + substring.replace(' ', '_').replace('-', ' ')
    return(substring)
    #strings2keyvaluepairdict(substring)

def listwithnesteddict(input):
    listallcolors = []
    for line in input:
        # reformat line
        line = formatline7b(line)
        linedict = strings2kvpairdict(line)
        listallcolors.append(linedict)
    return(listallcolors)

    
def tonestedlist(input):
    listallcolors = []
    for line in input:
        cleanline = formatline(line)
        listlinecolors = []
        for item in cleanline.split(" "):
            listlinecolors.append(item)
        listallcolors.append(listlinecolors)
    return(listallcolors)

def searchcolor(color,colorlist):
    for colorline in colorlist:
        # we start at index 1
        index = 1
        length = len(colorline)
        while index < length:
            if colorline[index] == color:
                # no duplicate colors should be added to my list
                if colorline[0] not in matchedcolors:
                    matchedcolors.append(colorline[0])
                    searchcolor(colorline[0], colorlist)
            index += 1
    return matchedcolors

def searchcolorb(color,colordictlist):
    for colordict in colordictlist:
        # we start at index 1
        index = 1
        length = len(colordict)
        while index < length:
            colorkeys = list(colordict.keys())
            if str(colorkeys[index]) == color:
                # no duplicate colors should be added to my list
                if colorkeys[0] not in matchedcolors:
                    matchedcolors.append(colorkeys[0])
                    searchcolorb(colorkeys[0], colordictlist)
            index += 1
    return matchedcolors

#colorlist = tonestedlist(content)
#matchedcolors = [] 
#matchedcolors = searchcolor(bagcolor,colorlist)
#print(matchedcolors)
#print(len(matchedcolors))

colordictlist = listwithnesteddict(content)
matchedcolors = [] 
matchedcolors = searchcolorb(bagcolor,colordictlist)
print(matchedcolors)
print(len(matchedcolors))

