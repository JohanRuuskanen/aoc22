
with open("input", "r") as f:
    commands = [line.strip() for line in f.readlines()]

X_next = 1
X_v = [X_next]
i = 0

while i < len(commands):
    if commands[i] == "noop":
        X_v.append(X_next)
    elif "addx" in commands[i]:
        X_v.append(X_next)
        X_v.append(X_next)
        X_next += int(commands[i].split()[1])
    else:
        raise Exception("No such command: {}".format(commands[i]))
    i += 1

if "addx" in commands[-1]:
    X_v.append(X_next)   

ss = sum([X_v[i]*i for i in range(20, len(X_v), 40)])
print("10a, signal strength {}".format(ss))

