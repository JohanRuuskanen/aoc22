
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

draw_v = [["."]*40 for k in range(6)] 
for row in range(len(draw_v)):
    for col in range(len(draw_v[row])):
        cycle = row*40 + col + 1
        spos = (X_v[cycle]-1, X_v[cycle], X_v[cycle]+1) 
        if col in spos:
            draw_v[row][col] = "#"

print("10b, picture")
for row in draw_v:
    print("".join(row))


