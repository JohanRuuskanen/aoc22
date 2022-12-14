
class Dir:
    def __init__(self, name, sup):
        self.name = name
        self.sup = sup
        self.sub = {}
        self.fs = 0
        self.ds = -1

    def print(self):
        print("name: {}".format(self.name))
        print("sup: {}".format(self.sup.name))
        print("sub: {}".format(list(self.sub.keys())))
        print("fs: {}".format(self.fs))
        print("ds: {}".format(self.ds))


with open("input", "r") as f:
    commands = [line.strip() for line in f.readlines()]

topdir = Dir("/", Dir("", ""))
curdir = ""
dirlist = [topdir]

# From the commands, create the directory tree
i = 0
while i < len(commands):
    if "$ cd" in commands[i]:
        if "$ cd /" == commands[i]:
            curdir = topdir
        elif "$ cd .." == commands[i]:
            curdir = curdir.sup
        else:
            curdir = curdir.sub[commands[i][5:]]
        i += 1

    elif "$ ls" in commands[i]:
        while i < len(commands)-1 and commands[i+1][0] != "$":
            i += 1
            if "dir" in commands[i]:
                d = Dir(commands[i][4:], curdir)
                curdir.sub[commands[i][4:]] = d
                dirlist.append(d)
            else:
                curdir.fs += int(commands[i].split(" ")[0])
        i += 1

# Walk tree to infer directory sizes
def calc_ds(d):
    sub_ds = 0
    for sd in d.sub:
        v = calc_ds(d.sub[sd]) 
        d.sub[sd].ds = v 
        sub_ds += v
    return d.fs + sub_ds

topdir.ds = calc_ds(topdir)

# Find sum of all small sizes
small_sum = 0
for d in dirlist:
    if d.ds <= 100000:
        small_sum += d.ds

# Find smallest dir to delete
sizelist = []
for d in dirlist:
    sizelist.append(d.ds)
sizelist.sort()

space_left = 70000000 - topdir.ds
needs = 30000000 - space_left

for s in sizelist:
    if s >= needs:
        break

print("7a, small sum {}".format(small_sum))
print("7b, min del size {}".format(s))

