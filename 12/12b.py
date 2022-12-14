import numpy as np
from string import ascii_lowercase

with open("input", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    grid = np.matrix(lines)

endpos = tuple([x[0] for x in np.where(grid == "E")])
grid[np.where(grid == "S")] = "a"
grid[endpos] = "z"
sp = np.where(grid == "a") 
startpos = [(sp[0][i], sp[1][i]) for i in range(len(sp[0]))]
m, n = grid.shape

mapvals = {}
for i, c in enumerate(list(ascii_lowercase)):
    mapvals[c] = i

def valid_step(old, new):
    return mapvals[new] - mapvals[old] <= 1

def get_unvisited_neighbors(pos):
    neighbors = []
    
    for i in [-1, 1]:
        newpos = (pos[0] + i, pos[1]) 
        if 0 <= newpos[0] < m and valid_step(grid[pos], grid[newpos]) \
                and visited[newpos] == -1:
            neighbors.append(newpos)
    for j in [-1, 1]:
        newpos = (pos[0], pos[1] + j) 
        if 0 <= newpos[1] < n and valid_step(grid[pos], grid[newpos]) \
                and visited[newpos] == -1:
            neighbors.append(newpos)
    
    return neighbors

step = 0
visited = -1*np.ones(grid.shape, dtype=bool)
edge = set()
for sp in startpos:
    visited[sp] = step
    edge.add(sp)

while True:
    step += 1
    new_edge = set()
    while len(edge) > 0:
        node = edge.pop()
        valid_nbrs = get_unvisited_neighbors(node)
        for vn in valid_nbrs:
            new_edge.add(vn)
            visited[vn] = step
    edge = new_edge
   
    if visited[endpos] != -1:
        break

    if len(edge) == 0:
        raise Exception("No more paths")

print("12b, shortest path {}".format(visited[endpos]))




