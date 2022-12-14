import numpy as np

with open("input", "r") as f:
    commands = [line.strip() for line in f.readlines()]

H = (0, 0)
T = (0, 0)
Tvisited = set([T])

def dist(H, T):
    return max(np.abs(H[0] - T[0]), np.abs(H[1] - T[1]))

def updateT(H, T):
    d = dist(H, T)
    if d in (0, 1):
        return T
    elif d == 2:
        dy = np.sign(H[0] - T[0])
        dx = np.sign(H[1] - T[1]) 
        return (T[0] + dy, T[1] + dx)
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
        H = (H[0] + ds[0], H[1] + ds[1])
        T = updateT(H, T)
        Tvisited.add(T)

print("9a, unique tail visits {}".format(len(Tvisited)))

