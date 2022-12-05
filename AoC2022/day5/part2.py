'''
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

'''

from itertools import groupby
import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
new_lines = [x.replace('\n', '') for x in lines]

matrix_and_moves = [list(sub) for ele, sub in groupby(new_lines, key = bool) if ele]
matrix = matrix_and_moves[0]
moves = matrix_and_moves[1]
# print(matrix)

col_nums = matrix[-1]
# print(col_nums)
col_indexes = [i for i, x in enumerate(col_nums) if x.isdigit()]
# print(col_indexes)

# print(moves)

rows = len(matrix) - 1
cols = len(col_indexes)
# print(rows, ' ', cols)

# create a 2D array
crates = [["_" for i in range(cols)] for j in range(rows)]
for i in range(rows):
    col_idx = 0
    for j in col_indexes:
        if matrix[i][j].isalpha():
            # print(i, ' ', j, ' ', matrix[i][j])
            crates[i][col_idx] = matrix[i][j]
        col_idx += 1
        
print('----- Initial Crates -----')
for crate in crates:
    print(crate)
    print()


# Put the crates into stacks
stacks = [[] for i in range(cols)]
for j in range(cols):
    for i in range(rows):
        if crates[i][j] != '*':
            stacks[j].append(crates[i][j])
# print('----- Initial Stacks -----')
# print(stacks)

print('----- Moves -----')
# # print(moves)
move_steps = []
for move in moves:
    move_steps.append([int(x) for i, x in enumerate(move) if x.isdigit()])
# print(move_steps)

for move_step in move_steps:
    count = move_step[0]
    from_stack = move_step[1] - 1
    to_stack = move_step[2] - 1
    
    while count > 0 and len(stacks[from_stack]) > 0:

        stacks[to_stack].insert(0, (stacks[from_stack].pop(0)))
        count -= 1
    # print(stacks)

print('----- Top Crates -----')
sol = ''
for stack in stacks:
    sol += stack[0]