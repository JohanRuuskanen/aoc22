import numpy as np

with open("input", "r") as f:
    lines = [list(map(int, list(line.strip()))) for line in f.readlines()]
    T = np.matrix(lines)

m, n = T.shape
V = np.zeros((m, n), dtype=int)

def scenic_score(i, j):
    score = 1

    if 0 < i < (m-1) and 0 < j < (n-1): 
        for k in reversed(range(i)):
            if T[k, j] >= T[i,j] or k == 0:
                #print(k)
                score *= i-k
                break

        for k in range(i+1, m):
            if T[k, j] >= T[i, j] or k == (m-1):
                #print(k)
                score *= k-i
                break

        for k in reversed(range(j)):
            if T[i, k] >= T[i, j] or k == 0:
                #print(k)
                score *= j-k
                break

        for k in range(j+1, n):
            if T[i, k] >= T[i, j] or k == (n-1):
                #print(k)
                score *= k-j
                break
    else:
        score = 0

    return score



for i in range(m):
    for j in range(n):
        V[i, j] = scenic_score(i, j)    
   
print("8b, max score {}".format(V.max()))
