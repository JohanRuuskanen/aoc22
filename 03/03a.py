import string

with open("input", "r") as f:
    rucksacks = [line.strip() for line in f.readlines()]

chars = string.ascii_lowercase + string.ascii_uppercase
priority_map = {}
for i, c in enumerate(chars):
    priority_map[c] = i+1

def get_priority(rucksack):
    comp1 = rucksack[:len(rucksack) // 2]
    comp2 = rucksack[len(rucksack) // 2:]

    for c in comp1:
        if c in comp2:
            return score_map[c]

    raise Exception("No similarities found!")

prios = [get_priority(r) for r in rucksacks]
print("3a, sum of priorities: {}".format(sum(prios)))

