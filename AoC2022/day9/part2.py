import sys 
import os 

with open(os.path.join(sys.path[0], "input0.txt"), "r") as f:
    lines = f.read().strip().splitlines()

def make_moves(moves, rope_len):
    rows = [0] * rope_len
    cols = [0] * rope_len
    
    visited = { rows[-1], cols[-1] }
    
    for (x, y), distance in moves:
        for _ in range(distance):
            rows[0] += x
            cols[0] += y
            
            for i in range(rope_len - 1):
                dx = rows[i+1] - rows[i]
                dy = cols[i+1] - cols[i]
                if abs(dx) == 2 or abs(dy) == 2:
                    rows[i+1] = rows[i] + int(dx / 2)
                    cols[i+1] = cols[i] + int(dy / 2)
            visited.add((rows[-1], cols[-1]))
    return len(visited)

dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
moves = [(dirs[line[0]], int(line[1:])) for line in lines]
print(moves)

# print("Part 1:", make_moves(moves, 2) - 1)
print("Part 2:", make_moves(moves, 10) - 1)

                    