import sys 
import os 
import re

with open(os.path.join(sys.path[0], "input0.txt"), "r") as f:
    lines = f.read().strip().splitlines()

'''
Rules
1. noop does not change anything
2. At the start and during and (i)Addx cycle the register value doesn't change
3. After the (i+1) Addx cycle, the register value changes
'''

register_value = 1
cycle_num = 1
cycles = [20, 60, 100, 140, 180, 220]
visited = set()
cycles_and_values = []

CRT_num = 0 # resets to 0 after 40
sprite_pos= 0
image = [["."] * 40 for i in range(6)]
# print(image)
col = 0
hash_loc = set()

for line in lines:
    if line == "noop":  
        # print("---Begin noop cycle", cycle_num, "register value is", register_value)      
        cycles_and_values.append((cycle_num, register_value))
        cycle_num += 1
        cycles_and_values.append((cycle_num, register_value))
        # print("---After noop", cycle_num, "register value is", register_value)
        
        # CRT_num += 1
        # if CRT_num == 40:
        #     CRT_num = 0
        #     col += 1
    elif line.startswith("addx"):
        # print("---Begin addx cycle", cycle_num, "register value is", register_value)
        cycle_num += 1
        cycles_and_values.append((cycle_num, register_value))
        curr_value = re.findall(r'-?\d+', line)[0]
        # print("---During addx cycle", cycle_num, "register value is", register_value)
        
        # sprite_pos = register_value
        # print("CRT_num", CRT_num, "sprite_pos", sprite_pos, "col", col)
        # if CRT_num == sprite_pos or CRT_num == sprite_pos + 1 or CRT_num == sprite_pos - 1:
        #     image[CRT_num][col] = "#"
        #     hash_loc.add((CRT_num, col))
        
        # CRT_num += 1
        # if CRT_num == 40:
        #     CRT_num = 0
        #     col += 1
        
        cycle_num += 1
        register_value += int(curr_value)
        # print("~~~After addx cycle", cycle_num, "register value is", register_value)
        cycles_and_values.append((cycle_num, register_value))
        
        # CRT_num += 1
        # if CRT_num == 40:
        #     CRT_num = 0
        #     col += 1
# print(cycles_and_values)

sum_ = 0
for cycle in cycles:
    for cycle_and_value in cycles_and_values:
        if cycle_and_value[0] == cycle and cycle not in visited:
            visited.add(cycle)
            sum_ += cycle_and_value[1] * cycle
            # print("Cycle", cycle, "register value is", cycle_and_value[1])

print("Part 1:", sum_)
# print("Part 2:", image)

