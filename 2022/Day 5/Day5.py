lines = []

with open('input.txt', 'r') as f:
    lines = f.readlines()


stacks = []
instructions = []
for i in range(len(lines)):
    if lines[i] == '\n':
        stacks = lines[:i]
        instructions = lines[i+1:]

data = []
for i in range(len(stacks[-1])):
    if stacks[-1][i].isnumeric():
        data.append([])
        for j in range(len(stacks)-2, -1, -1):
            if stacks[j][i] != ' ':
                data[-1].append(stacks[j][i])

for i in range(len(instructions)):
    line = instructions[i].split(' ')
    for j in range(int(line[1])):
        tmp = data[int(line[3])-1].pop()
        data[int(line[5])-1].append(tmp)

result = ""
for i in range(len(data)):
    result += data[i][-1]

print("Task 1: %s" %(result))

data = []
for i in range(len(stacks[-1])):
    if stacks[-1][i].isnumeric():
        data.append([])
        for j in range(len(stacks)-2, -1, -1):
            if stacks[j][i] != ' ':
                data[-1].append(stacks[j][i])

for i in range(len(instructions)):
    line = instructions[i].split(' ')
    stack = []
    for j in range(int(line[1])):
        stack.append(data[int(line[3])-1].pop())
    for j in range(len(stack)):
        data[int(line[5])-1].append(stack.pop())

result = ""
for i in range(len(data)):
    result += data[i][-1]

print("Task 2: %s" %(result))
