
class Monkey:
    def __init__(self, name, items, op, test):
        self.name = name
        self.items = items
        self.op = op
        self.test = test

    def print(self):
        print("Monkey {}: ".format(self.name) + \
                ", ".join([str(v) for v in self.items]))

def create_monkey(lines):
    # Extract name
    name = lines[0].split(":")[0].split(" ")[1]
    
    # Extract starting items as list of integers
    starting_items = [int(val.strip()) \
            for val in lines[1].split(":")[1].split(",")]
    
    # Extract the operation as lambda function
    op_s = lines[2].split("=")[1].strip().split(" ")
    if op_s[0] == op_s[2] == "old":
        op = lambda x: x * x
    elif op_s[1] == "+":
        op = lambda x: x + int(op_s[2])
    elif op_s[1] == "*":
        op = lambda x: x * int(op_s[2])
    else:
        raise Exception("No such operation implemented: {}".format(line[2]))

    # Extract the test as a lambda function
    div = int(lines[3].split(" ")[-1].strip())
    iftrue = int(lines[4].split(" ")[-1].strip())
    iffalse = int(lines[5].split(" ")[-1].strip())
    test = lambda x: iftrue if x % div == 0 else iffalse

    return Monkey(name, starting_items, op, test)

with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# Create the monkeys initial conditions
monkeys = []
while len(lines) != 0:
    if "" in lines:
        sp = lines.index("")
        monkeys.append(create_monkey(lines[:sp]))
        lines = lines[(sp+1):]
    else:
        monkeys.append(create_monkey(lines))
        lines = []

# Run 20 rounds
inspections = [0] * len(monkeys)
rounds = 20
for _ in range(rounds):
    for i, monkey in enumerate(monkeys):
        inspections[i] += len(monkey.items)
        while len(monkey.items) != 0:
            item = monkey.items.pop(0)
            new_wl = monkey.op(item) // 3
            monkeys[monkey.test(new_wl)].items.append(new_wl)

print("Monkey item list at round {}".format(rounds))         
for monkey in monkeys:
    monkey.print()
print("")

inspections.sort(reverse=True)
print("11a, monkey business {}".format(inspections[0] * inspections[1]))



