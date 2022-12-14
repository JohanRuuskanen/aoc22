
intl = lambda l: [int(x) for x in l]

with open("input", "r") as f:
    idranges = []
    for line in f.readlines():
        r1, r2 = [r.split("-") for r in line.strip().split(",")]
        idranges.append(sorted([intl(r1), intl(r2)], key=lambda x: x[0]))

hit = [0] * len(idranges)
for i, (r1, r2) in enumerate(idranges):
    if r1[0] <= r2[0] and r1[1] >= r2[1]:
        hit[i] = 1
    elif r1[0] == r2[0]:
        hit[i] = 1

print("4a, complete overlaps: {}".format(sum(hit)))
