#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_country = None
current_tag = None
country = None
tag = None

K=3

class tagList:
    def __init__(self, K):
        self.tagList = [None for k in range(K)]
        self.countList = [0 for k in range(K)]
        self.K=K

    def update(self, tag, count):
        index = -1
        for i, elem in enumerate(self.countList):
            if count > elem:
                index=i
        if index==0:
            self.tagList= [tag] + self.tagList[1:]
            self.countList= [count] + self.countList[1:]
        if index>0:
            self.tagList=self.tagList[1:index+1] + [tag] + self.tagList[index+1:]
            self.countList=self.countList[1:index+1] + [count] + self.countList[index+1:]

    def printTag(self):
        for tag in reversed(self.tagList):
            if tag:
                print ('  %s' % (tag))

    def printTagCount(self):
        for i in range(self.K):
            if self.tagList[self.K-1-i]:
                print ('  %s   %s' % (self.tagList[self.K-1-i], self.countList[self.K-1-i]))


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    country, tag, count = line.split('\t', 2)


    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if current_country == country:
        bestTag.update(tag, count)

    else:
        if current_country:
            # print country
            print('%s' % (current_country))
            # print the K first
            bestTag.printTagCount()
        #init 
        bestTag=tagList(K)
        bestTag.update(tag, count)
        current_country = country
        current_tag = tag

# do not forget to output the last country if needed!
if current_country == country:
    # print country
    print('%s' % (current_country))
    # print the K first
    bestTag.printTagCount()