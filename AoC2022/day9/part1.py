'''
Rules:
1. the head (H) and tail (T) must always be touching 
(diagonally adjacent and even overlapping both count as touching)
2. If the head is ever two steps directly up, down, left, or right from the tail, 
the tail must also move one step in that direction so it remains close enough
3. Otherwise, if the head and tail aren't touching and aren't in the same row or column, 
the tail always moves one step diagonally to keep up
4. After each step, you'll need to update the position of the tail if the step means 
the head is no longer adjacent to the tail.

R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

== Initial State ==

......
......
......
......
H.....  (H covers T, s)

== R 4 ==

......
......
......
......
TH....  (T covers s)

......
......
......
......
sTH...

......
......
......
......
s.TH..

......
......
......
......
s..TH.

== U 4 ==

......
......
......
....H.
s..T..

......
......
....H.
....T.
s.....

......
....H.
....T.
......
s.....

....H.
....T.
......
......
s.....

== L 3 ==

...H..
....T.
......
......
s.....

..HT..
......
......
......
s.....

.HT...
......
......
......
s.....

== D 1 ==

..T...
.H....
......
......
s.....

== R 4 ==

..T...
..H...
......
......
s.....

..T...
...H..
......
......
s.....

......
...TH.
......
......
s.....

......
....TH
......
......
s.....

== D 1 ==

......
....T.
.....H
......
s.....

== L 5 ==

......
....T.
....H.
......
s.....

......
....T.
...H..
......
s.....

......
......
..HT..
......
s.....

......
......
.HT...
......
s.....

......
......
HT....
......
s.....

== R 2 ==

......
......
.H....  (H covers T)
......
s.....

......
......
.TH...
......
s.....

'''

import sys 
import os 

with open(os.path.join(sys.path[0], "input0.txt"), "r") as f:
    lines = f.read().strip().splitlines()

moves = []
for line in lines:
    moves.append(line.split())

def move(direction, cell):
    i, j = cell 
    
    if direction == 'L':
        j -= 1
    
    elif direction == 'R':
        j += 1
        
    elif direction == 'U':
        i -= 1
        
    elif direction == 'D':
        i += 1
    
    elif direction == 'DLU-V':
        i -= 1
        j -= 1
    elif direction == 'DLU-H':
        i -= 1
        j -= 1
    
    elif direction == 'DRU-V':
        i -= 1
        j += 1
    elif direction == 'DRU-H':
        i -= 1
        j += 1
    
    elif direction == "DLD-V":
        i += 1
        j -= 1
    elif direction == "DLD-H":
        i += 1
        j -= 1
    
    elif direction == "DRD-V":
        i+= 1
        j += 1
    elif direction == "DRD-H":
        i += 1
        j += 1
        
    return (i, j)


def is_touching(head, tail):
    h_i, h_j = head
    t_i, t_j = tail
    
    # overlapping
    if h_i == t_i and h_j == t_j:
        return True

    # same row adjacent
    elif h_i == t_i and abs(h_j - t_j) == 1:
        return True
    
    # same column adjacent
    elif h_j == t_j and abs(h_i - t_i) == 1:
        return True
    
    # diagonal adjacent
    elif abs(h_i - t_i) == 1 and abs(h_j - t_j) == 1:
        return True
    
    else:
        return False


head_pos = (0, 0)
tail_pos = (0, 0)

part1_visited = set()
part1_visited.add(tail_pos)

for m in moves:
    print("~~~~~~ 🔆 ", m, "~~~~~~")
    direction = m[0]
    steps = int(m[1])
    while steps > 0:
        # Head moves
        new_head_pos = move(direction, head_pos)
        head_new_i, head_new_j = new_head_pos
        head_pos = new_head_pos
        steps -= 1
        
        # Check if head is touching tail 
        # print("~~~~ before checking if head is touching tail ~~~~")
        print("head pos: ", head_pos, "tail pos: ", tail_pos)
        if is_touching(head_pos, tail_pos):
            print("**** ✅ head is touching tail ****")
            
        # tail moves
        else: 
            print("**** ❌ head is not touching tail ****")
            x = head_pos[0] - tail_pos[0]
            y = head_pos[1] - tail_pos[1]
            print("x: ", x, "y: ", y)
            
            # tail moves right
            if x == 2 and y == 0:
                new_tail_pos = move('D', tail_pos)
            
            # tail moves left 
            elif x == -2 and y == 0:
                new_tail_pos = move('U', tail_pos)
            
            # tail moves up
            elif x == 0 and y == -2:
                new_tail_pos = move('L', tail_pos)
                
            # tail moves down 
            elif x == 0 and y == 2:
                new_tail_pos = move('R', tail_pos)
            
            # tail moves left up
            elif x == -2 and y == -1:
                new_tail_pos = move('DLU-V', tail_pos)
                
            elif x == -1 and y == -2:
                new_tail_pos = move('DLU-H', tail_pos)
            
            # tail moves right up
            elif x == -2 and y == 1:
                new_tail_pos = move('DRU-V', tail_pos)
                
            elif x == -1 and y == 2:
                new_tail_pos = move('DRU-H', tail_pos)
                
            # tail moves left down
            elif x == 2 and y == -1:
                new_tail_pos = move('DLD-V', tail_pos)
            
            elif x == 1 and y == -2:
                new_tail_pos = move('DLD-H', tail_pos)
                
            # tail moves right down
            elif x == 2 and y == 1:
                new_tail_pos = move('DRD-V', tail_pos)
            
            elif x == 1 and y == 2:
                new_tail_pos = move('DRD-H', tail_pos)
            
            else:
                print("Invalid move: ", x, y)
                break
            
            new_tail_i, new_tail_j = new_tail_pos
            tail_pos = new_tail_pos
            part1_visited.add(new_tail_pos)
            
# print(visited)
print("Part 1:", len(part1_visited))
print(part1_visited)

