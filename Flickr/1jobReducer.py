#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_country = None
current_tag = None
country = None
tag = None

tagDic={}
K=3

def SortAndPrint(tagDic, K):
    k=0
    for tag, count in sorted(tagDic.items(), key=lambda x: x[1], reverse=True):
        if k<K:
            print('  %s   %s' % (tag, count))
            k+=1

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
        if current_tag == tag:
            tagDic[tag] += count
        else :
            tagDic[tag] = count
            current_tag = tag
    else:
        if current_country:
            # print country
            print('%s' % (current_country))
            # order and print the K first 
            SortAndPrint(tagDic, K)
            #init new country
            tagDic.clear()

        tagDic[tag]= count
        current_country = country
        current_tag = tag

# do not forget to output the last country if needed!
if current_country == country:
    # print country
    print('%s' % (current_country))
    # order and print the K first 
    k=0
    for tag, count in sorted(tagDic.items(), key=lambda x: x[1], reverse=True):
        if k<K:
            print('  %s   %s' % (tag, count))
            k+=1
