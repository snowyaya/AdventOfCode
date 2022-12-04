'''
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

'''

'''
sec1       -------
sec2 -----------------

sec1 -----------------
sec2       --------

sec1 -----------
sec2         ---------

sec1      --------
sec2 ---------         

'''

import os
import sys
from itertools import groupby

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    
newlines =[x.replace('\n', '') for x in lines]
# print(newlines)

pairs = [x.split(',') for x in newlines]
# print(pairs)

total = 0
for pair in pairs:
    sec1_left = int(pair[0].split('-')[0])
    sec1_right = int(pair[0].split('-')[1])
    sec2_left = int(pair[1].split('-')[0])
    sec2_right = int(pair[1].split('-')[1])
    
    if sec1_left >= sec2_left and sec1_right <= sec2_right:
        print(pair)
        total += 1
    elif sec1_left <= sec2_left and sec1_right >= sec2_right:
        print(pair)
        total += 1
    elif sec1_left <= sec2_left and sec1_right >= sec2_left:
        print(pair)
        total += 1
    elif sec1_left >= sec2_left and sec1_left <= sec2_right:
        print(pair)
        total += 1
print(total)
