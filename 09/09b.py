import numpy as np

with open("input", "r") as f:
    commands = [line.strip() for line in f.readlines()]

R = [(0, 0)]*10
Tvisited = set([R[-1]])

def dist(K1, K2):
    return max(np.abs(K1[0] - K2[0]), np.abs(K1[1] - K2[1]))

def updateK(K1, K2):
    d = dist(K1, K2)
    if d in (0, 1):
        return K2
    elif d == 2:
        dy = np.sign(K1[0] - K2[0])
        dx = np.sign(K1[1] - K2[1]) 
        return (K2[0] + dy, K2[1] + dx)
    else:
        raise Exception("distance {}, larger than 2".format(d))

for c in commands:    
    if c[0] == "R":
        ds = (0, 1)
    elif c[0] == "L":
        ds = (0, -1)
    elif c[0] == "U":
        ds = (1, 0)
    elif c[0] == "D":
        ds = (-1, 0)
    else:
        raise Exception("Unrecognized cmd {}".format(c[0]))

    steps = int(c.split(" ")[1])

    for _ in range(steps):
        R[0] = (R[0][0] + ds[0], R[0][1] + ds[1])
        for i in range(1, len(R)):
            R[i] = updateK(R[i-1], R[i])
        Tvisited.add(R[-1])

print("9a, unique tail visits {}".format(len(Tvisited)))

