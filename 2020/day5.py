#!/usr/bin/python3

"""
5a:
find the highest seat number for binary space partitioning like for example FBFBBFFRLR
ROW: first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.

COLUMN the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.

seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357

5b:
your seat should be the only missing boarding pass in your list. 
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?

"""

import sys
import re

if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()
#print(content)

# 5a pseudo code
# convert F to 0
# convert B to 1
# convert R to 1 
# convert L to 0
# then just cast to int with base 2

def processpasses(passcodes):
    seatids = []
    remainingseats = [] 
    highseat = 0
    lowseat = 127 * 8 + 7
    for passcode in passcodes:
        row = passcode[0:7]
        column = passcode[7:10]
        row = convertrowtoint(row)
        column = convertcolumntoint(column)
        seatid = row * 8 + column
        print(str(passcode) + " " + str(row) + " " + str(column) + " " + str(seatid))
        seatids.append(seatid)
        if seatid > highseat:
            highseat = seatid
        if seatid < lowseat:
            lowseat = seatid
    print("highest seat number " + str(highseat))
    allseatids = list(range(lowseat,highseat+1))
    remainingseats = Diff(allseatids, seatids) 
    print("your seat has ID: " + str(remainingseats))

def convertrowtoint(row):
    # to binary
    srow = row.replace('F','0').replace('B','1')
    # to int
    irow = int(srow,2)
    return irow
    
def convertcolumntoint(column):
    # to binary
    scolumn = column.replace('L','0').replace('R','1')
    # to int
    icolumn = int(scolumn,2)
    return icolumn

# Python code to get difference of two lists
# Not using set()
def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

processpasses(content)
