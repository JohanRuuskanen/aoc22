import numpy as np

with open("input", "r") as f:
    lines = [list(map(int, list(line.strip()))) for line in f.readlines()]
    T = np.matrix(lines)

m, n = T.shape
V = np.zeros((m, n), dtype=bool)

def is_visible(i, j):
    if (T[:i, j] < T[i, j]).all():
        return True
    elif (T[i+1:, j] < T[i, j]).all():
        return True
    elif (T[i, :j] < T[i, j]).all():
        return True
    elif (T[i, j+1:] < T[i, j]).all():
        return True
    else:
        return False

for i in range(m):
    for j in range(n):
        V[i, j] = is_visible(i, j)    
   
print("8a, total visible {}".format(sum(sum(V))))
