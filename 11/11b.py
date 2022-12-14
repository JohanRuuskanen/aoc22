
class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextnode = None

class DLinkedList:
    def __init__(self):
        self.headnode = None
        self.tailnode = None

    def pop(self):
        popnode = self.headnode
        self.headnode = self.headnode.nextnode
        if self.headnode == None:
            self.tailnode = None
        popnode.nextnode = None
        return popnode

    def append(self, node):        
        if self.headnode == self.tailnode == None:
            self.headnode = node
            self.tailnode = node
        else:
            self.tailnode.nextnode = node
            self.tailnode = node
    
    def to_list(self):
        node = self.headnode
        v = []
        while node != None:
            v.append(node.dataval)
            node = node.nextnode
        return v

class Monkey:
    def __init__(self, name, items, op, test, div):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.div = div

    def print(self):
        print("Monkey {}: ".format(self.name) + \
                ", ".join([str(v) for v in self.items.to_list()]))

def create_monkey(lines):
    # Extract name
    name = lines[0].split(":")[0].split(" ")[1]
    
    # Extract starting items as list of integers
    items_s = lines[1].split(":")[1].split(",")
    items = DLinkedList()
    for item_s in items_s:
        items.append(Node(int(item_s.strip())))

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

    return Monkey(name, items, op, test, div)

def main(rounds):
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

    # Supermod
    supermodulo = 1
    for monkey in monkeys:
        supermodulo *= monkey.div

    inspections = [0] * len(monkeys)
    for r in range(rounds):
        print("\nRound {}".format(r))
        for i, monkey in enumerate(monkeys):
            insp = 0
            print(monkey.items.to_list())
            while monkey.items.headnode != None:
                insp += 1
                itemnode = monkey.items.pop()
                
                itemnode.dataval = monkey.op(itemnode.dataval) % supermodulo
                
                nextmonkey = monkey.test(itemnode.dataval)
                
                monkeys[nextmonkey].items.append(itemnode)
            inspections[i] += insp
    
    return monkeys, inspections

monkeys, inspections = main(10000)

print("Monkey item list at round {}".format(rounds))         
for monkey in monkeys:
    monkey.print()
print("")
for i, monkey in enumerate(monkeys):
    print("Monkey {} inspected items {} times".format(i, inspections[i]))

inspections.sort(reverse=True)
print("11b, monkey business {}".format(inspections[0] * inspections[1]))



