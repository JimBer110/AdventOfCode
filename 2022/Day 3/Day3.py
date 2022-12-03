lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [item.replace("\n","") for item in lines]

errors = []
for i in range(len(lines)):
    line = [lines[i][:len(lines[i])//2], lines[i][len(lines[i])//2:]]
    for j in range(len(line[0])):
        if line[0][j] in line[1]:
            errors.append(line[0][j])
            break

total_sum = 0
for i in range(len(errors)):
    tmp = 0
    if (errors[i].islower()):
        tmp = ord(errors[i])-ord("a")+1
    else:
        tmp = ord(errors[i])-ord("A")+27
    total_sum += tmp

print("Task 1: %s" %(total_sum))


errors = []
for i in range(len(lines)//3):

    for j in range(len(lines[i*3])):
        if lines[i*3][j] in lines[i*3+1] and lines[i*3][j] in lines[i*3+2]:
            errors.append(lines[i*3][j])
            break

total_sum = 0
for i in range(len(errors)):
    tmp = 0
    if (errors[i].islower()):
        tmp = ord(errors[i])-ord("a")+1
    else:
        tmp = ord(errors[i])-ord("A")+27
    total_sum += tmp

print("Task 2: %s" %(total_sum))
