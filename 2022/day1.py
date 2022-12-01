#!/usr/bin/python3

import sys
if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().splitlines()
file.close()

elfnumber = 1
caloriecounter = 0
biggestcalories = 0
calorierichelf = 1

# lets make a dict of elfnumber:calories key value pairs
elfdict = {}

for line in content:
  if line == "":
    elfnumber += 1
    caloriecounter = 0
  else:
    caloriecounter += int(line)
    elfdict[elfnumber] = caloriecounter

# print(elfdict)

# 1a find the largest value
for key,value in elfdict.items():
    if value > biggestcalories:
        calorierichelf = key
        biggestcalories = value
print("elf " + str(calorierichelf) + " carries " + str(biggestcalories) + " calories")

# 1b find the top 3 and summarise
# take the dict, sort it
# cast it to list and take the last 3 items
elfcount = len(elfdict)
top3dict = list(sorted(elfdict.items(), key=lambda item: item[1]))[elfcount-3:elfcount]
# print(top3dict)
# summarise the values
counter = 0
for k,v in top3dict:
    counter += v
print("calorie count summary of the top 3 elfs: " + str(counter))
