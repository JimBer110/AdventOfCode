lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace('\n','') for item in lines]

valves = {}

for i in range(len(lines)):
    line = lines[i].split(' ')
    for j in range(9, len(line)):
        line[j] = line[j].replace(',','')
    valves[line[1]] = {'flow': int(line[4].split('=')[1][:-1]),
                       'neighbours': line[9:]}

print(valves)
