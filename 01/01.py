with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def to_int(x):
    return [int(y) for y in x]

ind = [i for i, x in enumerate(lines) if x == '']
cals = [to_int(lines[0:ind[0]])]
for i in range(len(ind)-1):
    cals.append(to_int(lines[(ind[i]+1):ind[i+1]]))
cals.append(to_int(lines[(ind[-1]+1):len(lines)]))

cals_sum = sorted([sum(c) for c in cals], reverse=True)

print("1a, most calories: {}".format(cals_sum[0]))
print("1b, 3 most calories: {}".format(sum(cals_sum[0:3])))
