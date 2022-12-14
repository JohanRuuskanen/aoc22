import string

with open("input", "r") as f:
    rucksacks = [line.strip() for line in f.readlines()]

chars = string.ascii_lowercase + string.ascii_uppercase
priority_map = {}
for i, c in enumerate(chars):
    priority_map[c] = i+1

def get_priority(r_group):
    for c in r_group[0]:
        if c in r_group[1] and c in r_group[2]:
            return score_map[c]
    raise Exception("No similarities found!")

r_groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
prios = [get_priority(r_g) for r_g in r_groups]

print("3a, sum of priorities: {}".format(sum(prios)))

