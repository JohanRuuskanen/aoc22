#import pandas as pd
#stacktable = pd.read_table("testinput", header=None, )

import re

# Read the data for the stacks and for the moves
with open("input", "r") as f:
    stacklines = []
    moves = []
    read_stacks = True
    for line in f.readlines():
        if len(line.strip("\n")) == 0:
            read_stacks = False
            continue

        if read_stacks:
            stacklines.append(line.strip("\n"))
        else:
            moveline = re.split(r"move|from|to", line.strip("\n"))[1:]
            moves.append([int(m.strip()) for m in moveline])

# Create stacks from the read data
stacks = []
while len(stacklines[0]) > 0:
    s = []
    for i, line in enumerate(stacklines):
        if re.match(r"\[[A-Z]\]", line[0:3]):
            s.insert(0, line[1])
        stacklines[i] = line[4:]
    stacks.append(s)

# Move the crates
for move in moves:
    m = stacks[move[1]-1][-move[0]:]
    stacks[move[2]-1].extend(m)
    del stacks[move[1]-1][-move[0]:]

attop = "".join([s[-1] for s in stacks])
print("5b, at top: {}".format(attop))        
