lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace("\n","") for item in lines]


class Monkey:

    def __init__(self, items, test_case, operation, if_true, if_false, monkey_array):
        self.items = items
        self.test_case = test_case
        self.operation = operation
        self.if_true = if_true
        self.if_false = if_false
        self.monkey_array = monkey_array
        self.times_thrown = 0
        self.modulo = 1

    def handle_turn(self, divide_by):
        worry_value = 0
        for i in range(len(self.items)):
            self.times_thrown += 1
            worry_value = self.items[i]
            if (self.operation[0] == "*"):
                worry_value = worry_value * eval(self.operation[2:])
            else:
                worry_value = worry_value + eval(self.operation[2:])
            worry_value = worry_value // divide_by
            worry_value = worry_value % self.modulo
            if (worry_value % self.test_case == 0):
                self.monkey_array[self.if_true].get_item(worry_value)
            else:
                self.monkey_array[self.if_false].get_item(worry_value)
        self.items = []

    def get_item(self, item):
        self.items.append(item)

monkey_array = []
modulo = 1
for i in range(0, len(lines), 7):
    starting_items = [int(item) for item in lines[i+1][18:].split(", ")]
    operation = lines[i+2][23:].replace("old", "worry_value")
    test_case = int(lines[i+3][21:])
    modulo *= test_case
    if_true = int(lines[i+4][29:])
    if_false = int(lines[i+5][30:])

    monkey_array.append(Monkey(starting_items, test_case, operation, if_true, if_false, monkey_array))
for i in monkey_array:
    i.modulo = modulo


for i in range(20):
    for j in monkey_array:
        j.handle_turn(3)

times_thrown = []
for i in monkey_array:
    times_thrown.append(i.times_thrown)
times_thrown.sort(reverse=True)

print("Task 1: %s" %(times_thrown[0]*times_thrown[1]))


monkey_array = []
for i in range(0, len(lines), 7):
    starting_items = [int(item) for item in lines[i+1][18:].split(", ")]
    operation = lines[i+2][23:].replace("old", "worry_value")
    test_case = int(lines[i+3][21:])
    if_true = int(lines[i+4][29:])
    if_false = int(lines[i+5][30:])

    monkey_array.append(Monkey(starting_items, test_case, operation, if_true, if_false, monkey_array))
for i in monkey_array:
    i.modulo = modulo

for i in range(10000):
    for j in monkey_array:
        j.handle_turn(1)

times_thrown = []
for i in monkey_array:
    times_thrown.append(i.times_thrown)
times_thrown.sort(reverse=True)

print("Task 2: %s" %(times_thrown[0]*times_thrown[1]))
