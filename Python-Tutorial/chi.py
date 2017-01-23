# Name:        module1
# Purpose:      Program to toss a coin 18 times and get I Ching Hexagram (Number & Name).
# Author:      Narotam Singh
# Created:     26-04-2013
# Copyright:   (c) Narotam Singh 2013
import random

# - by NS
def onetoss():
    a = 0
    s = ""
    while a < 3:
        a = a + 1
        n = random.randint(0, 1)
        if n == 1:
            r = "H"
        if n == 0:
            r = "T"
        s = s + r
    return s

def half_name(s):
    if s == "------- -":
        n = "Lake"
    elif s == "---- ----":
        n = "Flame"
    elif s == "- -------":
        n = "Wind"
    elif s == "- -- -- -":
        n = "Earth"
    elif s == "- -- ----":
        n = "Mountain"
    elif s == "- ----- -":
        n = "Water"
    elif s == "---- -- -":
        n = "Thunder"
    elif s == "---------":
        n = "Heaven"
    return n

def toss():
    ## 3 times onetoss() ##
    i = 3
    j = 0
    s = ""
    while j < i:
        j = j + 1
        t = onetoss()
        if (t == "HTH" or t == "THH" or t == "HHT"):
            u = "- -"
        elif t == "HHH":
            u = "---"
        elif t == "TTT":
            u = "- -"
        elif (t == "HTT" or t == "TTH" or t == "THT"):
            u = "---"
        s = s + u
        print u
    # print s
    return half_name(s)

def tossl(i):
    ## ith times onetoss() ##
    j = 0
    s = ""
    l = []
    while j < i:
        j = j + 1
        t = onetoss()
        if (t == "HTH" or t == "THH" or t == "HHT"):
            s = "- -"
        elif t == "HHH":
            s = "---"
        elif t == "TTT":
            s = "- -"
        elif (t == "HTT" or t == "TTH" or t == "THT"):
            s = "---"
        l.append(s)
    l.reverse()
    print '\n'.join(l)

def fulli():
    j = 0
    l = ["Lake", "Flame", "Wind", "Earth", "Mountain", "Water", "Thunder", "Heaven"]
    while j < i:
        s = "Wind"
        t = l[j]
        print "elif s == '", t, "over", s, "':"
        print "        u= 1"
        j = j + 1

def full():
    s = toss()
    t = toss()
    v = t + " over " + s
    return v

def dis(s):
    u = 0
    if s == 'Lake over Lake':
        u = 58
    elif s == 'Flame over Lake':
        u = 38
    elif s == 'Wind over Lake':
        u = 61
    elif s == 'Earth over Lake':
        u = 19
    elif s == 'Mountain over Lake':
        u = 41
    elif s == 'Water over Lake':
        u = 60
    elif s == 'Thunder over Lake':
        u = 54
    elif s == 'Heaven over Lake':
        u = 10
    elif s == 'Lake over Flame':
        u = 49
    elif s == 'Flame over Flame':
        u = 30
    elif s == 'Wind over Flame':
        u = 37
    elif s == 'Earth over Flame':
        u = 36
    elif s == 'Mountain over Flame':
        u = 22
    elif s == 'Water over Flame':
        u = 63
    elif s == 'Thunder over Flame':
        u = 55
    elif s == 'Heaven over Flame':
        u = 13
    elif s == 'Lake over Wind':
        u = 28
    elif s == 'Flame over Wind':
        u = 50
    elif s == 'Wind over Wind':
        u = 57
    elif s == 'Earth over Wind':
        u = 46
    elif s == 'Mountain over Wind':
        u = 18
    elif s == 'Water over Wind':
        u = 48
    elif s == 'Thunder over Wind':
        u = 32
    elif s == 'Heaven over Wind':
        u = 44
    elif s == 'Lake over Earth':
        u = 45
    elif s == 'Flame over Earth':
        u = 35
    elif s == 'Wind over Earth':
        u = 20
    elif s == 'Earth over Earth':
        u = 2
    elif s == 'Mountain over Earth':
        u = 23
    elif s == 'Water over Earth':
        u = 8
    elif s == 'Thunder over Earth':
        u = 16
    elif s == 'Heaven over Earth':
        u = 12
    elif s == 'Lake over Mountain':
        u = 31
    elif s == 'Flame over Mountain':
        u = 56
    elif s == 'Wind over Mountain':
        u = 53
    elif s == 'Earth over Mountain':
        u = 15
    elif s == 'Mountain over Mountain':
        u = 52
    elif s == 'Water over Mountain':
        u = 39
    elif s == 'Thunder over Mountain':
        u = 62
    elif s == 'Heaven over Mountain':
        u = 33
    elif s == 'Lake over Water':
        u = 47
    elif s == 'Flame over Water':
        u = 64
    elif s == 'Wind over Water':
        u = 59
    elif s == 'Earth over Water':
        u = 7
    elif s == 'Mountain over Water':
        u = 4
    elif s == 'Water over Water':
        u = 29
    elif s == 'Thunder over Water':
        u = 40
    elif s == 'Heaven over Water':
        u = 6
    elif s == 'Lake over Thunder':
        u = 17
    elif s == 'Flame over Thunder':
        u = 21
    elif s == 'Wind over Thunder':
        u = 42
    elif s == 'Earth over Thunder':
        u = 24
    elif s == 'Mountain over Thunder':
        u = 27
    elif s == 'Water over Thunder':
        u = 3
    elif s == 'Thunder over Thunder':
        u = 51
    elif s == 'Heaven over Thunder':
        u = 25
    elif s == 'Lake over Heaven':
        u = 43
    elif s == 'Flame over Heaven':
        u = 14
    elif s == 'Wind over Heaven':
        u = 9
    elif s == 'Earth over Heaven':
        u = 11
    elif s == 'Mountain over Heaven':
        u = 26
    elif s == 'Water over Heaven':
        u = 5
    elif s == 'Thunder over Heaven':
        u = 34
    elif s == 'Heaven over Heaven':
        u = 1
    print u
    print s

s = full()
dis(s)

