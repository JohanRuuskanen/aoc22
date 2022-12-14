
intl = lambda l: [int(x) for x in l]

with open("input", "r") as f:
    idranges = []
    for line in f.readlines():
        r1, r2 = [r.split("-") for r in line.strip().split(",")]
        idranges.append(sorted([intl(r1), intl(r2)], key=lambda x: x[0]))

hit = [1] * len(idranges)
for i, (r1, r2) in enumerate(idranges):
    if r1[1] < r2[0]:
        hit[i] = 0

print("4b, complete overlaps: {}".format(sum(hit)))
