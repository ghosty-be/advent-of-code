#!/usr/bin/python3

"""
4a:
all data seperated with an empty line are key value pairs (with random newlines in them) for one passport
figure out how much passports have the keys: ["byr","iyr","eyr","hgt","hcl","ecl","pid"] in them
4b:
for all the passports that have the above keys in them do a check of the values for some patterns:
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

import sys
import re

if len(sys.argv) < 2:
    print("usage: " + sys.argv[0] + " <filename>")
    exit(1)

filename = sys.argv[1]

file = open(filename)
content = file.read().replace("\n"," ").replace("  ","\n").splitlines()
file.close()
#print(content)

keyvaluepairs = []

# content looks like
# ['a:b c:d', 'e:f g:h']
# converting that to a dict with key value pairs
# [{'a': 'b', 'c': 'd'}, {'e': 'f', 'g': 'h'}]
def stringdict2keyvaluepairdict(stringdict):
    keyvaluepairdict = []
    for string in stringdict:
        #rstrip needed to get rid of the last space caused by the last newline in the file
        res = dict(item.split(":") for item in string.rstrip().split(" "))
        keyvaluepairdict.append(res)
    return keyvaluepairdict

def checkpassports(keyvaluepairdict):
    presentcounter = 0
    validcounter = 0
    for passport in keyvaluepairdict:
        #print(passport)
        if checkfields(passport):
            presentcounter+=1
            validcounter+=validatefields(passport)
    print("passports with all required fields present: " + str(presentcounter))
    print("passports with all required fields valid: " + str(validcounter))

def checkfields(passport):
    requiredfields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    hasallfields = 1
    for field in requiredfields:
        if field not in passport:
            hasallfields = 0
            break
    return hasallfields

def validatefields(passport):
    eyecolors = ['amb','blu','brn','gry','grn','hzl','oth']
    validfields = 0
    byr = passport.get('byr')
    if re.match(r"^[0-9]{4}$", byr) and int(byr) >= 1920 and int(byr) <= 2002:
        validfields+=1
    iyr = passport.get('iyr')
    if re.match(r"^[0-9]{4}$", iyr) and int(iyr) >= 2010 and int(iyr) <= 2020:
        validfields+=1
    eyr = passport.get('eyr')
    if re.match(r"^[0-9]{4}$", eyr) and int(eyr) >= 2020 and int(eyr) <= 2030:
        validfields+=1
    hgt = passport.get('hgt')
    if re.match(r"^[0-9]{2}in$", hgt) and int(hgt.rstrip('in')) >= 59 and int(hgt.rstrip('in')) <= 76:
        validfields+=1
    if re.match(r"^[0-9]{3}cm$", hgt) and int(hgt.rstrip('cm')) >= 150 and int(hgt.rstrip('cm')) <= 193:
        validfields+=1
    hcl = passport.get('hcl')
    if re.match(r"^#[0-9a-f]{6}$", hcl): 
        validfields+=1
    ecl = passport.get('ecl')
    if ecl in eyecolors:
        validfields+=1
    pid = passport.get('pid')
    if re.match(r"^[0-9]{9}$", pid):
        validfields+=1
    if validfields == 7:
        return 1
    else:
        return 0

passportdict = stringdict2keyvaluepairdict(content)
checkpassports(passportdict)
