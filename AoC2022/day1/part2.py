'''
--- Part Two ---

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

'''

import os
import sys
from itertools import groupby
import random
    
# with open('input.txt') as f:
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()

#remove newlines
newlines =[x.replace('\n', '') for x in lines]

res = [list(sub) for ele, sub in groupby(newlines, bool) if ele]

sum_list = []
for i in res:
    curr_sum = 0
    for j in i:
        curr_sum += int(j)
    sum_list.append(curr_sum)
     # kth largest is (n - k)th smallest 

def merge(nums, l, m, r):
    
    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * (n1)
    R = [0] * (n2)
    
    for i in range(0, n1):
        L[i] = nums[l + i]
    for j in range(0, n2):
        R[j] = nums[m + 1 + j]
        
    i = 0
    j = 0
    k = l
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        nums[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        nums[k] = R[j]
        j += 1
        k += 1
        
def mergeSort(nums, l , r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(nums, l, m)
        mergeSort(nums, m + 1, r)
        merge(nums, l, m, r)
        
mergeSort(sum_list, 0, len(sum_list) - 1)
print(sum_list[-3:])
print(sum(sum_list[-3:]))
