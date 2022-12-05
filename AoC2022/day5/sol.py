import re, copy
import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    stack_txt, instruction_data = f.read().split('\n\n')
    stack_txt = stack_txt.split('\n')
    instruction_data = instruction_data.split('\n')
    
stack_last = stack_txt.pop()

stack = {}
loc = {}
ordering = []
for ii in range(len(stack_last)):
    if stack_last[ii] != ' ':
        stack[stack_last[ii]] = []
        loc[stack_last[ii]] = ii
        ordering.append(stack_last[ii])
        
for line in reversed(stack_txt):
    for key in loc.keys():
        if line[loc[key]] != ' ':
            stack[key].append(line[loc[key]])

stack2 = copy.deepcopy(stack)

for line in instruction_data:
    if 'move' in line:
        inst_values = re.findall(r'\d+', line)
        count = int(inst_values[0])
        ff = inst_values[1]
        tt = inst_values[2]
    
        for ii in range(count):
            pop_val = stack[ff].pop()
            stack[tt].append(pop_val)
            
        stack2[tt] += stack2[ff][-count:]
        stack2[ff] = stack2[ff][:-count]

''' Part 1 '''
for ii in ordering:
    print(stack[ii][-1], end='')

print()
''' Part 2 '''
for ii in ordering:
    print(stack2[ii][-1], end='')
    