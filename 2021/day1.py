#!/usr/bin/python3
# question 1 A
# find all increases of consecutive numbers
# question 1 B
# similar to A but with the sum of a sliding window of 3 numbers

import sys
if len(sys.argv) < 3:
    print("usage: " + sys.argv[0] + " <filename> <windowsize>")
    exit(1)

filename = sys.argv[1]
window_size = int(sys.argv[2])


prevmeasurement=0
increasecounter=0

file = open(filename)
content = file.read().splitlines()
file.close()

# this was for 1A but it can be done by setting window_size = 1
#for measurement in content:

# change for 1 B
#this is now a parameter
#window_size = 3

for i in range(len(content) - window_size + 1):
    measurement = sum(list(map(int,content[i: i + window_size])))
# end change for 1 B

    if prevmeasurement==0:
        prevmeasurement=measurement
    else:
        if prevmeasurement < measurement:
            print(str(measurement) + " increase")
            increasecounter+=1
        else:
            print(str(measurement) + " decrease")
        prevmeasurement=measurement

print(str(increasecounter))
