
# Functions for extracting nested lists

def findclosure(l, i):
    if l[i] != "[":
        raise Exception("Has to start on [")
    else:
        c = 1
        for j in range(i+1, len(l)):
            if l[j] == "[":
                c += 1
            elif l[j] == "]":
                c -= 1

            if c == 0:
                return j

def extract_list(line):
    l = []

    while len(line) > 0:
        if line[0] == "[":
            ic = findclosure(line, 0)
            l.append(extract_list(line[1:ic]))
            line = line[ic+2:] 
        else:
            if "," in line:
                i = line.index(",")
                l.append(int(line[:i]))
                line = line[i+1:]
            else:
                l.append(int(line))
                line = ""

    return l
                
# Extract the pairs of packets to be compared
pairs = []
with open("input", "r") as f:
    pair = []
    for line in f.readlines():
        if line.strip() == "":
            pairs.append(tuple(pair))
            pair = []
        else:
            pair.append(extract_list(line.strip()[1:-1]))
    if pair:
        pairs.append(tuple(pair))

# Compare the packet pairs
def clist(x):
    if type(x) == list:
        return x
    else:
        return [x]

def compare(left, right): 
   
    if len(left) == 0 and len(right) > 0:
        return 1
    elif len(left) > 0 and len(right) == 0:
        return -1
    elif len(left) == 0 and len(right) == 0:
        return 0
    elif type(left[0]) == list or type(right[0]) == list:
        res = compare(clist(left[0]), clist(right[0]))
        if res in [-1, 1]:
            return res
        return compare(left[1:], right[1:])
    elif left[0] < right[0]:
        return 1
    elif left[0] > right[0]:
        return -1
    elif len(left) == 1 and len(right) > 1:
        return 1
    elif len(left) > 1 and len(right) == 1:
        return -1
    elif len(left) > 1 and len(right) > 1:
        return compare(left[1:], right[1:])
    else:
        return 0

l = []
for i in range(len(pairs)):
    left, right = pairs[i]
    if compare(left, right) in [0, 1]:
        l.append(i+1)

print("13a, sum of indices {}".format(sum(l)))
