#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_country = None
current_tag = None
current_count = 0
country = None
tag = None

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

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: country) before it is passed to the reducer
    if current_country == country and current_tag == tag:
        current_count += count
    else:
        if current_country:
            # write result to STDOUT
            print ('%s\t%s\t%s' % (current_country, current_tag, current_count))
            
        current_count = count
        current_country = country
        current_tag = tag

# do not forget to output the last country if needed!
if current_country == country and current_tag == tag:
    print ('%s\t%s\t%s' % (current_country, current_tag, current_count))
