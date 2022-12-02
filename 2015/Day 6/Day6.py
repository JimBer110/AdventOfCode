lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

all_lights = []
for i in range(1000):
    all_lights.append([0]*1000)


for i in range(len(lines)):

    line = lines[i].replace("\n",'').split(" ")

    if line[0] == "toggle":
        for j in range(int(line[1].split(",")[0]), int(line[3].split(",")[0])+1):
            for k in range(int(line[1].split(",")[1]), int(line[3].split(",")[1])+1):
                all_lights[j][k] = 1 if all_lights[j][k] == 0 else 0
    elif line[1] == "on":
        for j in range(int(line[2].split(",")[0]), int(line[4].split(",")[0])+1):
            for k in range(int(line[2].split(",")[1]), int(line[4].split(",")[1])+1):
                all_lights[j][k] = 1
    else:
        for j in range(int(line[2].split(",")[0]), int(line[4].split(",")[0])+1):
            for k in range(int(line[2].split(",")[1]), int(line[4].split(",")[1])+1):
                all_lights[j][k] = 0

total_count = 0
for i in range(len(all_lights)):
    for j in range(len(all_lights[i])):
        if all_lights[i][j]:
            total_count += 1

print("Task 1: %s" %(total_count))


all_lights = []
for i in range(1000):
    all_lights.append([0]*1000)

for i in range(len(lines)):

    line = lines[i].replace("\n",'').split(" ")

    if line[0] == "toggle":
        for j in range(int(line[1].split(",")[0]), int(line[3].split(",")[0])+1):
            for k in range(int(line[1].split(",")[1]), int(line[3].split(",")[1])+1):
                all_lights[j][k] += 2
    elif line[1] == "on":
        for j in range(int(line[2].split(",")[0]), int(line[4].split(",")[0])+1):
            for k in range(int(line[2].split(",")[1]), int(line[4].split(",")[1])+1):
                all_lights[j][k] += 1
    else:
        for j in range(int(line[2].split(",")[0]), int(line[4].split(",")[0])+1):
            for k in range(int(line[2].split(",")[1]), int(line[4].split(",")[1])+1):
                all_lights[j][k] = max(0,all_lights[j][k]-1)

total_count = 0
for i in range(len(all_lights)):
    for j in range(len(all_lights[i])):
        total_count += all_lights[i][j]

print("Task 2: %s" %(total_count))
