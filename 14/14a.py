import numpy as np

class Board:

    def __init__(self, rockpaths, sandstart):
        self.rockpaths_old = rockpaths
        self.sandstart = sandstart
        self.corrections()
        self.fill_board()

    def fill_board(self):
        self.board = np.matrix([["."] * self.size[1] \
                for _ in range(self.size[0])]) 
        self.board[self.sandstart] = "+"
        for rp in self.rockpaths:
            for i in range(len(rp)-1):
                lx = sorted([rp[i][0], rp[i+1][0]])
                ly = sorted([rp[i][1], rp[i+1][1]]) 
                self.board[range(lx[0], lx[1]+1), range(ly[0], ly[1]+1)] = "#"

    def corrections(self):
        all_nodes = [item for sublist in self.rockpaths_old for item in sublist]
        all_x = [p[0] for p in all_nodes]
        all_y = [p[1] for p in all_nodes]
        
        self.size = (max(all_y) + 1, max(all_x) - min(all_x) + 1)
        self.sandstart = (0, self.sandstart[0] - min(all_x))
        self.rockpaths = []
        for rp_old in self.rockpaths_old:
            rp = []
            for r in rp_old:
                rp.append((r[1], r[0] - min(all_x)))
            self.rockpaths.append(rp)
    
    def drop_sand(self):
        pos = np.array(self.sandstart)
        while True:
            if pos[0] + 1 == self.size[0]:
                return 0
            elif self.board[pos[0]+1, pos[1]] == ".":
                pos[0] += 1
            elif pos[1]-1 < 0:
                return 0
            elif self.board[pos[0]+1, pos[1]-1] == ".":
                pos[0] += 1
                pos[1] -= 1
            elif pos[1]+ 1 > self.size[1]:
                return 0
            elif self.board[pos[0]+1, pos[1]+1] == ".":
                pos[0] += 1
                pos[1] += 1
            else:
                break
        self.board[pos[0], pos[1]] = "o"
        return 1

    def print(self):
        print("")
        for i in range(self.size[0]):
            print("".join(self.board[i, :].tolist()[0]))
        print("")

with open("input", "r") as f:
    rockpaths = []
    for line in f.readlines():
        rp = []
        for val in line.strip().split("->"):
            rp.append(tuple([int(x) for x in val.strip().split(",")]))
        rockpaths.append(rp)

board = Board(rockpaths, (500, 0))

us = 0
while True:
    s = board.drop_sand()
    if s == 0:
        break
    else:
        us += 1

board.print()

print("14a, units of sand {}".format(us))


