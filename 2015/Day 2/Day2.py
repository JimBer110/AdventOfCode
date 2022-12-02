lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

total_sum = 0
total_ribbon = 0
for i in range(len(lines)):
    line = [int(item) for item in lines[i].split('x')]

    measures = []
    line.sort()
    for j in range(len(line)):
        measures.append(line[j]*line[(j+1)%len(line)])

    total_sum += min(measures)
    total_ribbon += line[0]*2+line[1]*2
    total_ribbon += line[0]*line[1]*line[2]

    for j in range(len(line)):
        total_sum += measures[j] * 2

print("Task 1: %s" %(total_sum))
print("Task 2: %s" %(total_ribbon))
