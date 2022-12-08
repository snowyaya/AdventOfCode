'''
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?

--- Part Two ---

Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?

'''

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().strip().splitlines()

# print(lines)
rows = len(lines)
cols = len(lines[0])
print("rows: ", rows, "cols: ", cols)

outer_numb_trees = rows*2 + cols*2 - 4
print("outer_numb_trees: ", outer_numb_trees)

matrix = [[0]*cols for i in range(rows)]
# print(matrix)

count = 0
for line in lines:
    row = [int(x) for x in line]
    matrix[count] = row
    count += 1
# print(matrix)

def is_visible(i, j, direction):
    curr_tree = matrix[i][j]
    if direction == "left":
        for k in range(j-1, -1, -1):
            if matrix[i][k] >= curr_tree:
                # print("visible from left tree: ", matrix[i][k])
                return False
    
    elif direction == "right":
        for k in range(j+1, cols):
            if matrix[i][k] >= curr_tree:
                # print("visible from right tree: ", matrix[i][k])
                return False
    
    elif direction == "up":
        for k in range(i-1, -1, -1):
            if matrix[k][j] >= curr_tree:
                # print("visible from up tree: ", matrix[k][j])
                return False
            
    elif direction == "down":
        for k in range(i+1, rows):
            if matrix[k][j] >= curr_tree:
                # print("visible from down tree: ", matrix[k][j])
                return False
    
    return True
    
inner_numb_trees = 0
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        curr_tree = matrix[i][j]
        # print("------- curr_tree: ", curr_tree, "i: ", i, "j: ", j)
        if is_visible(i, j, "left") or is_visible(i, j, "right") or is_visible(i, j, "up") or is_visible(i, j, "down"):
            # print("🔆", curr_tree)
            inner_numb_trees += 1
        
        # left_tree = matrix[i][j-1]
        # right_tree = matrix[i][j+1]
        # up_tree = matrix[i-1][j]
        # down_tree = matrix[i+1][j]
        
        # if curr_tree > left_tree or curr_tree > right_tree or curr_tree > up_tree or curr_tree > down_tree:
        #     print("🔆", curr_tree, left_tree, right_tree, up_tree, down_tree)
        #     inner_numb_trees += 1
        

    
print("inner_numb_trees: ", inner_numb_trees) 
print("Part 1: ", outer_numb_trees + inner_numb_trees)

def get_scenic_score(i, j):
    left, right, up, down = 0, 0, 0, 0
    curr_tree = matrix[i][j]
    # print("------- curr_tree: ", curr_tree, "i: ", i, "j: ", j, "--------")
    # left
    for k in range(j-1, -1, -1):
        if matrix[i][k] >= curr_tree:
            left += 1
            break
        else:
            left += 1
            
    # right
    for k in range(j+1, cols):
        if matrix[i][k] >= curr_tree:
            right += 1
            break
        else:
            right += 1
            
    # up
    for k in range(i-1, -1, -1):
        if matrix[k][j] >= curr_tree:
            up += 1
            break
        else:
            up += 1
    
    # down
    for k in range(i+1, rows):
        if matrix[k][j] >= curr_tree:
            down += 1
            break
        else:
            down += 1
    
    score = left * right * up * down
    # print("🔆 score: ", score)
    return score
    

scenic_scores = []
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        curr_tree = matrix[i][j]
        scenic_scores.append(get_scenic_score(i, j))
# print(scenic_scores)
print("Part 2: ", max(scenic_scores))
        