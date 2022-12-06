lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [line.replace("\n","") for line in lines]

data = {}

def read(_data):
    if _data.isnumeric():
        return int(_data)
    return data[_data]

stack = lines.copy()
while lines:
    line = lines.pop(0).split(" ")

    if line[0] == "NOT":
        try:
            tmp = read(line[1])
        except:
            lines.append(" ".join(line))
            continue
        tmp = tmp ^ 0b1111111111111111
        data[line[3]] = tmp
    elif line[1] == "->":
        try:
            data[line[2]] = read(line[0])
        except:
            lines.append(" ".join(line))
            continue
    else:
        try:
            tmp1 = read(line[0])
            tmp2 = read(line[2])
        except:
            lines.append(" ".join(line))
            continue
        tmp = 0
        if line[1] == "AND":
            tmp = tmp1 & tmp2
        elif line[1] == "OR":
            tmp = tmp1 | tmp2
        elif line[1] == "LSHIFT":
            tmp = tmp1 << tmp2
        elif line[1] == "RSHIFT":
            tmp = tmp1 >> tmp2
        data[line[4]] = tmp

print("Task 1: %s" %(data["a"]))


data = {'b': data['a']}
constb = data['b']
lines = stack
while lines:
    line = lines.pop(0).split(" ")
    data['b'] = constb

    if line[0] == "NOT":
        try:
            tmp = read(line[1])
        except:
            lines.append(" ".join(line))
            continue
        tmp = tmp ^ 0b1111111111111111
        data[line[3]] = tmp
    elif line[1] == "->":
        try:
            data[line[2]] = read(line[0])
        except:
            lines.append(" ".join(line))
            continue
    else:
        try:
            tmp1 = read(line[0])
            tmp2 = read(line[2])
        except:
            lines.append(" ".join(line))
            continue
        tmp = 0
        if line[1] == "AND":
            tmp = tmp1 & tmp2
        elif line[1] == "OR":
            tmp = tmp1 | tmp2
        elif line[1] == "LSHIFT":
            tmp = tmp1 << tmp2
        elif line[1] == "RSHIFT":
            tmp = tmp1 >> tmp2
        data[line[4]] = tmp

print("Task 2: %s" %(data["a"]))
